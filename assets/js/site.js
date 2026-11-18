/* Petraquim · Ita-Bio Soluções — comportamento do site (sem dependências) */
(function () {
  'use strict';
  var doc = document.documentElement;
  doc.classList.remove('sem-js');

  var WA_NUM = '5511987769550';
  var EMAIL = 'joseroberto@petraquim.com.br';
  var CONVERSAO = 'AW-18567411730/kGkyCPjDrrYdEJLw0JVF';
  var CHAVE_CONSENT = 'pq-consentimento';

  function $(s, el) { return (el || document).querySelector(s); }
  function $$(s, el) { return Array.prototype.slice.call((el || document).querySelectorAll(s)); }
  function lerStorage(k) { try { return window.localStorage.getItem(k); } catch (e) { return null; } }
  function gravarStorage(k, v) { try { window.localStorage.setItem(k, v); } catch (e) {} }

  /* ---------- medição de contatos (Google Ads / GTM) ---------- */
  window.dataLayer = window.dataLayer || [];
  var jaContou = false;
  function medir(canal) {
    try {
      window.dataLayer.push({ event: jaContou ? 'contato_repetido' : 'contato', canal: canal });
      if (!jaContou && typeof window.gtag === 'function') {
        window.gtag('event', 'conversion', { send_to: CONVERSAO, value: 1.0, currency: 'BRL' });
      }
      jaContou = true;
    } catch (e) {}
  }
  document.addEventListener('click', function (e) {
    var a = e.target.closest ? e.target.closest('a[data-conv]') : null;
    if (a) medir(a.getAttribute('data-conv'));
  });

  /* ---------- consentimento (LGPD + Consent Mode v2) ---------- */
  var caixa = $('#consentimento');
  function aplicarConsentimento(aceito) {
    gravarStorage(CHAVE_CONSENT, aceito ? 'granted' : 'denied');
    if (typeof window.gtag === 'function') {
      var v = aceito ? 'granted' : 'denied';
      window.gtag('consent', 'update', { ad_storage: v, ad_user_data: v, ad_personalization: v, analytics_storage: v });
    }
    if (caixa) caixa.classList.remove('mostra');
  }
  if (caixa) {
    if (!lerStorage(CHAVE_CONSENT)) caixa.classList.add('mostra');
    $('[data-consent="aceitar"]', caixa).addEventListener('click', function () { aplicarConsentimento(true); });
    $('[data-consent="recusar"]', caixa).addEventListener('click', function () { aplicarConsentimento(false); });
  }
  $$('[data-abre-consentimento]').forEach(function (b) {
    b.addEventListener('click', function () { if (caixa) { caixa.classList.add('mostra'); $('button', caixa).focus(); } });
  });

  /* ---------- cabeçalho e menu ---------- */
  var topo = $('.topo');
  var menu = $('#menu-principal');
  var botaoMenu = $('.abre-menu');
  function ajustarTopo() {
    if (!topo) return;
    topo.classList.toggle('rolou', window.scrollY > 8);
    var r = topo.getBoundingClientRect();
    doc.style.setProperty('--topo-real', Math.max(0, r.bottom) + 'px');
  }
  window.addEventListener('scroll', ajustarTopo, { passive: true });
  window.addEventListener('resize', ajustarTopo);
  ajustarTopo();
  function fecharMenu() {
    if (!menu) return;
    menu.classList.remove('aberto');
    botaoMenu.setAttribute('aria-expanded', 'false');
    document.body.style.overflow = '';
  }
  if (botaoMenu && menu) {
    botaoMenu.addEventListener('click', function () {
      var abrir = !menu.classList.contains('aberto');
      ajustarTopo();
      menu.classList.toggle('aberto', abrir);
      botaoMenu.setAttribute('aria-expanded', String(abrir));
      document.body.style.overflow = abrir ? 'hidden' : '';
    });
    $$('a', menu).forEach(function (a) { a.addEventListener('click', fecharMenu); });
    document.addEventListener('keydown', function (e) { if (e.key === 'Escape') fecharMenu(); });
    window.addEventListener('resize', function () { if (window.innerWidth > 980) fecharMenu(); });
  }

  /* ---------- animação de entrada ---------- */
  var rv = $$('.rv');
  if ('IntersectionObserver' in window) {
    var io = new IntersectionObserver(function (en) {
      en.forEach(function (x) { if (x.isIntersecting) { x.target.classList.add('in'); io.unobserve(x.target); } });
    }, { threshold: 0.12, rootMargin: '0px 0px -40px 0px' });
    rv.forEach(function (el) { io.observe(el); });
  } else { rv.forEach(function (el) { el.classList.add('in'); }); }

  /* ---------- índice com destaque da seção atual ---------- */
  var links = $$('.indice a');
  if (links.length && 'IntersectionObserver' in window) {
    var mapa = {};
    links.forEach(function (a) { mapa[a.getAttribute('href').slice(1)] = a; });
    var spy = new IntersectionObserver(function (en) {
      en.forEach(function (x) {
        if (x.isIntersecting && mapa[x.target.id]) {
          links.forEach(function (l) { l.classList.remove('ativo'); });
          mapa[x.target.id].classList.add('ativo');
        }
      });
    }, { rootMargin: '-30% 0px -60% 0px' });
    Object.keys(mapa).forEach(function (id) { var s = document.getElementById(id); if (s) spy.observe(s); });
  }

  /* ---------- vídeo: pausar/retomar e respeitar movimento reduzido ---------- */
  var reduzir = window.matchMedia && window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  $$('[data-video]').forEach(function (fig) {
    var v = $('video', fig), b = $('.video-ctrl', fig);
    if (!v) return;
    if (reduzir) { v.removeAttribute('autoplay'); v.pause(); }
    function rotulo() {
      if (!b) return;
      b.setAttribute('aria-label', v.paused ? 'Reproduzir vídeo' : 'Pausar vídeo');
      b.innerHTML = v.paused
        ? '<svg viewBox="0 0 24 24" fill="currentColor"><path d="M8 5v14l11-7z"/></svg>'
        : '<svg viewBox="0 0 24 24" fill="currentColor"><path d="M7 5h4v14H7zM13 5h4v14h-4z"/></svg>';
    }
    if (b) b.addEventListener('click', function () { if (v.paused) v.play(); else v.pause(); });
    v.addEventListener('play', rotulo); v.addEventListener('pause', rotulo); rotulo();
  });

  /* ---------- galeria ampliada ---------- */
  var lb = $('#lightbox');
  if (lb) {
    var itens = $$('[data-amplia]');
    var atual = 0, origem = null;
    var img = $('img', lb), legenda = $('p', lb);
    function mostrar(i) {
      atual = (i + itens.length) % itens.length;
      var it = itens[atual];
      img.src = it.getAttribute('data-amplia');
      img.alt = it.getAttribute('data-legenda') || '';
      legenda.textContent = it.getAttribute('data-legenda') || '';
    }
    function abrir(i) { origem = document.activeElement; mostrar(i); lb.classList.add('aberto'); lb.setAttribute('aria-hidden', 'false'); document.body.style.overflow = 'hidden'; $('.fecha', lb).focus(); }
    function fechar() { lb.classList.remove('aberto'); lb.setAttribute('aria-hidden', 'true'); document.body.style.overflow = ''; if (origem) origem.focus(); }
    itens.forEach(function (it, i) { it.addEventListener('click', function () { abrir(i); }); });
    $('.fecha', lb).addEventListener('click', fechar);
    $('.ant', lb).addEventListener('click', function () { mostrar(atual - 1); });
    $('.prox', lb).addEventListener('click', function () { mostrar(atual + 1); });
    lb.addEventListener('click', function (e) { if (e.target === lb) fechar(); });
    document.addEventListener('keydown', function (e) {
      if (!lb.classList.contains('aberto')) return;
      if (e.key === 'Escape') fechar();
      if (e.key === 'ArrowLeft') mostrar(atual - 1);
      if (e.key === 'ArrowRight') mostrar(atual + 1);
    });
  }

  /* ---------- formulário de cotação ---------- */
  $$('form.js-cotacao').forEach(function (f) {
    var params = new URLSearchParams(window.location.search);
    ['quantidade', 'granulometria', 'embalagem', 'aplicacao'].forEach(function (n) {
      var v = params.get(n), el = f.elements[n];
      if (v && el) el.value = v;
    });

    function valor(n) { var el = f.elements[n]; return el && el.value.trim() ? el.value.trim() : ''; }
    function validar() {
      var ok = true, primeiro = null;
      $$('[required]', f).forEach(function (el) {
        var erro = $('#' + el.id + '-erro', f);
        var invalido = !el.value.trim() || (el.type === 'email' && el.value && !/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(el.value));
        el.setAttribute('aria-invalid', invalido ? 'true' : 'false');
        if (erro) erro.classList.toggle('mostra', invalido);
        if (invalido) { ok = false; if (!primeiro) primeiro = el; }
      });
      var email = f.elements.email;
      if (email && email.value && !/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(email.value)) {
        email.setAttribute('aria-invalid', 'true');
        var e2 = $('#' + email.id + '-erro', f); if (e2) e2.classList.add('mostra');
        ok = false; if (!primeiro) primeiro = email;
      }
      if (primeiro) primeiro.focus();
      return ok;
    }
    $$('input,select,textarea', f).forEach(function (el) {
      el.addEventListener('input', function () {
        if (el.getAttribute('aria-invalid') === 'true') {
          el.setAttribute('aria-invalid', 'false');
          var erro = $('#' + el.id + '-erro', f); if (erro) erro.classList.remove('mostra');
        }
      });
    });
    function mensagem() {
      var linhas = [
        'Olá! Gostaria de uma cotação de Alumina Ativada.',
        '',
        'Nome: ' + valor('nome'),
        'Empresa: ' + (valor('empresa') || '—'),
        'Telefone/WhatsApp: ' + valor('telefone'),
        'E-mail: ' + (valor('email') || '—'),
        'Granulometria: ' + valor('granulometria'),
        'Embalagem: ' + valor('embalagem'),
        'Quantidade total: ' + valor('quantidade'),
        'Frequência de compra: ' + (valor('frequencia') || '—'),
        'Cidade/UF de entrega: ' + valor('cidade'),
        'Aplicação e observações: ' + (valor('aplicacao') || '—')
      ];
      return linhas.join('\n');
    }
    var status = $('.status-form', f);
    function avisar(txt) { if (status) { status.textContent = txt; status.classList.add('mostra'); } }

    f.addEventListener('submit', function (e) {
      e.preventDefault();
      if (!validar()) return;
      medir('form-whatsapp');
      window.open('https://wa.me/' + WA_NUM + '?text=' + encodeURIComponent(mensagem()), '_blank', 'noopener');
      avisar('Abrimos o WhatsApp com a sua mensagem pronta. Basta tocar em enviar.');
    });
    var be = $('[data-enviar="email"]', f);
    if (be) be.addEventListener('click', function () {
      if (!validar()) return;
      medir('form-email');
      var assunto = 'Cotação - Alumina Ativada' + (valor('empresa') ? ' - ' + valor('empresa') : '');
      window.location.href = 'mailto:' + EMAIL + '?subject=' + encodeURIComponent(assunto) + '&body=' + encodeURIComponent(mensagem());
      avisar('Abrimos o seu programa de e-mail com a mensagem pronta. Se nada abriu, escreva para ' + EMAIL + '.');
    });
  });

  /* ---------- calculadora de estimativa de massa ---------- */
  var calc = $('#calc-leito');
  if (calc) {
    // Umidade do ar saturado (g de água por m³) à pressão atmosférica
    var SAT = { 20: 17.3, 25: 23.0, 30: 30.4, 35: 39.6, 40: 51.1, 45: 65.4 };
    var CAP = 0.12;      // capacidade dinâmica de trabalho adotada (12 % em massa)
    var MARGEM = 1.2;    // margem de 20 % para envelhecimento
    var DENS = 0.77;     // densidade aparente compactada, kg/L
    var fmt = function (n, d) { return n.toLocaleString('pt-BR', { minimumFractionDigits: d, maximumFractionDigits: d }); };
    function sugestao(kg) {
      var emb = [1, 5, 25, 50, 200, 1000];
      for (var i = 0; i < emb.length; i++) if (kg <= emb[i]) return '1 embalagem de ' + fmt(emb[i], 0) + ' kg';
      var n = Math.ceil(kg / 1000);
      return n + ' embalagens de 1.000 kg';
    }
    function calcular() {
      var q = parseFloat(String(calc.vazao.value).replace(',', '.'));
      var p = parseFloat(String(calc.pressao.value).replace(',', '.'));
      var t = parseInt(calc.temperatura.value, 10);
      var h = parseFloat(String(calc.ciclo.value).replace(',', '.'));
      var saida = $('#calc-saida');
      if (!(q > 0) || !(p >= 0) || !(h > 0)) {
        $('#calc-kg').innerHTML = '—';
        $('#calc-agua').textContent = 'Preencha vazão, pressão e tempo de ciclo.';
        $('#calc-vol').textContent = '';
        $('#calc-emb').textContent = '';
        return;
      }
      var pAbs = (p + 1.013) / 1.013;              // pressão absoluta em atm
      var teor = SAT[t] / pAbs;                    // g de água por Nm³ após resfriador
      var agua = q * teor * h;                     // g por ciclo
      var kg = (agua / 1000) / CAP * MARGEM;
      var litros = kg / DENS;
      $('#calc-kg').innerHTML = fmt(kg, kg < 10 ? 1 : 0) + '<small>kg</small>';
      $('#calc-agua').textContent = 'Água retida por ciclo: ≈ ' + fmt(agua, 0) + ' g (' + fmt(teor, 1) + ' g/Nm³ após o resfriador).';
      $('#calc-vol').textContent = 'Volume de leito: ≈ ' + fmt(litros, 1) + ' litros.';
      $('#calc-emb').textContent = 'Sugestão de compra: ' + sugestao(kg) + '.';
      var link = $('#calc-cotar');
      if (link) {
        var qs = new URLSearchParams({ quantidade: fmt(Math.ceil(kg), 0) + ' kg (estimativa da calculadora)', aplicacao: 'Secador de ar comprimido: ' + fmt(q, 0) + ' Nm³/h, ' + fmt(p, 1) + ' bar, ' + t + ' °C, ciclo de ' + fmt(h, 1) + ' h.' });
        link.href = 'cotacao.html?' + qs.toString() + '#formulario';
      }
      if (saida) saida.setAttribute('data-ok', '1');
    }
    calc.addEventListener('input', calcular);
    calc.addEventListener('submit', function (e) { e.preventDefault(); calcular(); });
    calcular();
  }

  /* ---------- ano no rodapé ---------- */
  $$('[data-ano]').forEach(function (el) { el.textContent = new Date().getFullYear(); });
})();

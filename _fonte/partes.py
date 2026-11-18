# -*- coding: utf-8 -*-
"""Partes comuns das páginas (cabeçalho, rodapé, ícones, imagens).
Gerar o site:  python _fonte/gerar.py   (a partir da pasta do site)"""

SITE = "https://www.petraquim.com.br"
WA = "5511987769550"
WA_MSG = "Ol%C3%A1!%20Gostaria%20de%20uma%20cota%C3%A7%C3%A3o%20de%20Alumina%20Ativada."
WA_LINK = f"https://wa.me/{WA}?text={WA_MSG}"
ML_LINK = "https://produto.mercadolivre.com.br/MLB-7984362474"
EMAIL = "joseroberto@petraquim.com.br"
TEL = "+551122673311"
TEL_TXT = "(11) 2267-3311"
WA_TXT = "(11) 98776-9550"
FDS = "FDS-Alumina-Ativada-Ita-Bio.pdf"
INSTAGRAM = "https://www.instagram.com/itabio.solucoes/"
MAPA = "https://www.google.com/maps/search/?api=1&query=Av.+Paulista,+2073+-+Bela+Vista,+S%C3%A3o+Paulo+-+SP,+01311-010"

# dimensões reais dos arquivos gerados em assets/img (largura: altura)
IMGS = {
    "alumina-copo": [(640, 724), (1000, 1132), (1400, 1584)],
    "alumina-tigela": [(600, 750), (1000, 1250)],
    "alumina-embalagem": [(600, 750), (1000, 1250)],
    "alumina-porcao": [(600, 750), (1000, 1250)],
    "alumina-textura": [(800, 800), (1200, 1200)],
    "alumina-regua-1": [(600, 1067), (900, 1600)],
    "alumina-regua-2": [(600, 1067), (900, 1600)],
    "alumina-detalhe": [(800, 800)],
    "alumina-video-capa": [(576, 1024)],
    "ind-tubulacao": [(1000, 562), (1920, 1080)],
    "app-gases": [(800, 533), (1400, 933)],
    "app-liquidos": [(800, 533), (1400, 933)],
    "app-guarda": [(800, 533), (1400, 933)],
    "app-laboratorio": [(800, 533), (1400, 933)],
    "logistica": [(800, 533), (1400, 933)],
    "app-ar-comprimido": [(800, 533), (1400, 934)],
    "app-oleos": [(800, 533), (1400, 933)],
}


def pic(nome, alt, sizes="100vw", classe="", ansioso=False):
    """<picture> com WebP + JPG, srcset e dimensões intrínsecas (evita salto de layout)."""
    v = IMGS[nome]
    srcset_w = ", ".join(f"assets/img/{nome}-{w}.webp {w}w" for w, h in v)
    srcset_j = ", ".join(f"assets/img/{nome}-{w}.jpg {w}w" for w, h in v)
    w, h = v[-1] if len(v) < 3 else v[1]
    carga = 'fetchpriority="high"' if ansioso else 'loading="lazy" decoding="async"'
    cls = f' class="{classe}"' if classe else ""
    return (f'<picture><source type="image/webp" srcset="{srcset_w}" sizes="{sizes}">'
            f'<img{cls} src="assets/img/{nome}-{w}.jpg" srcset="{srcset_j}" sizes="{sizes}" '
            f'width="{w}" height="{h}" alt="{alt}" {carga}></picture>')


def maior(nome, ext="jpg"):
    w, h = IMGS[nome][-1]
    return f"assets/img/{nome}-{w}.{ext}"


ICONES = """<svg width="0" height="0" style="position:absolute" aria-hidden="true" focusable="false">
 <symbol id="i-check" viewBox="0 0 24 24"><circle cx="12" cy="12" r="11" fill="#C5A253"/><path d="M7 12.5l3.2 3.2L17 9" fill="none" stroke="#2F3514" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"/></symbol>
 <symbol id="i-wa" viewBox="0 0 24 24"><path fill="currentColor" d="M12 2a10 10 0 0 0-8.6 15.1L2 22l5-1.3A10 10 0 1 0 12 2zm0 18.2a8.2 8.2 0 0 1-4.2-1.2l-.3-.2-3 .8.8-2.9-.2-.3A8.2 8.2 0 1 1 12 20.2zm4.5-6.1c-.2-.1-1.5-.7-1.7-.8s-.4-.1-.6.1-.6.8-.8 1-.3.2-.5.1a6.7 6.7 0 0 1-3.3-2.9c-.3-.4.3-.4.7-1.3.1-.2 0-.3 0-.4l-.8-1.8c-.2-.5-.4-.4-.6-.4h-.5a1 1 0 0 0-.7.3 3 3 0 0 0-.9 2.2 5.2 5.2 0 0 0 1.1 2.7 11.9 11.9 0 0 0 4.6 4c1.7.7 2.3.8 3.2.7a2.7 2.7 0 0 0 1.8-1.3 2.2 2.2 0 0 0 .2-1.3c-.1-.1-.2-.2-.5-.3z"/></symbol>
 <symbol id="i-mail" viewBox="0 0 24 24"><g fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="3" y="5" width="18" height="14" rx="2"/><path d="M3.5 6.5l8.5 6.5 8.5-6.5"/></g></symbol>
 <symbol id="i-fone" viewBox="0 0 24 24"><path fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" d="M5 4h4l2 5-2.5 1.5a11 11 0 0 0 5 5L15 13l5 2v4a2 2 0 0 1-2 2A16 16 0 0 1 3 6a2 2 0 0 1 2-2"/></symbol>
 <symbol id="i-pin" viewBox="0 0 24 24"><g fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M12 21s-7-6.2-7-11.5a7 7 0 0 1 14 0C19 14.8 12 21 12 21z"/><circle cx="12" cy="9.5" r="2.5"/></g></symbol>
 <symbol id="i-seta" viewBox="0 0 24 24"><path fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round" d="M5 12h14M13 6l6 6-6 6"/></symbol>
 <symbol id="i-doc" viewBox="0 0 24 24"><g fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M14 3H7a2 2 0 0 0-2 2v14a2 2 0 0 0 2 2h10a2 2 0 0 0 2-2V8z"/><path d="M14 3v5h5M9 13h6M9 17h6"/></g></symbol>
 <symbol id="i-baixar" viewBox="0 0 24 24"><path fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" d="M12 4v11m0 0l-4.5-4.5M12 15l4.5-4.5M5 20h14"/></symbol>
 <symbol id="i-ar" viewBox="0 0 24 24"><path fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" d="M3 8h11a3 3 0 1 0-3-3M3 12h16a3 3 0 1 1-3 3M3 16h8"/></symbol>
 <symbol id="i-gota" viewBox="0 0 24 24"><path fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" d="M12 3s6 6.6 6 11a6 6 0 0 1-12 0c0-4.4 6-11 6-11zM9 15a3 3 0 0 0 3 3"/></symbol>
 <symbol id="i-escudo" viewBox="0 0 24 24"><path fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" d="M12 3l7 3v5c0 4.5-3 8.3-7 10-4-1.7-7-5.5-7-10V6zM9 12l2 2 4-4"/></symbol>
 <symbol id="i-frasco" viewBox="0 0 24 24"><path fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" d="M9 3h6M10 3v6L5 18a2 2 0 0 0 1.8 3h10.4A2 2 0 0 0 19 18l-5-9V3M7.5 14h9"/></symbol>
 <symbol id="i-chama" viewBox="0 0 24 24"><path fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" d="M12 3c1 3 4 4.5 4 9a4 4 0 0 1-8 0c0-2 1-3 1-3s.5 2 2 2c0-3-1-5 1-8z"/></symbol>
 <symbol id="i-ciclo" viewBox="0 0 24 24"><path fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" d="M20 12a8 8 0 1 1-2.3-5.7M20 4v4h-4"/></symbol>
 <symbol id="i-caminhao" viewBox="0 0 24 24"><g fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M3 6h11v10H3zM14 9h4l3 3v4h-7z"/><circle cx="7" cy="17.5" r="1.8"/><circle cx="17" cy="17.5" r="1.8"/></g></symbol>
 <symbol id="i-caixa" viewBox="0 0 24 24"><g fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M21 8l-9-5-9 5 9 5 9-5zM3 8v8l9 5 9-5V8M12 13v8"/></g></symbol>
 <symbol id="i-pessoa" viewBox="0 0 24 24"><g fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="8" r="4"/><path d="M4 21a8 8 0 0 1 16 0"/></g></symbol>
 <symbol id="i-lupa" viewBox="0 0 24 24"><g fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round"><circle cx="11" cy="11" r="7"/><path d="M20 20l-4-4"/></g></symbol>
 <symbol id="i-info" viewBox="0 0 24 24"><g fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><circle cx="12" cy="12" r="9"/><path d="M12 11v6M12 7.5v.01"/></g></symbol>
 <symbol id="i-alerta" viewBox="0 0 24 24"><g fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M12 3l10 18H2z"/><path d="M12 10v5M12 18v.01"/></g></symbol>
 <symbol id="i-menu" viewBox="0 0 24 24"><path fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" d="M4 7h16M4 12h16M4 17h16"/></symbol>
 <symbol id="i-insta" viewBox="0 0 24 24"><g fill="none" stroke="currentColor" stroke-width="1.8"><rect x="3" y="3" width="18" height="18" rx="5"/><circle cx="12" cy="12" r="4"/><circle cx="17.5" cy="6.5" r=".6" fill="currentColor"/></g></symbol>
 <symbol id="i-carrinho" viewBox="0 0 24 24"><g fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="9" cy="20" r="1.4"/><circle cx="18" cy="20" r="1.4"/><path d="M2 3h3l2.5 12h11l2-8H6.2"/></g></symbol>
 <symbol id="i-fabrica" viewBox="0 0 24 24"><path fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" d="M3 21V10l6 4V10l6 4V4h4v17zM7 17h2M12 17h2"/></symbol>
 <symbol id="i-medidor" viewBox="0 0 24 24"><g fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round"><path d="M4 18a9 9 0 1 1 16 0"/><path d="M12 14l4-5"/><circle cx="12" cy="14" r="1.3" fill="currentColor"/></g></symbol>
</svg>"""

MONOGRAMA = """<svg viewBox="0 0 56 56" aria-hidden="true"><circle cx="28" cy="28" r="26" fill="none" stroke="#C5A253" stroke-width="1.6"/><circle cx="28" cy="28" r="21.5" fill="none" stroke="#C5A253" stroke-width=".8" opacity=".7"/><text x="28" y="34.5" text-anchor="middle" font-family="Lora,Georgia,serif" font-size="17" fill="#C5A253" letter-spacing=".5">IB</text></svg>"""


def cabeca(titulo, descricao, caminho, og_img="assets/img/og-alumina.jpg", jsonld="", preload=""):
    url = SITE + "/" + caminho
    return f"""<!doctype html>
<html lang="pt-BR" class="sem-js">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>{titulo}</title>
<meta name="description" content="{descricao}">
<link rel="canonical" href="{url}">
<meta name="robots" content="index, follow, max-image-preview:large">
<meta name="theme-color" content="#2F3514">
<meta name="format-detection" content="telephone=no">
<link rel="icon" href="favicon.svg" type="image/svg+xml">
<link rel="icon" href="favicon-64.png" type="image/png" sizes="64x64">
<link rel="apple-touch-icon" href="apple-touch-icon.png">
<link rel="manifest" href="site.webmanifest">
<meta property="og:type" content="website">
<meta property="og:locale" content="pt_BR">
<meta property="og:site_name" content="Petraquim · Ita-Bio Soluções">
<meta property="og:title" content="{titulo}">
<meta property="og:description" content="{descricao}">
<meta property="og:url" content="{url}">
<meta property="og:image" content="{SITE}/{og_img}">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta property="og:image:alt" content="Alumina ativada em grânulos esféricos brancos">
<meta name="twitter:card" content="summary_large_image">
<!-- Google: modo de consentimento (LGPD) + Google Tag Manager + tag do Google Ads -->
<script>
window.dataLayer=window.dataLayer||[];function gtag(){{dataLayer.push(arguments);}}
gtag('consent','default',{{ad_storage:'denied',ad_user_data:'denied',ad_personalization:'denied',analytics_storage:'denied',wait_for_update:500}});
try{{if(localStorage.getItem('pq-consentimento')==='granted'){{gtag('consent','update',{{ad_storage:'granted',ad_user_data:'granted',ad_personalization:'granted',analytics_storage:'granted'}});}}}}catch(e){{}}
gtag('js',new Date());gtag('config','AW-18567411730');
(function(w,d,s,l,i){{w[l]=w[l]||[];w[l].push({{'gtm.start':new Date().getTime(),event:'gtm.js'}});var f=d.getElementsByTagName(s)[0],j=d.createElement(s),dl=l!='dataLayer'?'&l='+l:'';j.async=true;j.src='https://www.googletagmanager.com/gtm.js?id='+i+dl;f.parentNode.insertBefore(j,f);}})(window,document,'script','dataLayer','GTM-KXJSFW6B');
</script>
<script async src="https://www.googletagmanager.com/gtag/js?id=AW-18567411730"></script>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Lato:wght@400;700&family=Lora:wght@500;600&display=swap" rel="stylesheet">
{preload}<link rel="stylesheet" href="assets/css/site.css?v=2">
{jsonld}</head>"""


MENU = [
    ("index.html", "Início"),
    ("alumina-ativada.html", "Alumina Ativada"),
    ("aplicacoes.html", "Aplicações"),
    ("empresa.html", "Empresa"),
]


def topo(ativo):
    itens = "".join(
        f'<a href="{h}"{" aria-current=\"page\"" if h == ativo else ""}>{t}</a>' for h, t in MENU)
    cta_atual = ' aria-current="page"' if ativo == "cotacao.html" else ""
    return f"""<body>
<noscript><iframe src="https://www.googletagmanager.com/ns.html?id=GTM-KXJSFW6B" height="0" width="0" style="display:none;visibility:hidden" title="Google Tag Manager"></iframe></noscript>
<a class="pular" href="#conteudo">Pular para o conteúdo</a>
{ICONES}
<div class="barra">
 <div class="wrap">
  <span class="selo-barra">Ita-Bio Soluções Ltda. · São Paulo/SP · Atendimento em todo o Brasil</span>
  <div class="contatos">
   <a href="tel:{TEL}" data-conv="telefone"><svg><use href="#i-fone"/></svg>{TEL_TXT}</a>
   <a href="{WA_LINK}" target="_blank" rel="noopener" data-conv="whatsapp"><svg><use href="#i-wa"/></svg>{WA_TXT}</a>
   <a class="email-barra" href="mailto:{EMAIL}" data-conv="email"><svg><use href="#i-mail"/></svg>{EMAIL}</a>
  </div>
 </div>
</div>
<header class="topo">
 <div class="wrap">
  <a class="marca" href="index.html" aria-label="Ita-Bio Soluções · Petraquim — página inicial"><img src="assets/img/logo-itabio.png" alt="Ita-Bio Soluções" width="144" height="52"></a>
  <button class="abre-menu" type="button" aria-expanded="false" aria-controls="menu-principal"><svg><use href="#i-menu"/></svg>Menu</button>
  <nav class="menu" id="menu-principal" aria-label="Principal">
   {itens}
   <a class="menu-cta" href="cotacao.html"{cta_atual}>Pedir cotação</a>
  </nav>
 </div>
</header>
<main id="conteudo">"""


def cta_final(titulo="Precisa de alumina ativada?", texto="Fale direto com o nosso gerente de vendas. Respondemos com granulometria indicada, embalagem e condições para a sua cidade."):
    return f"""
<section class="cta-final" aria-labelledby="cta-titulo">
 <div class="wrap">
  <div>
   <h2 id="cta-titulo">{titulo}</h2>
   <p>{texto}</p>
  </div>
  <div class="botoes">
   <a class="btn btn-wa" href="{WA_LINK}" target="_blank" rel="noopener" data-conv="whatsapp"><svg><use href="#i-wa"/></svg>Chamar no WhatsApp</a>
   <a class="btn btn-claro" href="cotacao.html">Montar cotação</a>
  </div>
 </div>
</section>"""


def rodape(lightbox=False):
    lb = """
<div class="lightbox" id="lightbox" role="dialog" aria-modal="true" aria-label="Foto ampliada" aria-hidden="true">
 <button class="fecha" type="button" aria-label="Fechar"><svg viewBox="0 0 24 24"><path fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" d="M6 6l12 12M18 6L6 18"/></svg></button>
 <button class="ant" type="button" aria-label="Foto anterior"><svg viewBox="0 0 24 24"><path fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round" d="M15 5l-7 7 7 7"/></svg></button>
 <img src="data:image/gif;base64,R0lGODlhAQABAAAAACw=" alt="">
 <button class="prox" type="button" aria-label="Próxima foto"><svg viewBox="0 0 24 24"><path fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round" d="M9 5l7 7-7 7"/></svg></button>
 <p></p>
</div>""" if lightbox else ""
    return f"""</main>
<footer class="rodape">
 <div class="wrap colunas">
  <div>
   <div class="assinatura-marca">{MONOGRAMA}<div><strong>ITA-BIO SOLUÇÕES LTDA</strong><span>Petraquim</span></div></div>
   <address>
    Av. Paulista, 2073 — Bela Vista<br>
    CEP 01311-010 — São Paulo/SP<br>
    CNPJ 14.392.945/0001-00<br>
    I.E. 161.624.00.116
   </address>
  </div>
  <div>
   <h2>Produto</h2>
   <ul>
    <li><a href="alumina-ativada.html">Alumina ativada</a></li>
    <li><a href="alumina-ativada.html#especificacao">Especificação</a></li>
    <li><a href="alumina-ativada.html#calculadora">Calculadora de leito</a></li>
    <li><a href="aplicacoes.html">Aplicações</a></li>
    <li><a href="{FDS}" download data-conv="fds">FDS (PDF)</a></li>
   </ul>
  </div>
  <div>
   <h2>Empresa</h2>
   <ul>
    <li><a href="empresa.html">Quem somos</a></li>
    <li><a href="alumina-ativada.html#perguntas">Perguntas frequentes</a></li>
    <li><a href="cotacao.html">Pedir cotação</a></li>
    <li><a href="politica-de-privacidade.html">Política de privacidade</a></li>
   </ul>
  </div>
  <div>
   <h2>Contato</h2>
   <ul>
    <li><a href="tel:{TEL}" data-conv="telefone">{TEL_TXT}</a></li>
    <li><a href="{WA_LINK}" target="_blank" rel="noopener" data-conv="whatsapp">{WA_TXT} (WhatsApp)</a></li>
    <li><a href="mailto:{EMAIL}" data-conv="email">{EMAIL}</a></li>
    <li><a href="{INSTAGRAM}" target="_blank" rel="noopener">Instagram @itabio.solucoes</a></li>
    <li><a href="{ML_LINK}" target="_blank" rel="noopener" data-conv="mercadolivre">Loja no Mercado Livre</a></li>
   </ul>
  </div>
 </div>
 <div class="base">
  <div class="wrap">
   <span>© <span data-ano>2026</span> Ita-Bio Soluções Ltda. Todos os direitos reservados.</span>
   <span><a href="politica-de-privacidade.html">Privacidade</a> · <button type="button" data-abre-consentimento>Preferências de cookies</button></span>
  </div>
 </div>
</footer>
<a class="wa-flutuante" href="{WA_LINK}" target="_blank" rel="noopener" data-conv="whatsapp" aria-label="Falar pelo WhatsApp"><svg><use href="#i-wa"/></svg><span>WhatsApp</span></a>
<div class="consentimento" id="consentimento" role="dialog" aria-labelledby="consent-titulo" aria-live="polite">
 <h2 id="consent-titulo">Sua privacidade</h2>
 <p>Usamos cookies do Google apenas para medir o resultado dos nossos anúncios. Você pode aceitar ou recusar; o site funciona igual. <a href="politica-de-privacidade.html">Saiba mais</a>.</p>
 <div class="botoes"><button class="btn btn-contorno" type="button" data-consent="recusar">Recusar</button><button class="btn btn-primario" type="button" data-consent="aceitar">Aceitar</button></div>
</div>{lb}
<script src="assets/js/site.js?v=2" defer></script>
</body>
</html>
"""


def migalhas(itens):
    """itens: lista de (rótulo, href ou None). Gera HTML + JSON-LD BreadcrumbList."""
    html = '<nav class="migalhas" aria-label="Você está em"><ol>'
    ld = []
    for i, (t, h) in enumerate(itens, 1):
        if h:
            html += f'<li><a href="{h}">{t}</a></li>'
            ld.append(f'{{"@type":"ListItem","position":{i},"name":"{t}","item":"{SITE}/{"" if h == "index.html" else h}"}}')
        else:
            html += f'<li aria-current="page">{t}</li>'
            ld.append(f'{{"@type":"ListItem","position":{i},"name":"{t}"}}')
    html += "</ol></nav>"
    jl = '{"@context":"https://schema.org","@type":"BreadcrumbList","itemListElement":[' + ",".join(ld) + "]}"
    return html, jl


def formulario(id_form="formulario", titulo="Monte sua cotação", nivel="h2"):
    return f"""<form class="form-cotacao js-cotacao rv" id="{id_form}" novalidate aria-labelledby="{id_form}-titulo">
 <{nivel} id="{id_form}-titulo">{titulo}</{nivel}>
 <p class="intro">Preencha e envie pelo WhatsApp ou por e-mail. Quem responde é José Roberto Rocha, Gerente de Vendas.</p>
 <div class="campos">
  <div class="campo"><label for="{id_form}-nome">Nome *</label><input id="{id_form}-nome" name="nome" autocomplete="name" required aria-describedby="{id_form}-nome-erro"><span class="erro" id="{id_form}-nome-erro">Informe seu nome.</span></div>
  <div class="campo"><label for="{id_form}-empresa">Empresa <span class="opc">(opcional)</span></label><input id="{id_form}-empresa" name="empresa" autocomplete="organization"></div>
  <div class="campo"><label for="{id_form}-telefone">Telefone / WhatsApp *</label><input id="{id_form}-telefone" name="telefone" type="tel" inputmode="tel" autocomplete="tel" placeholder="(11) 90000-0000" required aria-describedby="{id_form}-telefone-erro"><span class="erro" id="{id_form}-telefone-erro">Informe um telefone para retorno.</span></div>
  <div class="campo"><label for="{id_form}-email">E-mail <span class="opc">(opcional)</span></label><input id="{id_form}-email" name="email" type="email" inputmode="email" autocomplete="email" aria-describedby="{id_form}-email-erro"><span class="erro" id="{id_form}-email-erro">Confira o e-mail digitado.</span></div>
  <div class="campo"><label for="{id_form}-gran">Granulometria</label><select id="{id_form}-gran" name="granulometria"><option>7 x 14 mesh (≈ 1,2 a 2,8 mm)</option><option>2,0 a 3,0 mm</option><option>Não sei / preciso de orientação</option></select></div>
  <div class="campo"><label for="{id_form}-emb">Embalagem</label><select id="{id_form}-emb" name="embalagem"><option>1 kg</option><option>5 kg</option><option selected>25 kg</option><option>50 kg</option><option>200 kg</option><option>1.000 kg</option><option>Preciso de orientação</option></select></div>
  <div class="campo"><label for="{id_form}-qtd">Quantidade total *</label><input id="{id_form}-qtd" name="quantidade" placeholder="Ex.: 100 kg" required aria-describedby="{id_form}-qtd-erro"><span class="erro" id="{id_form}-qtd-erro">Informe a quantidade aproximada.</span></div>
  <div class="campo"><label for="{id_form}-freq">Frequência de compra</label><select id="{id_form}-freq" name="frequencia"><option>Compra única</option><option>Mensal</option><option>Trimestral</option><option>Semestral ou anual</option></select></div>
  <div class="campo cheio"><label for="{id_form}-cidade">Cidade / UF de entrega *</label><input id="{id_form}-cidade" name="cidade" autocomplete="address-level2" placeholder="Ex.: Campinas/SP" required aria-describedby="{id_form}-cidade-erro"><span class="erro" id="{id_form}-cidade-erro">Informe a cidade de entrega.</span></div>
  <div class="campo cheio"><label for="{id_form}-app">Aplicação e observações</label><textarea id="{id_form}-app" name="aplicacao" placeholder="Ex.: secador de ar comprimido de 50 Nm³/h, 7 bar; troca a cada 12 meses"></textarea><span class="ajuda">Fluido ou gás tratado, vazão, pressão, temperatura e volume do leito ajudam a indicar o produto certo.</span></div>
 </div>
 <div class="botoes">
  <button type="submit" class="btn btn-wa"><svg><use href="#i-wa"/></svg>Enviar pelo WhatsApp</button>
  <button type="button" class="btn btn-contorno" data-enviar="email"><svg><use href="#i-mail"/></svg>Enviar por e-mail</button>
 </div>
 <p class="status-form" role="status"></p>
 <p class="privacidade">Os dados não ficam gravados neste site: eles só montam a mensagem no seu WhatsApp ou e-mail, e você decide se envia. <a href="politica-de-privacidade.html">Política de privacidade</a>.</p>
</form>"""


ORG_JSONLD = f"""{{"@context":"https://schema.org","@type":"Organization","@id":"{SITE}/#organizacao","name":"Ita-Bio Soluções Ltda.","alternateName":["Petraquim","ITA-BIO"],"url":"{SITE}/","logo":"{SITE}/assets/img/logo-itabio.png","email":"{EMAIL}","telephone":"+55-11-2267-3311","taxID":"14.392.945/0001-00","address":{{"@type":"PostalAddress","streetAddress":"Av. Paulista, 2073 — Bela Vista","postalCode":"01311-010","addressLocality":"São Paulo","addressRegion":"SP","addressCountry":"BR"}},"contactPoint":[{{"@type":"ContactPoint","contactType":"sales","telephone":"+55-11-98776-9550","email":"{EMAIL}","areaServed":"BR","availableLanguage":["pt-BR"]}}],"sameAs":["{INSTAGRAM}"]}}"""


def ld(*blocos):
    return "".join(f'<script type="application/ld+json">{b}</script>\n' for b in blocos)

# -*- coding: utf-8 -*-
"""Gera as páginas HTML do site a partir das partes comuns.
Uso (na pasta do site):  python _fonte/gerar.py"""
import os, sys, datetime
from urllib.parse import quote
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from partes import *  # noqa

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
HOJE = datetime.date.today().isoformat()


def salvar(nome, html):
    with open(os.path.join(RAIZ, nome), "w", encoding="utf-8", newline="\n") as f:
        f.write(html)
    print("ok", nome, len(html) // 1024, "KB")


# ---------------------------------------------------------------- componentes
def selos():
    return """<ul class="selos">
    <li><svg><use href="#i-check"/></svg>Produto importado</li>
    <li><svg><use href="#i-check"/></svg>Novo, em embalagem original</li>
    <li><svg><use href="#i-check"/></svg>De 1 kg a 1.000 kg</li>
    <li><svg><use href="#i-check"/></svg>Envio para todo o Brasil</li>
   </ul>"""


APPS = [
    ("ar-comprimido", "app-ar-comprimido", "Secagem de ar comprimido", "Secadores por adsorção, filtros de linha e cartuchos: reduz o ponto de orvalho e protege ferramentas, válvulas e instrumentos.", "Regulador e manômetro em linha de ar comprimido"),
    ("gases", "app-gases", "Secagem de gases de processo", "Gás natural, GLP, nitrogênio, CO₂, hidrogênio e ar de instrumentação. Boa resistência química em correntes ácidas.", "Planta petroquímica iluminada à noite"),
    ("liquidos", "app-liquidos", "Desidratação de líquidos", "Solventes orgânicos, hidrocarbonetos líquidos e correntes de processo em que a água compromete a reação ou o produto.", "Tubulações de aço inox em uma planta de processo"),
    ("guarda", "app-guarda", "Leito de guarda", "Camada de proteção antes de catalisadores e adsorventes mais caros: retém água e arraste de líquidos.", "Tanques industriais de armazenamento"),
    ("oleos", "app-oleos", "Óleos e fluidos isolantes", "Remoção de umidade e de compostos ácidos de óleos de transformadores, lubrificantes e fluidos refrigerantes.", "Equipamentos elétricos industriais"),
    ("laboratorio", "app-laboratorio", "Laboratório e sistemas piloto", "Colunas de secagem, ensaios em bancada e unidades piloto, a partir de 1 kg.", "Mão com luva segurando béquer em laboratório"),
]


def cartoes_apps(link=True):
    out = []
    for ancora, img, tit, txt, alt in APPS:
        tag = "a" if link else "div"
        href = f' href="aplicacoes.html#{ancora}"' if link else ""
        mais = '<span class="mais">Saiba mais<svg><use href="#i-seta"/></svg></span>' if link else ""
        out.append(f"""<{tag} class="app rv"{href}>
    <div class="foto">{pic(img, alt, "(max-width:640px) 100vw, (max-width:980px) 50vw, 380px")}</div>
    <div class="corpo"><h3>{tit}</h3><p>{txt}</p>{mais}</div>
   </{tag}>""")
    return "\n   ".join(out)


def tabela_espec(com_caption=True):
    cap = '<caption>Dados comerciais do produto em estoque. Valores técnicos de referência estão na <a href="alumina-ativada.html#referencia">ficha técnica</a>.</caption>' if com_caption else ""
    return f"""<table class="tabela">
    {cap}
    <tbody>
     <tr><th scope="row">Produto</th><td>Alumina ativada (óxido de alumínio, Al₂O₃)</td></tr>
     <tr><th scope="row">Origem</th><td>Importado</td></tr>
     <tr><th scope="row">Condição</th><td>Novo, em embalagem original</td></tr>
     <tr><th scope="row">Forma</th><td>Grânulos esféricos brancos</td></tr>
     <tr><th scope="row">Granulometrias</th><td>7 x 14 mesh (≈ 1,2 a 2,8 mm)<br>2,0 a 3,0 mm</td></tr>
     <tr><th scope="row">Função</th><td>Secagem (dessecante) e adsorção</td></tr>
     <tr><th scope="row">Embalagens</th><td><div class="chips"><span>1 kg</span><span>5 kg</span><span>25 kg</span><span>50 kg</span><span>200 kg</span><span>1.000 kg</span></div></td></tr>
     <tr><th scope="row">Segurança</th><td>Não classificado como perigoso (ABNT NBR 14725). Não classificado como perigoso para transporte.</td></tr>
     <tr><th scope="row">Documentação</th><td>Ficha com Dados de Segurança (FDS) — ABNT NBR 14725</td></tr>
    </tbody>
   </table>"""


def cartao_fds():
    return f"""<aside class="cartao-doc rv" aria-labelledby="fds-titulo">
    <div class="icone-doc"><svg><use href="#i-doc"/></svg></div>
    <h3 id="fds-titulo">Ficha com Dados de Segurança</h3>
    <p>Identificação, manuseio, armazenamento, transporte e medidas de emergência, conforme a ABNT NBR 14725.</p>
    <a class="btn btn-ouro" href="{FDS}" download data-conv="fds"><svg><use href="#i-baixar"/></svg>Baixar FDS (PDF)</a>
    <small>PDF · 195 KB · em português</small>
   </aside>"""


FAQ = [
    ("O que é alumina ativada?",
     "É óxido de alumínio (Al₂O₃) altamente poroso, produzido pela desidratação controlada do hidróxido de alumínio. Os poros têm enorme área interna e retêm moléculas de água e outros compostos polares por adsorção física, por isso o material funciona como dessecante e adsorvente."),
    ("Qual granulometria devo escolher: 7 x 14 mesh ou 2,0 a 3,0 mm?",
     "Grãos menores (7 x 14 mesh) secam mais rápido e são indicados para líquidos, colunas e leitos compactos, mas geram mais perda de carga. A faixa de 2,0 a 3,0 mm é um pouco maior e equilibra cinética e perda de carga em secadores compactos de ar e gases. Se o seu equipamento já usa alumina, repita a granulometria do fabricante. Na dúvida, envie os dados do equipamento que indicamos a opção adequada."),
    ("A alumina ativada pode ser reutilizada?",
     "Sim. Como a adsorção é física e reversível, o material saturado pode ser regenerado por aquecimento (tipicamente entre 180 °C e 250 °C em secadores de ar) ou por variação de pressão em secadores sem aquecimento. Evite passar de 320 °C, que reduz de forma permanente a capacidade."),
    ("Quanto de alumina eu preciso?",
     "Depende da quantidade de água a remover por ciclo, que vem da vazão, da pressão, da temperatura de entrada e do tempo entre regenerações. A nossa calculadora dá uma estimativa inicial; para projeto, consulte o fabricante do equipamento ou um profissional habilitado."),
    ("Qual é a quantidade mínima de compra?",
     "1 kg. Pequenas quantidades podem ser compradas direto no Mercado Livre, com nota fiscal. Para 5 kg ou mais, peça uma cotação: atendemos de 5 kg a 1.000 kg, inclusive fornecimento recorrente."),
    ("Vocês enviam para todo o Brasil?",
     "Sim. Informe a cidade e o estado de entrega na cotação para recebermos o frete e o prazo corretos para o seu endereço."),
    ("O produto é perigoso? Precisa de transporte especial?",
     "Não. Conforme a FDS do produto (ABNT NBR 14725), a alumina ativada não é classificada como perigosa nem como perigosa para transporte. A poeira pode irritar olhos e vias respiratórias: use óculos, luvas e máscara PFF2 ao carregar o leito."),
    ("Serve para tratamento de água potável?",
     "Não ofertamos este grau para água de consumo humano. Alumina para água potável exige grau específico com certificação própria (como NSF/ANSI 61). O produto deste site é de grau industrial para secagem e adsorção."),
    ("Como armazenar depois de aberto?",
     "A alumina ativada começa a adsorver a umidade do ar assim que a embalagem é aberta. Use todo o conteúdo de uma vez ou feche imediatamente em recipiente hermético, em local seco e coberto."),
]


def faq_html(qtd=None):
    itens = FAQ if qtd is None else FAQ[:qtd]
    return "\n".join(f"""  <details><summary>{p}</summary><div class="resposta"><p>{r}</p></div></details>""" for p, r in itens)


def faq_jsonld():
    import json
    return json.dumps({"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [
        {"@type": "Question", "name": p, "acceptedAnswer": {"@type": "Answer", "text": r}} for p, r in FAQ]}, ensure_ascii=False)


# ---------------------------------------------------------------- INÍCIO
def pagina_inicio():
    pre = f'<link rel="preload" as="image" type="image/webp" imagesrcset="assets/img/alumina-copo-640.webp 640w, assets/img/alumina-copo-1000.webp 1000w, assets/img/alumina-copo-1400.webp 1400w" imagesizes="(max-width:980px) 92vw, 520px">\n'
    website = f'{{"@context":"https://schema.org","@type":"WebSite","name":"Petraquim · Ita-Bio Soluções","url":"{SITE}/","inLanguage":"pt-BR","publisher":{{"@id":"{SITE}/#organizacao"}}}}'
    h = cabeca("Alumina Ativada — dessecante industrial | Petraquim · Ita-Bio",
               "Alumina ativada importada, nova, em embalagem original: 7 x 14 mesh e 2,0 a 3,0 mm, de 1 kg a 1.000 kg. Secagem de ar comprimido, gases e líquidos.",
               "", jsonld=ld(ORG_JSONLD, website), preload=pre)
    h += topo("index.html")
    h += f"""
<section class="hero" aria-labelledby="hero-titulo">
 <div class="wrap">
  <div>
   <span class="rotulo">Adsorvente industrial · Material em estoque</span>
   <h1 id="hero-titulo">Alumina Ativada para <em>secagem e adsorção</em></h1>
   <p class="sub">Dessecante em esferas para ar comprimido, gases e líquidos. Importada, nova, em embalagem original, com atendimento técnico-comercial direto.</p>
   {selos()}
   <div class="botoes">
    <a class="btn btn-wa" href="{WA_LINK}" target="_blank" rel="noopener" data-conv="whatsapp"><svg><use href="#i-wa"/></svg>Pedir cotação pelo WhatsApp</a>
    <a class="btn btn-contorno" href="#cotacao">Montar minha cotação</a>
   </div>
   <p class="apoio">Precisa de só 1 kg? <a href="{ML_LINK}" target="_blank" rel="noopener" data-conv="mercadolivre">Compre no Mercado Livre</a>, com nota fiscal.</p>
  </div>
  <div class="hero-midia">
   <div class="moldura" aria-hidden="true"></div>
   <div class="quadro">
    {pic("alumina-copo", "Alumina ativada em grânulos esféricos brancos dentro de um copo transparente", "(max-width:980px) 92vw, 520px", ansioso=True)}
    <span class="selo-real"><svg><use href="#i-check"/></svg>Foto real do produto</span>
   </div>
   <div class="ficha-flutuante"><b>Granulometrias</b><span>7 x 14 mesh · 2,0 a 3,0 mm</span></div>
  </div>
 </div>
</section>

<section class="faixa-dados" aria-label="Resumo do produto">
 <div class="wrap">
  <div class="dado"><strong>Al₂O₃</strong><span>Óxido de alumínio ativado, em esferas</span></div>
  <div class="dado"><strong>2 faixas</strong><span>7 x 14 mesh e 2,0 a 3,0 mm</span></div>
  <div class="dado"><strong>1 kg a 1 t</strong><span>6 opções de embalagem</span></div>
  <div class="dado"><strong>FDS</strong><span>Conforme ABNT NBR 14725</span></div>
 </div>
</section>

<section class="secao" id="aplicacoes" aria-labelledby="apps-titulo">
 <div class="wrap">
  <div class="cabecalho-secao rv">
   <span class="rotulo">Aplicações</span>
   <h2 id="apps-titulo">Onde a alumina ativada trabalha</h2>
   <p>Indicada para processos que precisam remover umidade ou reter compostos polares, do secador de ar da oficina à planta de processo.</p>
  </div>
  <div class="grade-apps">
   {cartoes_apps()}
  </div>
  <div class="nota rv"><svg><use href="#i-ciclo"/></svg><p><strong>Regenerável.</strong> Depois de saturada, a alumina ativada pode ser regenerada por aquecimento e voltar ao serviço, o que reduz o custo por ciclo.</p></div>
 </div>
</section>

<section class="secao secao-creme" id="produto" aria-labelledby="perto-titulo">
 <div class="wrap">
  <div class="cabecalho-secao rv">
   <span class="rotulo">O produto de perto</span>
   <h2 id="perto-titulo">Imagens reais do material em estoque</h2>
   <p>Esferas brancas e uniformes, sem pó, na embalagem original. Clique nas fotos para ampliar.</p>
  </div>
  <div class="galeria rv">
   <figure class="alto" data-video>
    <video src="assets/video/alumina-apresentacao.mp4" poster="{maior('alumina-video-capa')}" autoplay muted loop playsinline preload="metadata" aria-label="Vídeo dos grânulos de alumina ativada"></video>
    <button class="video-ctrl" type="button" aria-label="Pausar vídeo"></button>
    <figcaption>Grânulos esféricos de alumina ativada</figcaption>
   </figure>
   <figure>{pic("alumina-regua-1", "Grânulos de alumina ativada ao lado de uma régua em centímetros", "(max-width:640px) 100vw, 380px")}<button class="amplia" type="button" data-amplia="{maior('alumina-regua-1')}" data-legenda="Grânulos ao lado de régua (escala em centímetros)" aria-label="Ampliar: grânulos ao lado de régua"></button><figcaption>Ao lado da régua (cm)</figcaption></figure>
   <figure>{pic("alumina-tigela", "Porção de alumina ativada vista de cima", "(max-width:640px) 100vw, 380px")}<button class="amplia" type="button" data-amplia="{maior('alumina-tigela')}" data-legenda="Porção de alumina ativada vista de cima" aria-label="Ampliar: porção vista de cima"></button><figcaption>Esferas uniformes</figcaption></figure>
   <figure>{pic("alumina-embalagem", "Alumina ativada em embalagem plástica lacrada", "(max-width:640px) 100vw, 380px")}<button class="amplia" type="button" data-amplia="{maior('alumina-embalagem')}" data-legenda="Embalagem original lacrada" aria-label="Ampliar: embalagem original"></button><figcaption>Embalagem original lacrada</figcaption></figure>
   <figure>{pic("alumina-regua-2", "Grânulos de alumina ativada com régua, outro ângulo", "(max-width:640px) 100vw, 380px")}<button class="amplia" type="button" data-amplia="{maior('alumina-regua-2')}" data-legenda="Outro ângulo, com régua para referência de tamanho" aria-label="Ampliar: outro ângulo com régua"></button><figcaption>Referência de tamanho</figcaption></figure>
  </div>
 </div>
</section>

<section class="secao" id="especificacao" aria-labelledby="espec-titulo">
 <div class="wrap">
  <div class="cabecalho-secao rv">
   <span class="rotulo">Especificação</span>
   <h2 id="espec-titulo">O que você recebe</h2>
  </div>
  <div class="espec-grid">
   <div class="rv">
   {tabela_espec()}
   <p style="margin-top:22px"><a class="link-seta" href="alumina-ativada.html">Ver a ficha técnica completa<svg><use href="#i-seta"/></svg></a></p>
   </div>
   {cartao_fds()}
  </div>
 </div>
</section>

<section class="secao secao-creme" id="comprar" aria-labelledby="comprar-titulo">
 <div class="wrap">
  <div class="cabecalho-secao centro rv">
   <span class="rotulo">Como comprar</span>
   <h2 id="comprar-titulo">Do teste de bancada ao leito industrial</h2>
   <p>Escolha o caminho que combina com a sua quantidade.</p>
  </div>
  <div class="canais">
   <div class="canal rv">
    <span class="faixa">1 kg</span>
    <h3>Mercado Livre</h3>
    <p>Para reposição pontual, testes e laboratório.</p>
    <ul>
     <li><svg><use href="#i-check"/></svg>Compra imediata, com nota fiscal</li>
     <li><svg><use href="#i-check"/></svg>Pagamento e entrega pela plataforma</li>
    </ul>
    <a class="btn btn-ml" href="{ML_LINK}" target="_blank" rel="noopener" data-conv="mercadolivre"><svg><use href="#i-carrinho"/></svg>Comprar 1 kg</a>
   </div>
   <div class="canal destaque rv">
    <span class="faixa">5 kg a 200 kg</span>
    <h3>Cotação direta</h3>
    <p>Para secadores, filtros e trocas programadas de leito.</p>
    <ul>
     <li><svg><use href="#i-check"/></svg>Indicação da granulometria certa</li>
     <li><svg><use href="#i-check"/></svg>Frete calculado para a sua cidade</li>
     <li><svg><use href="#i-check"/></svg>FDS enviada junto com a proposta</li>
    </ul>
    <a class="btn btn-wa" href="{WA_LINK}" target="_blank" rel="noopener" data-conv="whatsapp"><svg><use href="#i-wa"/></svg>Pedir cotação</a>
   </div>
   <div class="canal rv">
    <span class="faixa">1.000 kg ou recorrente</span>
    <h3>Volumes industriais</h3>
    <p>Para plantas de processo e contratos de fornecimento.</p>
    <ul>
     <li><svg><use href="#i-check"/></svg>Embalagens de até 1.000 kg</li>
     <li><svg><use href="#i-check"/></svg>Programação de entregas</li>
     <li><svg><use href="#i-check"/></svg>Proposta comercial formal</li>
    </ul>
    <a class="btn btn-primario" href="cotacao.html">Solicitar proposta</a>
   </div>
  </div>
 </div>
</section>

<section class="banda-foto" aria-labelledby="banda-titulo">
 {pic("ind-tubulacao", "", "100vw")}
 <div class="wrap">
  <span class="rotulo claro">Atendimento técnico-comercial</span>
  <h2 id="banda-titulo">Você fala direto com quem decide</h2>
  <p>Sem central de atendimento: a sua consulta vai para o gerente de vendas, que conhece o produto e responde com a recomendação e as condições comerciais.</p>
  <ol class="passos" style="margin-top:40px">
   <li><h3>Envie os dados</h3><p>Quantidade, aplicação e cidade de entrega, pelo WhatsApp ou e-mail.</p></li>
   <li><h3>Receba a orientação</h3><p>Indicamos granulometria e embalagem para o seu equipamento.</p></li>
   <li><h3>Aprove a proposta</h3><p>Preço, frete e prazo por escrito, com a FDS do produto.</p></li>
   <li><h3>Receba com nota</h3><p>Faturamento com nota fiscal e envio para todo o Brasil.</p></li>
  </ol>
 </div>
</section>

<section class="secao" id="cotacao" aria-labelledby="formulario-titulo">
 <div class="wrap cotacao-grid">
  <div class="rv">
   <span class="rotulo">Cotação</span>
   <h2>Para cotar mais rápido, informe</h2>
   <ul class="lista-check">
    <li><svg><use href="#i-check"/></svg>Quantidade e embalagem desejadas</li>
    <li><svg><use href="#i-check"/></svg>Granulometria (7 x 14 mesh ou 2,0 a 3,0 mm)</li>
    <li><svg><use href="#i-check"/></svg>Aplicação: fluido ou gás a ser tratado</li>
    <li><svg><use href="#i-check"/></svg>Vazão, pressão e temperatura de operação</li>
    <li><svg><use href="#i-check"/></svg>Volume do leito e consumo mensal</li>
    <li><svg><use href="#i-check"/></svg>Cidade e estado de entrega</li>
   </ul>
   <div class="responsavel">
    <div class="mono">{MONOGRAMA}</div>
    <div><strong>José Roberto Rocha</strong><span>Gerente de Vendas · Ita-Bio Soluções</span></div>
   </div>
   <p>Não sabe quanto precisa? Use a <a href="alumina-ativada.html#calculadora">calculadora de leito</a> para ter uma estimativa.</p>
  </div>
  {formulario()}
 </div>
</section>

<section class="secao secao-creme" aria-labelledby="faq-titulo">
 <div class="wrap wrap-estreito">
  <div class="cabecalho-secao centro rv">
   <span class="rotulo">Dúvidas frequentes</span>
   <h2 id="faq-titulo">Perguntas sobre alumina ativada</h2>
  </div>
  <div class="faq rv">
{faq_html(5)}
  </div>
  <p style="text-align:center;margin-top:28px"><a class="link-seta" href="alumina-ativada.html#perguntas">Ver todas as perguntas<svg><use href="#i-seta"/></svg></a></p>
 </div>
</section>
"""
    h += cta_final()
    h += rodape(lightbox=True)
    salvar("index.html", h)


# ---------------------------------------------------------------- ALUMINA ATIVADA (ficha técnica)
def pagina_produto():
    mig, mig_ld = migalhas([("Início", "index.html"), ("Alumina Ativada", None)])
    produto = f'{{"@context":"https://schema.org","@type":"Product","name":"Alumina Ativada","description":"Alumina ativada (óxido de alumínio, Al₂O₃) em grânulos esféricos brancos, importada, nova, em embalagem original. Dessecante e adsorvente para secagem de ar comprimido, gases e líquidos. Granulometrias 7 x 14 mesh e 2,0 a 3,0 mm; embalagens de 1 kg a 1.000 kg.","image":["{SITE}/{maior("alumina-copo")}","{SITE}/{maior("alumina-embalagem")}","{SITE}/{maior("alumina-regua-1")}"],"category":"Adsorventes e dessecantes industriais","material":"Óxido de alumínio (Al₂O₃)","brand":{{"@type":"Brand","name":"Petraquim · Ita-Bio Soluções"}},"manufacturer":{{"@id":"{SITE}/#organizacao"}},"additionalProperty":[{{"@type":"PropertyValue","name":"Granulometria","value":"7 x 14 mesh (≈ 1,2 a 2,8 mm); 2,0 a 3,0 mm"}},{{"@type":"PropertyValue","name":"Embalagens","value":"1 kg, 5 kg, 25 kg, 50 kg, 200 kg, 1.000 kg"}},{{"@type":"PropertyValue","name":"Forma","value":"Grânulos esféricos brancos"}}]}}'
    h = cabeca("Alumina Ativada: ficha técnica, granulometria e regeneração | Petraquim",
               "Ficha técnica da alumina ativada: como funciona, granulometrias 7 x 14 mesh e 2,0 a 3,0 mm, valores de referência, regeneração, calculadora de leito, segurança e FDS.",
               "alumina-ativada.html", jsonld=ld(ORG_JSONLD, produto, mig_ld, faq_jsonld()))
    h += topo("alumina-ativada.html")
    h += f"""
<header class="pagina-topo">
 {pic("alumina-textura", "", "100vw", ansioso=True)}
 <div class="wrap">
  {mig}
  <span class="rotulo claro">Ficha técnica</span>
  <h1>Alumina Ativada</h1>
  <p>Tudo o que você precisa para especificar, dimensionar e operar um leito de alumina ativada, com as granulometrias e embalagens que temos em estoque.</p>
 </div>
</header>

<div class="secao">
 <div class="wrap com-indice">
  <nav class="indice" aria-label="Nesta página">
   <p>Nesta página</p>
   <ol>
    <li><a href="#o-que-e">O que é</a></li>
    <li><a href="#como-funciona">Como funciona</a></li>
    <li><a href="#granulometria">Granulometria</a></li>
    <li><a href="#especificacao">Especificação</a></li>
    <li><a href="#referencia">Valores de referência</a></li>
    <li><a href="#regeneracao">Regeneração</a></li>
    <li><a href="#calculadora">Calculadora de leito</a></li>
    <li><a href="#boas-praticas">Boas práticas</a></li>
    <li><a href="#seguranca">Segurança e FDS</a></li>
    <li><a href="#perguntas">Perguntas frequentes</a></li>
   </ol>
  </nav>

  <article class="artigo">
   <section id="o-que-e" aria-labelledby="t-oque">
    <span class="rotulo">01 · Definição</span>
    <h2 id="t-oque">O que é alumina ativada</h2>
    <div class="dividido" style="gap:40px;align-items:start">
     <div>
      <p>A alumina ativada é um <strong>óxido de alumínio (Al₂O₃)</strong> obtido pela desidratação controlada do hidróxido de alumínio. O processo retira água da estrutura cristalina sem colapsá-la e deixa um sólido com porosidade muito alta, formado principalmente pela fase gama (γ-Al₂O₃), que tem a superfície ativa.</p>
      <p>Na prática, cada grama do material tem centenas de metros quadrados de superfície interna. É ali que a água e outros compostos polares ficam retidos.</p>
      <ul class="lista-check">
       <li><svg><use href="#i-check"/></svg>Não amolece, não incha e não se desfaz em contato com líquidos.</li>
       <li><svg><use href="#i-check"/></svg>Inerte, inodora, branca a esbranquiçada.</li>
       <li><svg><use href="#i-check"/></svg>Regenerável por calor ou por variação de pressão.</li>
      </ul>
     </div>
     <div class="lado-midia">{pic("alumina-detalhe", "Close dos grânulos esféricos de alumina ativada", "(max-width:980px) 92vw, 420px")}<p class="credito">Foto real do produto em estoque.</p></div>
    </div>
   </section>

   <section id="como-funciona" aria-labelledby="t-func">
    <span class="rotulo">02 · Princípio</span>
    <h2 id="t-func">Como funciona: adsorção física e reversível</h2>
    <p>O gás ou líquido úmido atravessa o leito de esferas. As moléculas de água, fortemente polares, aderem à superfície dos poros e ficam retidas; o fluido sai seco. Quando o leito satura, a regeneração libera a água e o material volta a trabalhar.</p>
    <figure class="diagrama">
     <svg viewBox="0 0 760 330" role="img" aria-labelledby="dg-t dg-d">
      <title id="dg-t">Esquema de um leito de alumina ativada</title>
      <desc id="dg-d">O fluido úmido entra pelo topo do vaso, desce pelo leito de esferas, onde a frente de adsorção avança, e sai seco pela base. Na regeneração, gás seco e quente passa em sentido contrário, de baixo para cima.</desc>
      <defs><marker id="pt" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M0 0L10 5L0 10z" fill="#4B5320"/></marker><marker id="pt2" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M0 0L10 5L0 10z" fill="#9C7E35"/></marker><pattern id="esf" width="14" height="14" patternUnits="userSpaceOnUse"><circle cx="7" cy="7" r="5.2" fill="#fff" stroke="#CFC9B4" stroke-width="1"/></pattern><pattern id="esf2" width="14" height="14" patternUnits="userSpaceOnUse"><rect width="14" height="14" fill="#DCE6EF"/><circle cx="7" cy="7" r="5.2" fill="#EAF1F7" stroke="#A9BDCF" stroke-width="1"/></pattern></defs>
      <rect x="290" y="40" width="180" height="250" rx="26" fill="#fff" stroke="#4B5320" stroke-width="3"/>
      <rect x="302" y="78" width="156" height="72" fill="url(#esf2)"/>
      <rect x="302" y="150" width="156" height="104" fill="url(#esf)"/>
      <line x1="302" y1="150" x2="458" y2="150" stroke="#C5A253" stroke-width="3" stroke-dasharray="6 4"/>
      <text x="380" y="30" text-anchor="middle" font-family="Lato,Arial,sans-serif" font-size="14" font-weight="700" fill="#2F3514">VASO ADSORVEDOR</text>
      <path d="M150 60 H350 V74" fill="none" stroke="#4B5320" stroke-width="3" marker-end="url(#pt)"/>
      <text x="40" y="52" font-family="Lato,Arial,sans-serif" font-size="15" font-weight="700" fill="#2F3514">Entrada: fluido úmido</text>
      <text x="40" y="72" font-family="Lato,Arial,sans-serif" font-size="13" fill="#5E5F52">ar, gás ou líquido</text>
      <path d="M410 290 V312 H592" fill="none" stroke="#4B5320" stroke-width="3" marker-end="url(#pt)"/>
      <text x="602" y="317" font-family="Lato,Arial,sans-serif" font-size="15" font-weight="700" fill="#2F3514">Saída: fluido seco</text>
      <text x="490" y="112" font-family="Lato,Arial,sans-serif" font-size="13" fill="#5E5F52">zona saturada</text>
      <text x="490" y="155" font-family="Lato,Arial,sans-serif" font-size="13" font-weight="700" fill="#9C7E35">frente de adsorção ↓</text>
      <text x="490" y="205" font-family="Lato,Arial,sans-serif" font-size="13" fill="#5E5F52">alumina ainda ativa</text>
      <path d="M232 250 V110" fill="none" stroke="#9C7E35" stroke-width="2.5" stroke-dasharray="7 5" marker-end="url(#pt2)"/>
      <text x="222" y="200" font-family="Lato,Arial,sans-serif" font-size="13" fill="#9C7E35" text-anchor="end">Regeneração:</text>
      <text x="222" y="218" font-family="Lato,Arial,sans-serif" font-size="13" fill="#9C7E35" text-anchor="end">gás seco em</text>
      <text x="222" y="236" font-family="Lato,Arial,sans-serif" font-size="13" fill="#9C7E35" text-anchor="end">contracorrente</text>
     </svg>
     <figcaption>Na adsorção o fluxo é descendente; na regeneração, ascendente (contracorrente), para não arrastar umidade até a saída do leito.</figcaption>
    </figure>
   </section>

   <section id="granulometria" aria-labelledby="t-gran">
    <span class="rotulo">03 · Granulometria</span>
    <h2 id="t-gran">7 x 14 mesh ou 2,0 a 3,0 mm?</h2>
    <p>“7 x 14 mesh” significa que o grão passa na peneira de 7 mesh e fica retido na de 14 mesh. O tamanho do grão define o equilíbrio entre <strong>velocidade de adsorção</strong> e <strong>perda de carga</strong>: grãos menores secam mais rápido, mas oferecem mais resistência ao fluxo.</p>
    <div class="rolagem-tabela">
    <table class="tabela listrada">
     <thead><tr><th scope="col">Peneira</th><th scope="col">Série Tyler</th><th scope="col">Série ASTM/US</th></tr></thead>
     <tbody>
      <tr><th scope="row">7 mesh (passa)</th><td class="num">2,79 mm</td><td class="num">2,80 mm</td></tr>
      <tr><th scope="row">14 mesh (retém)</th><td class="num">1,17 mm</td><td class="num">1,40 mm</td></tr>
      <tr><th scope="row">Faixa 7 x 14</th><td class="num">≈ 1,2 a 2,8 mm</td><td class="num">≈ 1,4 a 2,8 mm</td></tr>
     </tbody>
    </table>
    </div>
    <h3>Qual escolher</h3>
    <div class="rolagem-tabela">
    <table class="tabela listrada">
     <thead><tr><th scope="col">Granulometria</th><th scope="col">Cinética</th><th scope="col">Perda de carga</th><th scope="col">Uso preferencial</th></tr></thead>
     <tbody>
      <tr><th scope="row">7 x 14 mesh</th><td>Mais rápida</td><td>Maior</td><td>Desidratação de líquidos, colunas, cartuchos, leitos compactos e laboratório</td></tr>
      <tr><th scope="row">2,0 a 3,0 mm</th><td>Rápida</td><td>Moderada</td><td>Secadores compactos de ar e gases, filtros de linha e reposição de leitos que usam esferas de ~2 a 3 mm</td></tr>
     </tbody>
    </table>
    </div>
    <div class="nota"><svg><use href="#i-info"/></svg><p>Vai repor um leito existente? Repita a granulometria indicada pelo fabricante do secador. Grandes leitos de fase vapor costumam usar esferas maiores (3 a 6 mm), que não fazem parte do nosso estoque atual. <a href="cotacao.html">Consulte-nos</a>.</p></div>
   </section>

   <section id="especificacao" aria-labelledby="t-espec">
    <span class="rotulo">04 · Especificação comercial</span>
    <h2 id="t-espec">Especificação do produto em estoque</h2>
    <div class="espec-grid" style="grid-template-columns:1fr">
     {tabela_espec(com_caption=False)}
    </div>
    <div class="botoes" style="margin-top:22px">
     <a class="btn btn-primario" href="{FDS}" download data-conv="fds"><svg><use href="#i-baixar"/></svg>Baixar FDS (PDF)</a>
     <a class="btn btn-contorno" href="cotacao.html">Pedir cotação</a>
    </div>
   </section>

   <section id="referencia" aria-labelledby="t-ref">
    <span class="rotulo">05 · Referência técnica</span>
    <h2 id="t-ref">Valores típicos da classe (grau de secagem, 7 x 14 mesh)</h2>
    <p>Faixas características de aluminas ativadas de grau de secagem, compiladas de fichas técnicas públicas de produtos equivalentes. Servem para pré-dimensionamento e comparação.</p>
    <div class="rolagem-tabela">
    <table class="tabela listrada">
     <thead><tr><th scope="col">Propriedade</th><th scope="col">Faixa típica</th><th scope="col">Para que serve</th></tr></thead>
     <tbody>
      <tr><th scope="row">Área superficial (BET)</th><td class="num">325 a 360 m²/g</td><td>Indica a capacidade máxima de adsorção</td></tr>
      <tr><th scope="row">Volume de poros</th><td class="num">0,45 a 0,50 cm³/g</td><td>Espaço disponível para reter a água</td></tr>
      <tr><th scope="row">Densidade aparente compactada</th><td class="num">0,70 a 0,80 g/cm³</td><td>Converte massa em volume de leito</td></tr>
      <tr><th scope="row">Resistência ao esmagamento</th><td class="num">≈ 5 kgf por esfera</td><td>Suporta o peso do leito e a ciclagem</td></tr>
      <tr><th scope="row">Perda por abrasão</th><td class="num">≤ 0,1 %</td><td>Indica a geração de pó (finos)</td></tr>
      <tr><th scope="row">Al₂O₃</th><td class="num">92 a 94 %</td><td>Constituinte principal</td></tr>
      <tr><th scope="row">Capacidade estática de água</th><td class="num">20 a 22 % (25 °C, 60 % UR)</td><td>Valor de catálogo, para comparar produtos</td></tr>
      <tr><th scope="row">Capacidade dinâmica de trabalho</th><td class="num">10 a 15 %</td><td>Valor a usar no dimensionamento</td></tr>
      <tr><th scope="row">Ponto de orvalho atingível</th><td class="num">−40 °C a −70 °C</td><td>Depende de pressão, ciclo, purga e regeneração</td></tr>
     </tbody>
    </table>
    </div>
    <div class="nota alerta"><svg><use href="#i-alerta"/></svg><p><strong>Valores de referência, não especificação do lote.</strong> Para projeto ou proposta técnica formal, solicite o certificado de análise do lote junto com a cotação.</p></div>
   </section>

   <section id="regeneracao" aria-labelledby="t-reg">
    <span class="rotulo">06 · Regeneração</span>
    <h2 id="t-reg">Regeneração e ciclos de operação</h2>
    <p>Como a adsorção é física, o leito saturado pode ser regenerado muitas vezes. Há dois métodos usuais:</p>
    <div class="valores duas" style="margin:22px 0">
     <div class="valor-item"><div class="ic"><svg><use href="#i-chama"/></svg></div><h3>Por temperatura (TSA)</h3><p>Aquecimento do leito, tipicamente entre 180 °C e 250 °C em secadores de ar, com purga de gás seco em contracorrente e resfriamento antes de voltar ao serviço.</p></div>
     <div class="valor-item"><div class="ic"><svg><use href="#i-medidor"/></svg></div><h3>Por pressão (PSA)</h3><p>Usado em secadores sem aquecimento (<i>heatless</i>): o leito é despressurizado e purgado com parte do ar já seco, em geral 10 % a 20 % da vazão tratada.</p></div>
    </div>
    <div class="rolagem-tabela">
    <table class="tabela listrada">
     <thead><tr><th scope="col">Etapa (TSA)</th><th scope="col">Condição típica</th><th scope="col">Cuidado</th></tr></thead>
     <tbody>
      <tr><th scope="row">Despressurização</th><td>Gradual</td><td>Despressurização brusca causa atrito e gera pó</td></tr>
      <tr><th scope="row">Aquecimento</th><td class="num">180 a 250 °C</td><td>Acima de 320 °C há perda permanente de área superficial</td></tr>
      <tr><th scope="row">Patamar</th><td class="num">2 a 4 h, conforme a carga</td><td>Patamar curto deixa capacidade residual baixa</td></tr>
      <tr><th scope="row">Purga</th><td>Gás seco em contracorrente</td><td>Sem purga, a água volta a ser adsorvida</td></tr>
      <tr><th scope="row">Resfriamento</th><td>Até perto da temperatura de operação</td><td>Entrar em serviço quente reduz muito a capacidade</td></tr>
     </tbody>
    </table>
    </div>
   </section>

   <section id="calculadora" aria-labelledby="t-calc">
    <span class="rotulo">07 · Ferramenta</span>
    <h2 id="t-calc">Calculadora de leito para ar comprimido</h2>
    <p>Estime quanta alumina ativada um secador precisa para o tempo de ciclo desejado. A conta parte do ar saturado após o resfriador, adota capacidade dinâmica de 12 % e soma 20 % de margem para envelhecimento.</p>
    <div class="calc">
     <form id="calc-leito" novalidate aria-label="Dados do secador">
      <div class="campos">
       <div class="campo"><label for="c-vazao">Vazão de ar</label><div class="unid"><input id="c-vazao" name="vazao" inputmode="decimal" value="10"><span>Nm³/h</span></div></div>
       <div class="campo"><label for="c-pressao">Pressão de trabalho</label><div class="unid"><input id="c-pressao" name="pressao" inputmode="decimal" value="7"><span>bar</span></div></div>
       <div class="campo"><label for="c-temp">Temperatura na entrada</label><select id="c-temp" name="temperatura"><option value="20">20 °C</option><option value="25">25 °C</option><option value="30">30 °C</option><option value="35" selected>35 °C</option><option value="40">40 °C</option><option value="45">45 °C</option></select></div>
       <div class="campo"><label for="c-ciclo">Tempo entre regenerações</label><div class="unid"><input id="c-ciclo" name="ciclo" inputmode="decimal" value="3"><span>horas</span></div></div>
      </div>
      <p class="ajuda" style="font-size:13.5px;color:var(--cinza);margin:16px 0 0">Pressão manométrica. Considera ar saturado (100 % UR) na temperatura informada.</p>
     </form>
     <div class="resultado" id="calc-saida" aria-live="polite">
      <span class="rotulo">Massa estimada</span>
      <div class="valor" id="calc-kg">—</div>
      <p class="detalhe" id="calc-agua"></p>
      <p class="detalhe" id="calc-vol"></p>
      <p class="detalhe" id="calc-emb"></p>
      <a class="btn btn-ouro" id="calc-cotar" href="cotacao.html#formulario">Cotar esta quantidade</a>
      <p class="ressalva">Estimativa de ordem de grandeza. Não substitui o dimensionamento do fabricante do equipamento ou de profissional habilitado.</p>
     </div>
    </div>
   </section>

   <section id="boas-praticas" aria-labelledby="t-bp">
    <span class="rotulo">08 · Operação</span>
    <h2 id="t-bp">Boas práticas e causas de falha</h2>
    <div class="dividido" style="align-items:start;gap:40px">
     <div>
      <h3 style="margin-top:0">Na instalação</h3>
      <ul class="lista-check">
       <li><svg><use href="#i-check"/></svg>Mantenha a embalagem lacrada até o carregamento.</li>
       <li><svg><use href="#i-check"/></svg>Carregue devagar e de forma uniforme, sem queda livre alta.</li>
       <li><svg><use href="#i-check"/></svg>Use telas e esferas cerâmicas inertes na entrada e na saída, quando aplicável.</li>
       <li><svg><use href="#i-check"/></svg>Pressurize o leito de forma gradual na partida.</li>
       <li><svg><use href="#i-check"/></svg>Monitore ponto de orvalho e perda de carga.</li>
      </ul>
     </div>
     <div>
      <h3 style="margin-top:0">O que encurta a vida do leito</h3>
      <ul class="lista-check">
       <li><svg><use href="#i-alerta" style="color:#A2361F"/></svg><span><strong>Água líquida:</strong> libera calor e pode fragmentar as esferas. Use separador e drenos.</span></li>
       <li><svg><use href="#i-alerta" style="color:#A2361F"/></svg><span><strong>Óleo do compressor:</strong> bloqueia os poros de forma irreversível. Use filtro coalescente.</span></li>
       <li><svg><use href="#i-alerta" style="color:#A2361F"/></svg><span><strong>Regeneração acima de 320 °C:</strong> perda permanente de capacidade.</span></li>
       <li><svg><use href="#i-alerta" style="color:#A2361F"/></svg><span><strong>Ácidos ou bases fortes:</strong> atacam a estrutura e geram pó.</span></li>
       <li><svg><use href="#i-alerta" style="color:#A2361F"/></svg><span><strong>Fluxo ascendente rápido na adsorção:</strong> fluidiza o leito e gera finos.</span></li>
      </ul>
     </div>
    </div>
   </section>

   <section id="seguranca" aria-labelledby="t-seg">
    <span class="rotulo">09 · Segurança</span>
    <h2 id="t-seg">Segurança, manuseio e armazenamento</h2>
    <div class="espec-grid">
     <div>
      <p>Conforme a FDS do produto (ABNT NBR 14725), a alumina ativada <strong>não é classificada como perigosa</strong> nem como perigosa para transporte. O cuidado principal é com a poeira gerada no manuseio.</p>
      <ul class="lista-check">
       <li><svg><use href="#i-check"/></svg><span><strong>Proteção:</strong> óculos de segurança, luvas e máscara PFF2 ao carregar ou peneirar.</span></li>
       <li><svg><use href="#i-check"/></svg><span><strong>Material saturado e quente:</strong> use luvas térmicas; a adsorção de água libera calor.</span></li>
       <li><svg><use href="#i-check"/></svg><span><strong>Armazenagem:</strong> local seco, coberto e ventilado, com a embalagem lacrada.</span></li>
       <li><svg><use href="#i-check"/></svg><span><strong>Derramamento:</strong> recolha mecanicamente, sem ar comprimido, evitando levantar pó.</span></li>
       <li><svg><use href="#i-check"/></svg><span><strong>Descarte:</strong> caracterize o material usado conforme a ABNT NBR 10004, pois depende do que foi adsorvido.</span></li>
      </ul>
     </div>
     {cartao_fds()}
    </div>
   </section>

   <section id="perguntas" aria-labelledby="t-faq">
    <span class="rotulo">10 · Dúvidas</span>
    <h2 id="t-faq">Perguntas frequentes</h2>
    <div class="faq">
{faq_html()}
    </div>
   </section>
  </article>
 </div>
</div>
"""
    h += cta_final("Pronto para cotar?", "Envie quantidade, granulometria e cidade de entrega. Respondemos com preço, frete e prazo por escrito.")
    h += rodape()
    salvar("alumina-ativada.html", h)


# ---------------------------------------------------------------- APLICAÇÕES
DETALHES = {
    "ar-comprimido": ("Secagem de ar comprimido", "A aplicação mais comum. Depois do resfriador posterior, o ar continua saturado de umidade; o leito de alumina reduz o ponto de orvalho e evita corrosão, congelamento em expansões e contaminação do produto final.",
                      ["Secadores por adsorção com ou sem aquecimento (TSA e PSA)", "Filtros de linha e cartuchos dessecantes", "Ar de instrumentação e de pintura", "Reposição de leitos em secadores compactos"], "2,0 a 3,0 mm ou a granulometria do fabricante do secador"),
    "gases": ("Secagem de gases de processo", "Desidratação de correntes gasosas antes de compressão, medição ou reação. A boa resistência química da alumina é uma vantagem em CO₂ e em correntes levemente ácidas.",
              ["Gás natural e GLP", "Nitrogênio, hidrogênio e CO₂", "Gases de craqueamento", "Primeira camada em leitos combinados com peneira molecular"], "Conforme vazão e perda de carga admissível"),
    "liquidos": ("Desidratação de líquidos", "Em líquidos a transferência de massa é mais lenta, por isso grãos menores rendem mais. A 7 x 14 mesh é a granulometria recomendada para essa família de aplicações.",
                 ["Solventes orgânicos", "Hidrocarbonetos líquidos", "Correntes de processo sensíveis à água", "Colunas de secagem por percolação"], "7 x 14 mesh"),
    "guarda": ("Leito de guarda", "Uma camada de alumina antes de catalisadores e adsorventes de maior valor retém água, arraste de líquidos e contaminantes que causariam desativação irreversível.",
               ["Proteção de catalisadores", "Camada de entrada antes de peneira molecular", "Proteção de linhas e equipamentos sensíveis à água"], "Conforme o projeto do leito"),
    "oleos": ("Óleos e fluidos isolantes", "A superfície levemente ácida da alumina ativada retém compostos ácidos e umidade de óleos e fluidos, prolongando a vida do fluido e do equipamento. É uso corrente na manutenção de transformadores.",
              ["Óleo isolante de transformadores", "Óleos lubrificantes", "Fluidos refrigerantes"], "7 x 14 mesh para percolação"),
    "laboratorio": ("Laboratório e sistemas piloto", "Para ensaios, colunas de bancada e unidades piloto, a embalagem de 1 kg permite testar antes de escalar para o leito industrial.",
                    ["Colunas de secagem e purificação", "Dessecadores e tubos de secagem", "Ensaios de capacidade e regeneração", "Unidades piloto"], "7 x 14 mesh"),
}


def pagina_aplicacoes():
    mig, mig_ld = migalhas([("Início", "index.html"), ("Aplicações", None)])
    h = cabeca("Aplicações da alumina ativada: ar comprimido, gases, líquidos e óleos | Petraquim",
               "Onde usar alumina ativada: secagem de ar comprimido, gases de processo, desidratação de líquidos e solventes, leito de guarda, óleos de transformador e laboratório.",
               "aplicacoes.html", jsonld=ld(ORG_JSONLD, mig_ld))
    h += topo("aplicacoes.html")
    h += f"""
<header class="pagina-topo">
 {pic("app-gases", "", "100vw", ansioso=True)}
 <div class="wrap">
  {mig}
  <span class="rotulo claro">Aplicações</span>
  <h1>Onde a alumina ativada faz diferença</h1>
  <p>Secagem e purificação de ar, gases, líquidos e óleos. Veja em que processos o produto é indicado e qual granulometria costuma funcionar melhor.</p>
 </div>
</header>
"""
    for i, (ancora, img, tit, txt, alt) in enumerate(APPS):
        titulo, texto, itens, gran = DETALHES[ancora]
        lis = "".join(f'<li><svg><use href="#i-check"/></svg>{x}</li>' for x in itens)
        fundo = " secao-creme" if i % 2 else ""
        inv = " inverte" if i % 2 else ""
        h += f"""
<section class="secao{fundo}" id="{ancora}" aria-labelledby="t-{ancora}">
 <div class="wrap dividido{inv}">
  <div class="rv">
   <span class="rotulo">Aplicação {i + 1:02d}</span>
   <h2 id="t-{ancora}">{titulo}</h2>
   <p class="lead">{texto}</p>
   <ul class="lista-check">{lis}</ul>
   <p><strong>Granulometria usual:</strong> {gran}.</p>
   <a class="link-seta" href="cotacao.html?aplicacao={quote(titulo)}#formulario">Cotar para esta aplicação<svg><use href="#i-seta"/></svg></a>
  </div>
  <div class="lado-midia rv">{pic(img, alt, "(max-width:980px) 92vw, 560px")}<p class="credito">Imagem ilustrativa.</p></div>
 </div>
</section>"""
    h += """
<section class="secao" aria-labelledby="t-agua">
 <div class="wrap wrap-estreito">
  <div class="nota alerta rv" style="margin-top:0"><svg><use href="#i-alerta"/></svg><div><h2 id="t-agua" style="font-size:1.3rem;margin-bottom:6px">E tratamento de água potável?</h2><p>A alumina ativada também é usada na remoção de flúor e arsênio da água, mas isso exige um grau específico, com certificação para contato com água de consumo humano (como NSF/ANSI 61). O produto deste site é de grau industrial para secagem e adsorção e <strong>não é ofertado para água potável, alimentos ou fármacos</strong>.</p></div></div>
 </div>
</section>
"""
    h += cta_final("Sua aplicação não está na lista?", "Descreva o processo, o fluido e as condições de operação. Dizemos se a alumina ativada é indicada e qual granulometria usar.")
    h += rodape()
    salvar("aplicacoes.html", h)


# ---------------------------------------------------------------- EMPRESA
def pagina_empresa():
    mig, mig_ld = migalhas([("Início", "index.html"), ("Empresa", None)])
    h = cabeca("Quem somos — Ita-Bio Soluções Ltda. (Petraquim) | São Paulo/SP",
               "A Ita-Bio Soluções Ltda., marca Petraquim, fornece alumina ativada importada com atendimento técnico-comercial direto, de 1 kg a 1.000 kg, para todo o Brasil.",
               "empresa.html", jsonld=ld(ORG_JSONLD, mig_ld))
    h += topo("empresa.html")
    h += f"""
<header class="pagina-topo">
 {pic("logistica", "", "100vw", ansioso=True)}
 <div class="wrap">
  {mig}
  <span class="rotulo claro">Empresa</span>
  <h1>Ita-Bio Soluções Ltda.</h1>
  <p>Fornecimento de insumos industriais com atendimento direto, documentação em dia e flexibilidade de volume. No site, a marca Petraquim.</p>
 </div>
</header>

<section class="secao" aria-labelledby="t-quem">
 <div class="wrap dividido">
  <div class="rv">
   <span class="rotulo">Quem somos</span>
   <h2 id="t-quem">Uma empresa paulistana de soluções em insumos industriais</h2>
   <p class="lead">A Ita-Bio Soluções Ltda. está sediada na Avenida Paulista, em São Paulo, e atende empresas de todo o país.</p>
   <p>Neste site apresentamos a nossa linha de <strong>alumina ativada</strong>: produto importado, novo e em embalagem original, disponível em duas granulometrias e em embalagens de 1 kg a 1.000 kg. Atendemos desde o laboratório que precisa de um quilo para teste até a planta que troca o leito inteiro do secador.</p>
   <p>O atendimento é feito diretamente pelo Gerente de Vendas, José Roberto Rocha, que acompanha cada consulta da orientação técnica à entrega.</p>
  </div>
  <div class="lado-midia rv">{pic("alumina-embalagem", "Alumina ativada na embalagem original lacrada", "(max-width:980px) 92vw, 560px")}<p class="credito">Foto real do produto em estoque.</p></div>
 </div>
</section>

<section class="secao secao-creme" aria-labelledby="t-comp">
 <div class="wrap">
  <div class="cabecalho-secao centro rv">
   <span class="rotulo">Nossos compromissos</span>
   <h2 id="t-comp">O que você pode esperar de nós</h2>
  </div>
  <div class="valores">
   <div class="valor-item rv"><div class="ic"><svg><use href="#i-lupa"/></svg></div><h3>Transparência técnica</h3><p>Fotos reais do produto, dados comerciais claros e valores de referência sempre identificados como tal.</p></div>
   <div class="valor-item rv"><div class="ic"><svg><use href="#i-pessoa"/></svg></div><h3>Atendimento direto</h3><p>Você fala com o gerente de vendas, não com uma central. Resposta objetiva e por escrito.</p></div>
   <div class="valor-item rv"><div class="ic"><svg><use href="#i-caixa"/></svg></div><h3>Volume flexível</h3><p>De 1 kg a 1.000 kg, em compra única ou fornecimento programado.</p></div>
   <div class="valor-item rv"><div class="ic"><svg><use href="#i-doc"/></svg></div><h3>Documentação em dia</h3><p>FDS conforme ABNT NBR 14725 e faturamento com nota fiscal.</p></div>
   <div class="valor-item rv"><div class="ic"><svg><use href="#i-caminhao"/></svg></div><h3>Alcance nacional</h3><p>Envio para todo o Brasil, com frete e prazo informados na proposta.</p></div>
   <div class="valor-item rv"><div class="ic"><svg><use href="#i-escudo"/></svg></div><h3>Indicação responsável</h3><p>Só recomendamos o produto quando ele serve à aplicação. Se não servir, dizemos.</p></div>
  </div>
 </div>
</section>

<section class="secao" aria-labelledby="t-dados">
 <div class="wrap dividido" style="align-items:start">
  <div class="rv">
   <span class="rotulo">Dados cadastrais</span>
   <h2 id="t-dados">Ficha da empresa</h2>
   <p>Informações para cadastro de fornecedor. Precisa de mais documentos? Peça junto com a cotação.</p>
   <div class="botoes"><a class="btn btn-primario" href="cotacao.html">Falar com a empresa</a></div>
  </div>
  <div class="ficha-empresa rv">
   <dl>
    <div><dt>Razão social</dt><dd>Ita-Bio Soluções Ltda.</dd></div>
    <div><dt>Marca no site</dt><dd>Petraquim</dd></div>
    <div><dt>CNPJ</dt><dd>14.392.945/0001-00</dd></div>
    <div><dt>Inscrição estadual</dt><dd>161.624.00.116</dd></div>
    <div><dt>Endereço</dt><dd>Av. Paulista, 2073 — Bela Vista<br>CEP 01311-010 — São Paulo/SP — <a href="{MAPA}" target="_blank" rel="noopener">ver no mapa</a></dd></div>
    <div><dt>Telefone</dt><dd><a href="tel:{TEL}" data-conv="telefone">{TEL_TXT}</a></dd></div>
    <div><dt>WhatsApp</dt><dd><a href="{WA_LINK}" target="_blank" rel="noopener" data-conv="whatsapp">{WA_TXT}</a></dd></div>
    <div><dt>E-mail</dt><dd><a href="mailto:{EMAIL}" data-conv="email">{EMAIL}</a></dd></div>
    <div><dt>Responsável comercial</dt><dd>José Roberto Rocha — Gerente de Vendas</dd></div>
   </dl>
  </div>
 </div>
</section>
"""
    h += cta_final()
    h += rodape()
    salvar("empresa.html", h)


# ---------------------------------------------------------------- COTAÇÃO
def pagina_cotacao():
    mig, mig_ld = migalhas([("Início", "index.html"), ("Pedir cotação", None)])
    contato = f'{{"@context":"https://schema.org","@type":"ContactPage","name":"Pedir cotação de alumina ativada","url":"{SITE}/cotacao.html","about":{{"@id":"{SITE}/#organizacao"}}}}'
    h = cabeca("Pedir cotação de alumina ativada | Petraquim · Ita-Bio Soluções",
               "Peça sua cotação de alumina ativada pelo WhatsApp, e-mail ou telefone. Atendimento direto com o gerente de vendas. De 1 kg a 1.000 kg, envio para todo o Brasil.",
               "cotacao.html", jsonld=ld(ORG_JSONLD, contato, mig_ld))
    h += topo("cotacao.html")
    h += f"""
<header class="pagina-topo">
 {pic("ind-tubulacao", "", "100vw", ansioso=True)}
 <div class="wrap">
  {mig}
  <span class="rotulo claro">Cotação e contato</span>
  <h1>Peça sua cotação</h1>
  <p>Escolha o canal que preferir. Respondemos com granulometria indicada, preço, frete e prazo para a sua cidade.</p>
 </div>
</header>

<section class="secao" aria-label="Canais de atendimento e formulário">
 <div class="wrap cotacao-grid">
  <div class="rv">
   <div class="responsavel">
    <div class="mono">{MONOGRAMA}</div>
    <div><strong>José Roberto Rocha</strong><span>Gerente de Vendas · Ita-Bio Soluções Ltda.</span></div>
   </div>
   <ul class="contato-lista">
    <li><span class="ic"><svg><use href="#i-wa"/></svg></span><div><b>WhatsApp</b><a href="{WA_LINK}" target="_blank" rel="noopener" data-conv="whatsapp">{WA_TXT}</a><br><span>O jeito mais rápido de receber a cotação.</span></div></li>
    <li><span class="ic"><svg><use href="#i-fone"/></svg></span><div><b>Telefone</b><a href="tel:{TEL}" data-conv="telefone">{TEL_TXT}</a></div></li>
    <li><span class="ic"><svg><use href="#i-mail"/></svg></span><div><b>E-mail</b><a href="mailto:{EMAIL}" data-conv="email">{EMAIL}</a><br><span>Ideal para propostas formais e cadastro de fornecedor.</span></div></li>
    <li><span class="ic"><svg><use href="#i-pin"/></svg></span><div><b>Endereço</b><span style="color:var(--texto);font-size:16px">Av. Paulista, 2073 — Bela Vista<br>CEP 01311-010 — São Paulo/SP</span><br><a href="{MAPA}" target="_blank" rel="noopener" style="font-size:15px">Ver no mapa</a></div></li>
    <li><span class="ic"><svg><use href="#i-carrinho"/></svg></span><div><b>Só 1 kg?</b><a href="{ML_LINK}" target="_blank" rel="noopener" data-conv="mercadolivre">Comprar no Mercado Livre</a><br><span>Compra imediata, com nota fiscal.</span></div></li>
   </ul>
   <div class="nota" style="margin-top:0"><svg><use href="#i-info"/></svg><p>Ainda não sabe a quantidade? A <a href="alumina-ativada.html#calculadora">calculadora de leito</a> dá uma estimativa a partir da vazão e do ciclo do seu secador.</p></div>
  </div>
  {formulario(titulo="Formulário de cotação", nivel="h2")}
 </div>
</section>
"""
    h += rodape()
    salvar("cotacao.html", h)


# ---------------------------------------------------------------- PRIVACIDADE
def pagina_privacidade():
    mig, mig_ld = migalhas([("Início", "index.html"), ("Política de privacidade", None)])
    h = cabeca("Política de privacidade | Petraquim · Ita-Bio Soluções",
               "Como o site petraquim.com.br trata dados pessoais e cookies, conforme a LGPD (Lei nº 13.709/2018).",
               "politica-de-privacidade.html", jsonld=ld(mig_ld))
    h += topo("")
    h += f"""
<header class="pagina-topo">
 <div class="wrap">
  {mig}
  <h1>Política de privacidade</h1>
  <p>Última atualização: 17 de novembro de 2026.</p>
 </div>
</header>
<section class="secao">
 <div class="wrap wrap-estreito artigo">
  <p>Esta política explica como o site <strong>www.petraquim.com.br</strong> trata as informações de quem o visita, conforme a Lei Geral de Proteção de Dados (Lei nº 13.709/2018 — LGPD).</p>
  <h2>Quem é o responsável</h2>
  <p>Ita-Bio Soluções Ltda. (marca Petraquim), CNPJ 14.392.945/0001-00, Av. Paulista, 2073 — Bela Vista — CEP 01311-010 — São Paulo/SP. Contato do encarregado: <a href="mailto:{EMAIL}">{EMAIL}</a>.</p>
  <h2>Formulário de cotação</h2>
  <p>O formulário <strong>não grava nem envia dados para nenhum servidor nosso</strong>. Ao clicar em enviar, ele apenas monta uma mensagem com o que você preencheu e a abre no seu WhatsApp ou no seu programa de e-mail. A mensagem só chega até nós se você decidir enviá-la.</p>
  <h2>Dados que recebemos quando você entra em contato</h2>
  <p>Se você nos enviar uma mensagem por WhatsApp, e-mail ou telefone, receberemos os dados que informar (por exemplo, nome, empresa, telefone, e-mail, cidade e detalhes do pedido). Usamos esses dados apenas para responder, elaborar cotações e atender o pedido, com base no procedimento preliminar a contrato solicitado por você, e os guardamos pelo tempo necessário para essas finalidades e para cumprir obrigações legais e fiscais.</p>
  <h2>Cookies e medição de anúncios</h2>
  <p>O site usa a <strong>tag do Google</strong> (Google Tag Manager e Google Ads, da Google LLC) para medir o resultado dos anúncios, por exemplo quantas pessoas clicam em “Pedir cotação”. Essas ferramentas só gravam cookies de anúncios <strong>depois que você clica em “Aceitar”</strong> no aviso de privacidade (modo de consentimento do Google). Se você recusar, o Google recebe apenas sinais anônimos, sem cookies. Não enviamos ao Google o conteúdo do formulário de cotação.</p>
  <p>Sua escolha fica salva no seu navegador. Você pode mudá-la quando quiser:</p>
  <p><button class="btn btn-contorno" type="button" data-abre-consentimento>Alterar preferências de cookies</button></p>
  <p>Saiba mais na <a href="https://policies.google.com/privacy?hl=pt-BR" target="_blank" rel="noopener">Política de Privacidade do Google</a> e gerencie anúncios personalizados em <a href="https://myadcenter.google.com/" target="_blank" rel="noopener">myadcenter.google.com</a>.</p>
  <h2>Outros serviços de terceiros</h2>
  <ul>
   <li><strong>Hospedagem:</strong> GitHub Pages (GitHub, Inc.), que pode registrar dados técnicos de acesso, como o endereço IP, para segurança e funcionamento do serviço.</li>
   <li><strong>Fontes:</strong> Google Fonts (Google LLC), o que envolve a comunicação do seu navegador com os servidores do Google.</li>
   <li><strong>WhatsApp, e-mail e Mercado Livre:</strong> ao usar esses canais, valem também as políticas de privacidade dos respectivos serviços.</li>
  </ul>
  <h2>Compartilhamento</h2>
  <p>Não vendemos nem cedemos seus dados. Eles só são compartilhados quando necessário para atender o seu pedido (por exemplo, com transportadoras) ou por exigência legal.</p>
  <h2>Seus direitos</h2>
  <p>Você pode pedir a confirmação, o acesso, a correção, a portabilidade ou a eliminação dos seus dados, entre outros direitos previstos na LGPD, pelo e-mail <a href="mailto:{EMAIL}">{EMAIL}</a>. Você também pode reclamar à Autoridade Nacional de Proteção de Dados (ANPD).</p>
  <h2>Créditos das imagens</h2>
  <p>As fotos da alumina ativada são reais, do produto em estoque. As imagens de ambientes industriais e de laboratório são ilustrativas, obtidas no Unsplash sob a <a href="https://unsplash.com/pt-br/licen%C3%A7a" target="_blank" rel="noopener">licença Unsplash</a>.</p>
 </div>
</section>
"""
    h += rodape()
    salvar("politica-de-privacidade.html", h)


# ---------------------------------------------------------------- 404
def pagina_404():
    h = cabeca("Página não encontrada | Petraquim · Ita-Bio Soluções", "A página procurada não existe ou mudou de endereço.", "404.html")
    h = h.replace('<meta name="robots" content="index, follow, max-image-preview:large">', '<meta name="robots" content="noindex">')
    # Em subpastas o GitHub Pages serve o 404 com outro caminho: usar endereços absolutos.
    h += topo("")
    h += f"""
<section class="secao">
 <div class="wrap wrap-estreito" style="text-align:center">
  <span class="rotulo" style="justify-content:center">Erro 404</span>
  <h1>Página não encontrada</h1>
  <p class="lead">O endereço pode ter mudado. Estes caminhos levam você ao que procura:</p>
  <div class="botoes" style="justify-content:center;margin-top:28px">
   <a class="btn btn-primario" href="/">Ir para o início</a>
   <a class="btn btn-contorno" href="/alumina-ativada.html">Ficha técnica</a>
   <a class="btn btn-wa" href="{WA_LINK}" target="_blank" rel="noopener" data-conv="whatsapp"><svg><use href="#i-wa"/></svg>WhatsApp</a>
  </div>
 </div>
</section>
"""
    h += rodape()
    h = h.replace('href="assets/', 'href="/assets/').replace('src="assets/', 'src="/assets/').replace('srcset="assets/', 'srcset="/assets/')
    for p in ["index.html", "alumina-ativada.html", "aplicacoes.html", "empresa.html", "cotacao.html", "politica-de-privacidade.html", FDS, "favicon.svg", "favicon-64.png", "apple-touch-icon.png", "site.webmanifest"]:
        h = h.replace(f'href="{p}', f'href="/{p}')
    salvar("404.html", h)


def extras():
    paginas = [("", "1.0"), ("alumina-ativada.html", "0.9"), ("aplicacoes.html", "0.8"), ("cotacao.html", "0.8"), ("empresa.html", "0.6"), ("politica-de-privacidade.html", "0.2")]
    sm = '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
    for p, pr in paginas:
        sm += f"  <url><loc>{SITE}/{p}</loc><lastmod>{HOJE}</lastmod><priority>{pr}</priority></url>\n"
    sm += "</urlset>\n"
    salvar("sitemap.xml", sm)
    salvar("robots.txt", f"User-agent: *\nAllow: /\nDisallow: /_fonte/\n\nSitemap: {SITE}/sitemap.xml\n")
    salvar("site.webmanifest", '{"name":"Petraquim · Ita-Bio Soluções","short_name":"Petraquim","start_url":"/","display":"browser","background_color":"#ffffff","theme_color":"#2F3514","icons":[{"src":"/favicon-64.png","sizes":"64x64","type":"image/png"},{"src":"/apple-touch-icon.png","sizes":"180x180","type":"image/png"}]}\n')


if __name__ == "__main__":
    pagina_inicio(); pagina_produto(); pagina_aplicacoes(); pagina_empresa(); pagina_cotacao(); pagina_privacidade(); pagina_404(); extras()

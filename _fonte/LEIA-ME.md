# Site petraquim.com.br — versão nova (17/11/2026)

## Estrutura
| Arquivo | Conteúdo |
|---|---|
| index.html | Página inicial (anúncios do Google caem aqui): hero com foto real, aplicações, galeria real + vídeo, especificação, canais de compra, passo a passo, formulário, perguntas |
| alumina-ativada.html | Ficha técnica: definição, diagrama do leito, granulometria, especificação, valores de referência, regeneração, **calculadora de leito**, boas práticas, segurança/FDS, 9 perguntas |
| aplicacoes.html | 6 aplicações detalhadas + aviso sobre água potável |
| empresa.html | Quem somos, compromissos, ficha cadastral |
| cotacao.html | Canais de contato + formulário completo (aceita dados vindos da calculadora) |
| politica-de-privacidade.html | LGPD + cookies (consentimento) + créditos de imagens |
| 404.html | Página de erro (o GitHub Pages usa automaticamente) |
| assets/ | css, js, img (WebP + JPG), vídeo |
| _fonte/ | gerador das páginas (não é publicado) |

## Como editar
Textos comuns (telefones, e-mail, cabeçalho, rodapé, formulário) ficam em `_fonte/partes.py`;
conteúdo de cada página em `_fonte/gerar.py`. Depois de editar, rode na pasta do site:

    python _fonte/gerar.py

## Publicar (GitHub Pages)
Substituir os arquivos do repositório atual pelo conteúdo desta pasta (o CNAME foi mantido).
Os endereços antigos `/` e `/politica-de-privacidade.html` continuam iguais.
Arquivos antigos que podem ser apagados do repositório: alumina-*.jpg, og-alumina.jpg e logo-itabio.png da raiz,
alumina-video*.mp4 (tudo foi movido para assets/).

## Medição
Mantidos o GTM-KXJSFW6B, a tag AW-18567411730 e o rótulo de conversão já usado.
Agora com modo de consentimento v2: cookies de anúncio só depois de "Aceitar".
Eventos no dataLayer: `contato` (primeiro clique) e `contato_repetido`, com `canal` =
whatsapp, telefone, email, mercadolivre, fds, form-whatsapp, form-email.

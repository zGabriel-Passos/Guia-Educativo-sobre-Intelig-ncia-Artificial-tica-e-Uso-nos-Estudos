# Entre Linha IA

Guia educativo sobre o uso ético da inteligência artificial nos estudos. O projeto reúne conteúdos sobre aprendizagem, autoria, direitos autorais, desinformação e segurança digital, além de quiz e mural comunitário.

## Funcionalidades

- Página inicial com os temas organizados em seções e navegação por âncoras.
- Conteúdo aberto para leitura, sem necessidade de conta.
- Quiz interativo com feedback e pontuação local (não salva resultados).
- Login e cadastro exclusivamente com conta Google via Firebase Authentication.
- Mural público de relatos armazenados no Cloud Firestore.
- Publicação de relatos para usuários autenticados.
- Edição e exclusão de relatos permitidas somente ao autor autenticado.
- Reações 👍 e 🚀 em relatos de outras pessoas, disponíveis somente após login Google. Visitantes podem consultar as contagens.
- Alternância entre tema claro e escuro, com preferência salva no navegador.
- Layout responsivo para celular, tablet e desktop.

## Tecnologias

- Python e Flask com templates Jinja2.
- HTML, CSS e JavaScript em módulos.
- Firebase Authentication e Cloud Firestore.
- Firebase JavaScript SDK carregado por CDN.
- Vercel para hospedagem.

## Executar localmente

Requisitos: Python 3.10 ou superior e pip.

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
pip install -r requirements.txt
python app.py
```

Acesse `http://127.0.0.1:5000`. Se o PowerShell bloquear a ativação do ambiente virtual, use `\.venv\Scripts\python.exe -m pip install -r requirements.txt` e depois `\.venv\Scripts\python.exe app.py`.

## Configuração do Firebase

O app web usa a configuração pública do Firebase em `static/js/firebase.js`. A chave `apiKey` do Firebase Web identifica o projeto e não substitui as regras de segurança do Firestore.

No Firebase Console:

1. Ative **Authentication → Sign-in method → Google**.
2. Adicione `localhost` em **Authentication → Settings → Authorized domains** para desenvolvimento local. Adicione também o domínio de produção usado na Vercel.
3. Crie ou ative o banco **Cloud Firestore**.
4. Publique as regras de [`firestore.rules`](firestore.rules) em **Firestore Database → Rules**.
5. Confirme que o domínio de produção corresponde ao app Firebase configurado.

As regras permitem leitura pública dos relatos. Criar exige login; editar e excluir exigem que o UID autenticado seja o autor. Reações ficam em `relatos/{relatoId}/reacoes/{uid_tipo}` e também exigem uma conta não anônima. Não remova essas restrições: elas protegem os relatos de alterações por terceiros.

Se o Firebase mostrar `permission-denied`, confira se as regras locais foram publicadas no projeto correto e se o documento está na coleção `relatos`.

## Organização do projeto

```text
app.py                  Rotas Flask e cabeçalhos HTTP
data/conteudo.py        Textos dos temas do guia
templates/              Templates Jinja2
  base.html             Navegação, controle de tema e rodapé
  home.html             Landing page e seções dos conteúdos
  pagina.html           Página individual de apoio/fallback
  mural.html            Formulário e lista de relatos
  entrar.html           Login Google
  quiz.html             Quiz educativo
static/css/             Estilos e temas claro/escuro
static/js/              Navegação, quiz e integração Firebase
firestore.rules         Regras de acesso do Firestore
vercel.json             Configuração de deploy na Vercel
requirements.txt        Dependências Python
```

## Publicação na Vercel

O repositório contém `vercel.json` configurado para executar a aplicação Flask. Importe o repositório na Vercel e confirme que o projeto usa a raiz deste diretório. Depois do primeiro deploy, inclua o domínio gerado em **Authorized domains** no Firebase Authentication.

## Documentação complementar

- [`guia_planejamento.md`](guia_planejamento.md): objetivos acadêmicos, conteúdo e etapas do projeto de extensão.
- [`workflow-site.md`](workflow-site.md): fluxo planejado, funcionalidades e arquitetura do site.

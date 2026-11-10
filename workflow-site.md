# 🧭 Workflow do Site: Guia Educativo sobre IA, Ética e Uso nos Estudos

**Stack:** Flask (Jinja2) + Firebase Auth + Firestore + Vercel
**Visual:** landing page no estilo HeyVovo (escuro quente, manuscrito, terracota)
**Escopo deste documento:** como o **site** funciona (páginas, conteúdo, fluxos, segurança e tecnologias). Não é o roteiro da documentação da extensão.

---

## 1. Visão geral do fluxo do usuário

```
Entra no site (Home)
   │
   ├─► Lê os guias (Seções 1, 2 e Cibersegurança)      → sem login
   ├─► Faz o Quiz                                       → sem login (pontuação salva só se logado)
   ├─► Vê o Mural e curte relatos                       → sem login
   └─► Quer comentar / editar / excluir                 → LOGIN (Firebase Auth)
```

| Ação | Precisa de login? |
| :--- | :---: |
| Ler os conteúdos | Não |
| Fazer o quiz | Não |
| Ver o mural | Não |
| Curtir relato de outra pessoa | Não (ver 6.4) |
| Publicar relato/dúvida/opinião | **Sim** |
| Editar ou excluir o **próprio** relato | **Sim** (só o dono) |
| Editar/excluir relato de outra pessoa | **Nunca** |
| Responder relato de outra pessoa | Não existe (decisão do projeto) |

---

## 2. Mapa do site e navegação

### 2.1 Navbar (header)

Adaptação do guia HeyVovo: ele pede só 1 botão, mas aqui a navbar precisa dos tópicos. Mantemos o estilo (fundo transparente, sem borda, logo em Caveat terracota) e deixamos **o botão de destaque à direita** para o login.

```
[Logo: Guia IA Ética]  Uso nos Estudos · Ética & Direitos · Deepfakes · Cibersegurança · Quiz · Comunidade     [Entrar]
```

| Item | Rota | Tipo |
| :--- | :--- | :--- |
| Logo | `/` | Home |
| Uso nos Estudos | `/estudos` | Seção 1 |
| Ética & Direitos | `/etica-direitos` | Seção 2 (parte 1) |
| Deepfakes & Desinformação | `/desinformacao` | Seção 2 (parte 2) |
| Cibersegurança | `/ciberseguranca` | Complemento |
| Quiz | `/quiz` | Interativo |
| Comunidade | `/mural` | Seção 3 |
| Entrar / Perfil | `/entrar` · `/perfil` | Auth |

**Mobile:** menu hambúrguer; "Entrar" continua visível.

### 2.2 Estrutura de páginas

| Página | Rota | Método | Descrição |
| :--- | :--- | :---: | :--- |
| Home | `/` | GET | Landing (6 seções do estilo HeyVovo) |
| Uso nos Estudos | `/estudos` | GET | Conteúdo da Seção 1 |
| Ética & Direitos | `/etica-direitos` | GET | Pirataria, direitos autorais, licenças |
| Deepfakes | `/desinformacao` | GET | Mídias sintéticas e checagem |
| Cibersegurança | `/ciberseguranca` | GET | Boas práticas de segurança |
| Quiz | `/quiz` | GET | Quiz interativo |
| Mural | `/mural` | GET | Lista pública de relatos |
| Login/Cadastro | `/entrar` | GET | Telas de autenticação |
| Perfil | `/perfil` | GET | Meus relatos e pontuação do quiz |
| Privacidade | `/privacidade` | GET | Aviso LGPD e termos do mural |
| API interna | `/api/...` | POST/PATCH/DELETE | Ver seção 7 |

---

## 3. Home (landing no estilo HeyVovo)

Seguindo a ordem obrigatória das 6 seções do guia visual.

1. **Navbar**: conforme 2.1.
2. **Hero**
   - Headline (Caveat, 6 a 8 palavras): *"Use a IA a seu favor, sem cair em armadilhas"*
   - Subtítulo (máx. 2 linhas): *"Um guia prático sobre ética, plágio, direitos autorais e segurança na era da inteligência artificial."*
   - CTA: **"Começar a ler"** (rola para "Como funciona" ou abre `/estudos`)
3. **Como funciona** (3 passos com linha conectora)
   1. **Leia**: entenda os limites do uso ético da IA.
   2. **Teste**: faça o quiz e veja o que fixou.
   3. **Compartilhe**: entre e deixe seu relato, dúvida ou opinião.
4. **Por que este guia?** (grid 2x2, só texto)
   - **Uso consciente**: aprenda a usar a IA como tutor, sem substituir sua autoria.
   - **Respeito ao criador**: entenda direitos autorais, licenças e pirataria.
   - **Verdade em tempo de deepfake**: aprenda a checar fontes e identificar mídias falsas.
   - **Segurança digital**: proteja seus dados, contas e as informações que você divide com ferramentas de IA.
5. **CTA final** (caixa com glow terracota)
   - Título: *"Entendeu o tema? Conta pra gente."*
   - Subtítulo: *"Deixe seu relato no mural da comunidade."*
   - Botão: **"Ir para a comunidade"**
6. **Footer**: logo + tagline *"Educação digital com consciência."*

> Regras visuais herdadas: Caveat + DM Sans; sem fundo branco; sem cores frias; uma única cor de destaque (`#d4724a`); sem imagens de stock; animação `fadeUp` com stagger nos cards.

---

## 4. Conteúdo do site (tópicos e resumos de pesquisa)

> Estes blocos servem de base para os textos de cada página. Cada página deve terminar com um **bloco "Ponto de atenção"** (alerta em card com borda terracota) e um botão **"Fazer o quiz"** / **"Comentar no mural"**.
> ⚠️ Antes de publicar, confirmar leis, números e referências em fontes oficiais. Legislação sobre IA muda rápido.

### 4.1 `/estudos`: Uso Produtivo e Ético da IA nos Estudos (Seção 1)

**4.1.1 O que é um LLM (em linguagem simples)**
- Modelos de linguagem geram texto prevendo a continuação mais provável. Não "sabem" a verdade: podem errar com muita confiança (as chamadas **alucinações**).
- **Ponto de atenção:** nunca trate a resposta da IA como fonte final. Ela é ponto de partida.

**4.1.2 IA como tutor complementar**
- Resumir matérias complexas e pedir explicação "como se eu tivesse 12 anos".
- Gerar mapas mentais, listas de tópicos e cronogramas de estudo.
- Criar simulados e perguntas de revisão sobre o seu próprio material.
- Pedir exemplos e analogias para conceitos difíceis.
- Revisão gramatical e sugestões de clareza.
- **Boa prática:** peça para a IA *te perguntar*, em vez de só *te responder*. Isso força o aprendizado ativo.

**4.1.3 A linha entre apoio e plágio**

| ✅ Uso ético | ❌ Uso antiético / plágio |
| :--- | :--- |
| Estruturar tópicos e ideias iniciais | Copiar a resposta da IA e entregar como sua |
| Tirar dúvidas e pedir explicações | Substituir sua escrita por texto sintetizado |
| Revisão gramatical do **seu** texto | Esconder que usou IA quando a regra exige declarar |
| Gerar simulados para estudar | Usar IA em prova ou atividade em que o uso é proibido |
| Brainstorming de base | Inventar referências ou citações que a IA gerou |

**4.1.4 Integridade acadêmica**
- Verifique as **regras da sua instituição e do professor**: cada um define o que é permitido.
- **Transparência:** declare o uso (ex.: "Usei [ferramenta] para revisar a estrutura dos tópicos").
- **Cite** quando a ideia ou trecho não for seu.
- **Confira** toda referência: a IA pode inventar autores, livros e links que não existem.
- Detectores de IA **não são confiáveis** e geram falsos positivos. O que protege você é o seu processo (rascunhos, anotações, histórico de versões).

**4.1.5 Checklist antes de entregar um trabalho**
- [ ] Eu entendo tudo o que está escrito aqui?
- [ ] O texto está na minha voz e com a minha análise?
- [ ] Verifiquei dados, datas e referências?
- [ ] Declarei o uso de IA, quando necessário?
- [ ] O uso respeitou a regra da disciplina?

---

### 4.2 `/etica-direitos`: Ética, Pirataria e Direitos Autorais (Seção 2, parte 1)

**4.2.1 O que é propriedade intelectual**
- Obras (textos, imagens, músicas, jogos, códigos) têm autoria e proteção legal.
- No Brasil, a base é a **Lei de Direitos Autorais (Lei nº 9.610/1998)**; software tem lei própria (**Lei nº 9.609/1998**).
- Violar direitos autorais pode gerar responsabilização civil e, em certos casos, penal.

**4.2.2 Pirataria: o que é e por que importa**
- Pirataria = copiar, distribuir ou usar obras e softwares sem autorização.
- Exemplos: baixar jogo/programa "crackeado", compartilhar PDFs de livros pagos, distribuir filmes e séries sem licença.
- Riscos: **processos**, **malware embutido** em arquivos piratas, perda de dados e prejuízo a quem criou.

**4.2.3 Reuso de código, artes e assets (alerta para devs)**
- **Recriar jogos de navegador** usando o código, arte, sons ou nome de outro projeto sem autorização é violação.
- Ter acesso ao código-fonte (ex.: "inspecionar elemento") **não significa ter permissão de copiar**.
- Regra de ouro: *"acessível" ≠ "livre para usar"*.
- Para aprender: estude a ideia, refaça com **suas próprias** artes, código e nomes.

**4.2.4 Licenças de software**

| Tipo | Ideia central | Exemplo de cuidado |
| :--- | :--- | :--- |
| **Proprietário** | Uso restrito, geralmente pago | Proibido copiar/redistribuir |
| **Open Source permissivo** (MIT, Apache 2.0) | Pode usar e modificar com poucas condições | Manter aviso de licença e autoria |
| **Copyleft** (GPL) | Derivados precisam manter a mesma licença | Atenção ao incorporar em projeto fechado |
| **Creative Commons** (para mídias) | Várias variações (BY, NC, ND, SA) | Ler as condições antes de usar |
| **Domínio público** | Sem restrição de uso | Confirmar que a obra realmente está em domínio público |

**4.2.5 Código gerado por IA e direitos autorais**
- A IA pode reproduzir trechos parecidos com código ou textos de terceiros. Revise e entenda o que foi gerado.
- Status legal de obras geradas por IA ainda está **em debate**; evite afirmar certezas. Linguagem recomendada no site: *"o tema ainda está em discussão e vale checar a política da sua instituição e das plataformas"*.

**4.2.6 O papel do desenvolvedor (ADS)**
- Construir soluções **originais**, respeitar licenças e dar crédito.
- Documentar dependências e licenças do projeto.
- Não transformar "cópia" em "portfólio".

**Ponto de atenção:** *"Se você não criou e não tem licença, pergunte antes de usar."*

---

### 4.3 `/desinformacao`: Deepfakes, Mídias Sintéticas e Desinformação (Seção 2, parte 2)

**4.3.1 Como funcionam (em alto nível)**
- **Texto:** modelos de linguagem geram notícias, comentários e e-mails convincentes em segundos.
- **Imagem:** modelos geram fotos realistas de pessoas e eventos que nunca existiram.
- **Voz:** clonagem de voz a partir de poucos segundos de áudio.
- **Vídeo (deepfake):** troca ou animação de rostos e movimentos labiais.

**4.3.2 Riscos reais**
- Golpes com **voz clonada** ("parente pedindo dinheiro urgente").
- **Montagens íntimas e difamatórias** (crime e causa de dano grave à vítima).
- Notícias falsas virais, principalmente em períodos eleitorais e crises.
- **Fraudes** em documentos, comprovantes e perfis falsos.

**4.3.3 Como checar uma informação (método prático)**
1. **Pare** antes de compartilhar. Conteúdo que provoca raiva ou pressa merece mais desconfiança.
2. **Fonte:** quem publicou? Tem histórico confiável? Existe o site/perfil oficial?
3. **Cruze:** a notícia aparece em outros veículos confiáveis?
4. **Busca reversa de imagem** (Google Lens, TinEye) para achar a origem.
5. **Contexto:** a data, o local e o evento batem com a imagem/vídeo?
6. **Metadados:** verificar dados da imagem pode ajudar, mas **metadados somem ou são editados com facilidade**; não são prova definitiva.
7. **Agências de checagem:** consultar Aos Fatos, Lupa, Comprova, entre outras.

**4.3.4 Sinais que podem indicar mídia sintética (não são garantia)**
- Mãos, dentes, brincos e texto dentro da imagem com distorções.
- Piscar, sombra e iluminação estranhos em vídeos.
- Sincronia labial imperfeita, voz sem respiração natural.
- ⚠️ **Os modelos melhoram rápido.** A ausência desses sinais **não prova** que o conteúdo é real. O hábito de checar a fonte vale mais do que "olho clínico".

**4.3.5 Responsabilidade ética ao compartilhar**
- Compartilhar também é publicar: você pode responder por isso.
- Não crie nem compartilhe conteúdo sintético de terceiros sem consentimento.
- Em dúvida, **não repasse**.

**4.3.6 Se você for vítima**
- Guarde provas (prints, links, data/hora), **não apague** antes de registrar.
- Denuncie na plataforma e procure a polícia/delegacia (incluindo delegacias de crimes cibernéticos, quando houver).
- No Brasil, a **SaferNet** oferece canal de denúncia e orientação.

**Ponto de atenção:** *"Se parece bom demais, chocante demais ou urgente demais, verifique antes de repassar."*

---

### 4.4 `/ciberseguranca`: Cibersegurança no uso de IA (complemento)

**4.4.1 O que você NÃO deve colocar em chats de IA**
- Senhas, tokens, chaves de API, dados bancários.
- Documentos pessoais (CPF, RG), dados de saúde, endereço.
- Dados de colegas, alunos ou professores.
- Código/documentos confidenciais da escola ou empresa.
- **Regra:** trate o chat como um local onde o conteúdo pode ser armazenado e revisado, conforme a política de cada ferramenta.

**4.4.2 Contas e senhas**
- Use **senhas longas e únicas** + gerenciador de senhas.
- Ative **verificação em duas etapas (2FA)**.
- Não reutilize a senha do e-mail em outros serviços.

**4.4.3 Phishing e golpes (potencializados por IA)**
- Mensagens e e-mails ficam cada vez mais bem escritos; **erro de português não é mais um bom sinal de golpe**.
- Desconfie de urgência, prêmios, links encurtados e pedidos de código/PIX.
- Confirme por outro canal (ligue para o número que você já conhece).

**4.4.4 Prompt injection e extensões duvidosas (noções básicas)**
- Textos de páginas ou arquivos podem conter instruções escondidas que tentam manipular a IA.
- Instale apenas extensões/plugins de IA de fontes oficiais e confira as permissões.

**4.4.5 Pirataria e malware**
- Cracks, keygens e "mods" gratuitos são vetores comuns de malware (ligação direta com 4.2).

**4.4.6 Privacidade e LGPD**
- A **LGPD (Lei nº 13.709/2018)** protege dados pessoais.
- Você pode pedir acesso, correção e exclusão dos seus dados.
- Neste site: coletamos o **mínimo** (ver seção 8.5).

**4.4.7 Checklist rápido de segurança**
- [ ] 2FA ativado?
- [ ] Senha única no e-mail principal?
- [ ] Sem dados pessoais nos prompts?
- [ ] Software só de fontes oficiais?
- [ ] Verifiquei o link antes de clicar?

---

### 4.5 `/mural`: Comunidade (Seção 3)

**Texto de apresentação:** *"Leu o conteúdo? Conte o que entendeu, tire uma dúvida ou compartilhe uma experiência. Seu relato ajuda outras pessoas a refletirem."*

**Categorias do relato (campo obrigatório):**
- 💬 Opinião
- ❓ Dúvida
- 📝 O que aprendi
- 📌 Caso vivenciado (plágio, pirataria, golpe, desinformação)

**Regras de convivência (visíveis acima do formulário):**
- Respeite as pessoas; sem ofensas, discriminação ou assédio.
- Não publique dados pessoais (seus ou de outros).
- Não publique conteúdo ilegal, pirata ou links suspeitos.
- Ao relatar um caso, **não identifique terceiros**.
- O conteúdo pode ser removido pela moderação.

---

## 5. Quiz (`/quiz`)

### 5.1 Estrutura
- **Banco:** 20 a 30 perguntas, sorteando 10 por tentativa.
- **Formato:** múltipla escolha (4 alternativas) e verdadeiro/falso.
- **Temas:** Seção 1 (uso ético), Seção 2 (direitos e deepfakes), Cibersegurança.
- **Feedback imediato:** após cada resposta, mostrar *certo/errado + explicação curta + link para o trecho do guia*.
- **Resultado final:** pontuação, nível e botão **"Compartilhar no mural"** (leva ao formulário, exigindo login).

### 5.2 Níveis (ideia de gamificação leve)
| Pontuação | Mensagem |
| :---: | :--- |
| 0–4 | "Vale reler o guia." |
| 5–7 | "Você está no caminho." |
| 8–10 | "Você manda bem em IA com ética." |

### 5.3 Onde ficam as perguntas
- **Opção recomendada:** arquivo `quiz.json` no servidor (Flask), com a **resposta correta validada no backend** (`POST /api/quiz/verificar`), para que o gabarito não fique exposto no HTML.
- Se logado: salvar a pontuação em `quiz_resultados` (Firestore).

### 5.4 Exemplos de perguntas
1. *Usar IA para organizar tópicos de um trabalho e depois escrever com suas palavras é…* → ✅ uso ético.
2. *Se a IA citou um livro, posso confiar que ele existe?* → ❌ Não, é preciso verificar.
3. *Ter acesso ao código de um site significa poder copiá-lo?* → ❌ Não.
4. *Detectores de IA são 100% confiáveis?* → ❌ Não.
5. *Um áudio idêntico à voz de um parente pedindo PIX urgente deve ser…* → confirmado por outro canal.
6. *Qual licença exige que derivados mantenham a mesma licença?* → GPL (copyleft).
7. *Posso colocar minha senha em um chat de IA para "ele guardar"?* → ❌ Não.
8. *Ausência de "sinais estranhos" em uma imagem prova que ela é real?* → ❌ Não.

---

## 6. Sistema de Comunidade (comentários/relatos)

### 6.1 Regras funcionais

| Funcionalidade | Regra |
| :--- | :--- |
| **Criar relato** | Apenas logado. Campos: categoria, texto (20 a 800 caracteres). |
| **Editar** | Apenas o **autor**. Marca "editado". |
| **Excluir** | Apenas o **autor** (e o admin/moderador). |
| **Curtir** | Qualquer visitante (ver 6.4). Um like por pessoa/relato. |
| **Responder** | **Não existe.** Sem threads. |
| **Ordenação** | Mais recentes (padrão) ou Mais curtidos. |
| **Paginação** | 10 relatos por página (cursor do Firestore). |
| **Denunciar** | Botão "Denunciar" (logado) → fila de moderação. |

### 6.2 Exibição
- Nome de exibição (apelido), categoria, data, texto, contagem de curtidas.
- **Não exibir e-mail** publicamente em nenhuma situação.
- Botões **Editar/Excluir** aparecem apenas nos relatos do usuário logado (e a regra é imposta no servidor, não só na interface).

### 6.3 Moderação
- Status do relato: `pending` → `approved` | `rejected`.
- Fase inicial (recomendado): **pré-moderação** até o projeto ganhar confiança; depois, publicação imediata + denúncia.
- Lista de palavras bloqueadas (filtro simples) + moderação manual por conta admin (custom claim `admin`).

### 6.4 Curtida sem login (como fazer com segurança)
Curtir sem login abre brecha para **spam de likes**. Solução recomendada:
- Usar **Firebase Anonymous Auth**: o visitante recebe um `uid` anônimo e invisível, sem cadastro.
- Documento de like: `relatos/{id}/curtidas/{uid}` (um por uid; o ID do documento impede duplicata).
- O contador é atualizado no servidor (transação ou incremento atômico).
- **Rate limit por IP** no endpoint de curtir.
- Aviso: isso reduz, mas não elimina fraude (a pessoa pode limpar o navegador). Para um projeto comunitário, é um equilíbrio aceitável.

---

## 7. Arquitetura técnica

```
Navegador ──► Vercel (Flask serverless)
                 │  ├─ Templates Jinja2 + CSS (estilo HeyVovo) + JS
                 │  ├─ Valida ID Token (Firebase Admin SDK)
                 │  └─ Sanitiza, valida e grava
                 ▼
            Firebase
              ├─ Authentication (e-mail/senha, Google, anônimo p/ curtidas)
              └─ Firestore (relatos, curtidas, quiz_resultados, denuncias)
```

### 7.1 Tecnologias

| Camada | Tecnologia | Função |
| :--- | :--- | :--- |
| Frontend | Jinja2 + HTML/CSS/JS | Páginas e interatividade |
| Estilo | CSS com variáveis (paleta HeyVovo); Tailwind opcional | Visual |
| Fontes | Caveat + DM Sans | Identidade visual |
| Backend | Flask | Rotas, validação, regras de negócio |
| Auth | Firebase Auth (SDK web) | Login/cadastro |
| Verificação | Firebase Admin SDK (Python) | Validar token no servidor |
| Banco | Firestore | Persistência |
| Hospedagem | Vercel | Deploy contínuo via GitHub |
| Segurança extra | Flask-WTF (CSRF), Flask-Limiter, Flask-Talisman, `bleach`/`markupsafe` | Ver seção 8 |

> **Decisão sobre estilo:** o guia HeyVovo manda usar HTML+CSS+JS puro para Flask; a ideia original cita Tailwind. Sugestão: CSS próprio com variáveis (fiel ao guia visual). Tailwind pode ficar para utilitários, se preferir.

### 7.2 Fluxo de autenticação
1. Usuário clica em **Entrar** → Firebase Auth (SDK web) autentica.
2. O navegador recebe um **ID Token (JWT)**.
3. Em cada ação protegida (`POST/PATCH/DELETE`), o front envia `Authorization: Bearer <token>`.
4. O Flask valida o token com o **Admin SDK** (`verify_id_token`) e extrai o `uid`.
5. O backend confere que `autor_uid == uid` antes de editar/excluir.

### 7.3 Rotas da API

| Método | Rota | Auth | Descrição |
| :--- | :--- | :---: | :--- |
| GET | `/mural` | Não | Lista relatos aprovados |
| POST | `/api/relatos` | ✅ | Cria relato |
| PATCH | `/api/relatos/<id>` | ✅ dono | Edita |
| DELETE | `/api/relatos/<id>` | ✅ dono/admin | Exclui |
| POST | `/api/relatos/<id>/curtir` | Anônimo ou logado | Alterna curtida |
| POST | `/api/relatos/<id>/denunciar` | ✅ | Denuncia |
| POST | `/api/quiz/verificar` | Não | Valida respostas |
| POST | `/api/quiz/resultado` | ✅ | Salva pontuação |
| DELETE | `/api/conta` | ✅ | Exclui conta e dados (LGPD) |

### 7.4 Modelo de dados (Firestore)

```
relatos/{relatoId}
  autor_uid:      string
  autor_nome:     string   (apelido)
  categoria:      "opiniao" | "duvida" | "aprendi" | "caso"
  texto:          string   (20–800)
  status:         "pending" | "approved" | "rejected"
  curtidas:       number
  criado_em:      timestamp (SERVER_TIMESTAMP)
  editado_em:     timestamp | null

relatos/{relatoId}/curtidas/{uid}
  criado_em:      timestamp

usuarios/{uid}
  apelido:        string
  criado_em:      timestamp

quiz_resultados/{id}
  uid:            string
  pontuacao:      number
  total:          number
  criado_em:      timestamp

denuncias/{id}
  relato_id:      string
  denunciante_uid:string
  motivo:         string
  criado_em:      timestamp
```

---

## 8. Segurança

### 8.1 Autenticação e autorização
- Firebase Auth com **e-mail/senha** e **Google**.
- Exigir **e-mail verificado** para publicar.
- Política de senha mínima (≥ 8 caracteres) e recuperação por e-mail.
- **Autorização no servidor**: a checagem de "dono do relato" nunca depende do front.
- Perfil admin via **custom claims** (não via campo editável pelo usuário).

### 8.2 Firestore Security Rules (resumo da lógica)
- `relatos`: leitura pública apenas se `status == "approved"`; criação só com `request.auth != null`, `autor_uid == request.auth.uid`, tamanho de texto validado, `curtidas == 0`; **update/delete somente se `resource.data.autor_uid == request.auth.uid`** (e sem permitir alterar `autor_uid`, `status`, `curtidas`).
- `curtidas/{uid}`: criar/excluir só se `uid == request.auth.uid`.
- `usuarios/{uid}`: leitura/escrita só do próprio dono.
- `quiz_resultados`: criar só o próprio; leitura só do dono.
- `denuncias`: só criação; leitura apenas admin.
- Princípio: **negar por padrão**, abrir só o necessário.

### 8.3 Proteções da aplicação (OWASP)

| Risco | Mitigação |
| :--- | :--- |
| **XSS** | Escape automático do Jinja2 (nunca usar `|safe` em conteúdo de usuário); `bleach` para limpar; CSP restritiva |
| **CSRF** | Flask-WTF/CSRFProtect (ou verificação de token + `SameSite`) |
| **Injeção / dados malformados** | Validação de tipo, tamanho e lista de categorias permitidas no servidor |
| **Spam / abuso** | Flask-Limiter (ex.: 5 relatos/hora por usuário; limite por IP em curtidas) |
| **Quebra de controle de acesso (IDOR)** | Conferir `autor_uid == uid` em PATCH/DELETE |
| **Exposição de segredos** | Credenciais do Admin SDK em **variáveis de ambiente da Vercel**; nunca no Git (`.gitignore`, `.env`) |
| **Clickjacking** | `X-Frame-Options: DENY` / `frame-ancestors 'none'` |
| **Sniffing / MITM** | HTTPS obrigatório + HSTS |
| **Cookies** | `Secure`, `HttpOnly`, `SameSite=Lax` |
| **Dependências vulneráveis** | `pip-audit`/Dependabot, versões fixadas no `requirements.txt` |
| **Bots no cadastro** | Firebase App Check (reCAPTCHA) |

### 8.4 Cabeçalhos HTTP (Flask-Talisman ou `vercel.json`)
- `Content-Security-Policy`
- `Strict-Transport-Security`
- `X-Content-Type-Options: nosniff`
- `Referrer-Policy: strict-origin-when-cross-origin`
- `Permissions-Policy` (desativar o que não for usado)

### 8.5 Privacidade e LGPD
- Coletar o **mínimo**: apelido + e-mail (via Auth). Sem telefone, CPF ou endereço.
- Exibir publicamente **apenas o apelido**.
- Página `/privacidade` com: quais dados, finalidade, prazo, contato e direitos do titular.
- **Consentimento** no cadastro (checkbox de aceite dos termos).
- Botão **"Excluir minha conta e meus relatos"**.
- Aviso para **menores de idade** (público escolar): recomendar uso com ciência do responsável e orientar a não expor dados pessoais.

### 8.6 Moderação e conteúdo
- Pré-moderação inicial, fila de denúncias, remoção de conteúdo ofensivo ou ilegal.
- Registro (log) de ações administrativas.

### 8.7 Boas práticas de deploy (Vercel)
- Variáveis: `FIREBASE_PROJECT_ID`, `FIREBASE_CLIENT_EMAIL`, `FIREBASE_PRIVATE_KEY`, `SECRET_KEY`, config pública do SDK web.
- Ambientes separados (preview x produção).
- Restringir domínios autorizados no Firebase Auth e a chave de API web por domínio.
- Ativar **autenticação em dois fatores** nas contas GitHub, Vercel e Firebase.

> 🔎 **Observação:** a configuração pública do Firebase (apiKey etc.) no front **não é segredo**; a proteção vem das **Security Rules** e da validação no backend.

---

## 9. Acessibilidade e responsividade
- Contraste adequado do texto creme sobre marrom escuro (verificar com ferramenta de contraste).
- Navegação por teclado, `focus` visível, `aria-label` em botões de ícone (ex.: coração de curtir).
- `prefers-reduced-motion`: desativar `fadeUp` para quem preferir.
- Textos curtos, linguagem simples e títulos hierárquicos (`h1`/`h2`/`h3`).
- Breakpoints: mobile (1 coluna), tablet, desktop; botões em largura total no mobile.

---

## 10. Estrutura de pastas sugerida

```
guia-ia-etica/
├─ app.py                 # app Flask (rotas)
├─ api/index.py           # entrada serverless (Vercel)
├─ firebase_admin_init.py # init do Admin SDK via env
├─ services/
│   ├─ auth.py            # verificação de token
│   ├─ relatos.py         # CRUD + regras de dono
│   └─ quiz.py
├─ data/quiz.json
├─ templates/
│   ├─ base.html          # navbar + footer
│   ├─ home.html
│   ├─ estudos.html
│   ├─ etica_direitos.html
│   ├─ desinformacao.html
│   ├─ ciberseguranca.html
│   ├─ quiz.html
│   ├─ mural.html
│   ├─ perfil.html
│   └─ privacidade.html
├─ static/
│   ├─ css/style.css      # variáveis HeyVovo
│   └─ js/{auth.js, mural.js, quiz.js}
├─ firestore.rules
├─ vercel.json
├─ requirements.txt
└─ .gitignore
```

---

## 11. Ordem de construção (checklist de desenvolvimento)

1. [ ] Projeto Firebase (Auth + Firestore) e domínios autorizados
2. [ ] Base Flask + `base.html` (navbar, footer, tokens de cor/fonte)
3. [ ] Home (6 seções) e páginas de conteúdo
4. [ ] Login/cadastro (Firebase Auth) + verificação de token no Flask
5. [ ] Mural: listar, criar, editar, excluir (regra de dono)
6. [ ] Curtidas (Anonymous Auth + rate limit)
7. [ ] Quiz (JSON + validação no servidor + salvar pontuação)
8. [ ] Moderação e denúncias
9. [ ] Security Rules, CSP/headers, CSRF, rate limit
10. [ ] Privacidade/LGPD e exclusão de conta
11. [ ] Testes de segurança (tentar editar relato de outra pessoa, XSS, abuso de like)
12. [ ] Deploy na Vercel e revisão de variáveis de ambiente
13. [ ] Prints para o relatório da extensão (Hero, artigos, Mural, quiz)

---

## 12. Testes de segurança que valem registrar no relatório
- Usuário A **não consegue** editar/excluir relato do usuário B (UI **e** API direta).
- Entrada `<script>alert(1)</script>` aparece como texto, sem executar.
- Mais de N relatos/hora → bloqueio por rate limit.
- Curtir duas vezes o mesmo relato não duplica.
- Acesso a `denuncias` por usuário comum é negado nas Rules.
- Nenhuma chave privada no repositório.
# 📘 Guia de Planejamento: Projeto de Extensão (ADS 2026/2)
**Projeto:** Guia Educativo sobre Inteligência Artificial, Ética e Uso nos Estudos  
**Stack Técnica:** Python (Flask) + Firebase (Firestore) + Vercel  
**Curso:** CST em Análise e Desenvolvimento de Sistemas (2º Semestre - UNIP)  
**Disciplina:** Atividades de Extensão II (Programa 8 – Inova Mais UNIP)  

---

## 🎯 1. Visão Geral e Alinhamento Acadêmico

O projeto consiste no desenvolvimento e na implantação de um portal web educativo e interativo voltado para estudantes e professores da rede pública e da comunidade local. O objetivo central é fornecer um guia prático e crítico sobre como utilizar a Inteligência Artificial no ambiente acadêmico, enfatizando os limites da ética, os riscos do plágio, a proteção aos direitos autorais e o combate à desinformação.

### 📊 Alinhamento com as ODS e Eixos Institucionais
* **ODS 4 (Educação de Qualidade):** Fomenta o uso responsável, crítico e produtivo de tecnologias digitais no processo de aprendizagem.
* **ODS 9 (Indústria, Inovação e Infraestrutura):** Promove o letramento tecnológico sobre ferramentas emergentes e inovação digital.
* **Eixos UNIP Atendidos:** Educação, Desenvolvimento Tecnológico, Inclusão Social e Desenvolvimento Comunitário.

---

## 📚 2. Estrutura de Conteúdo e Seções do Portal (Detalhamento Conceitual)

### 📌 Seção 1: Uso Produtivo e Ético da IA nos Estudos
* **IA como Tutor Complementar:** Orientar como utilizar modelos de linguagem (LLMs) para sintetizar matérias complexas, gerar mapas mentais, criar simulados de perguntas e explicar conceitos difíceis.
* **A Linha entre Apoio e Plágio:**
  * *Uso Permitido/Ético:* Estruturação de tópicos, esclarecimento de dúvidas, revisão gramatical e geração de ideias base.
  * *Uso Antiético/Plágio:* Cópia direta de respostas geradas por IA para entrega de trabalhos, substituição da escrita autoral por textos sintetizados e ocultação do uso de ferramentas de IA.
* **Integridade Acadêmica:** Promover a responsabilidade discente na citação e transparência quanto ao uso de algoritmos.

### 📌 Seção 2: Ética, Pirataria e Direitos Autorais na Era Digital
* **Propriedade Intelectual e Reutilização de Código/Mídias:**
  * Alerta sobre a reprodução não autorizada de códigos, artes e assets de jogos (recriação de jogos de navegador sem autorização e violação de direitos de propriedade).
  * O papel do desenvolvedor de ADS na construção de soluções originais e no respeito às licenças de software (Open Source vs. Proprietário).
* **Deepfakes, Mídias Sintéticas e Desinformação:**
  * Como funcionam os geradores de voz, imagem e texto.
  * Metodologias para checar fontes, verificar metadados e identificar notícias/mídias falsas geradas por IA.
  * Responsabilidade ética no compartilhamento de conteúdo digital.

### 📌 Seção 3: Mural Interativo da Comunidade (Módulo Dinâmico)
* **Objetivo:** Estabelecer um canal direto de escuta e participação da comunidade escolar e local.
* **Funcionalidade:**
  * Formulário interativo para envio de relatos, dúvidas sobre uso de IA, casos de plágio/pirataria vivenciados ou opiniões sobre o avanço tecnológico.
  * Exibição pública dos relatos e comentários cadastrados no **Firebase Firestore**, garantindo engajamento dinâmico.

---

## 🛠️ 3. Arquitetura da Solução Tecnológica

Para atender às diretrizes da Etapa 3 do Guia da UNIP (solução tecnológica simples de pequena complexidade), a arquitetura será estruturada da seguinte forma:

1. **Frontend (Templates Flask + Tailwind CSS):**
   * Interface responsiva e acessível para dispositivos móveis e desktops.
   * Páginas: `Página Inicial (Guia)`, `Seção Ética & Direitos Autorais` e `Mural da Comunidade`.
2. **Backend (Python / Flask):**
   * Roteamento HTTP simples (`GET /`, `GET /mural`, `POST /mural`).
   * Tratamento das requisições e sanitização dos campos digitados pelos usuários.
3. **Persistência em Nuvem (Firebase Firestore):**
   * Banco NoSQL leve para armazenar os relatos e comentários do mural com marcação de data/hora (`SERVER_TIMESTAMP`).
4. **Hospedagem (Vercel):**
   * Implantação Serverless contínua integrada ao repositório GitHub.

---

## 📋 4. Roteiro de Conclusão do Projeto (Etapas do Guia UNIP)

| Etapa | Carga Horária | Ação Prática |
| :--- | :---: | :--- |
| **1ª Etapa** | 10h | Contato com a escola pública/instituição parceira para apresentar a ideia do Guia de IA e colher demandas locais. |
| **2ª Etapa** | 10h | Estruturação dos textos educativos das Seções 1 e 2 e detalhamento dos requisitos do Mural Interativo. |
| **3ª Etapa** | 10h | Desenvolvimento do código em Flask, conexão com o Firebase Firestore e publicação na Vercel. |
| **4ª Etapa** | 10h | Apresentação da solução à comunidade escolar/parceira, coleta de depoimentos no mural e validação da utilidade pública. |
| **Etapa Final** | 10h | Coleta de fotos/prints, preenchimento do formulário oficial de comprovação assinado e organização do PDF único para postagem. |

---

## 📁 5. Check-list de Documentação para Envio na UNIP

Para a postagem na Área do Aluno, certifique-se de reunir:
* [ ] **Arquivo 1:** Formulário `01_Atividades De Extensão` assinado pela instituição parceira ou tutor (PDF).
* [ ] **Arquivo 2 (PDF Unificado):**
  * Relatório descritivo da ação realizada.
  * Screenshots do site no ar (Hero section, artigos e Mural de Comentários).
  * Evidências de interação com a comunidade (fotos, prints do formulário preenchido ou lista de contatos).
  * Registros dos depoimentos colhidos no banco do Firebase.
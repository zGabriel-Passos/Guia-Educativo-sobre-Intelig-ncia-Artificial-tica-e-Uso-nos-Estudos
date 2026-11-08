"""Conteúdo das páginas. Edite aqui sem mexer nos templates.
Confira leis e referências em fontes oficiais antes de publicar."""

PAGINAS = {
    "estudos": {
        "titulo": "Uso nos estudos",
        "intro": "A IA pode ajudar a estudar melhor, desde que você continue sendo o autor do seu trabalho.",
        "topicos": [
            ("O que é um LLM", "Modelos de linguagem geram texto prevendo a continuação mais provável. Não \"sabem\" a verdade e podem errar com muita confiança (alucinações). Trate a resposta como ponto de partida, nunca como fonte final."),
            ("IA como tutor complementar", "Use para resumir matérias difíceis, montar mapas mentais, criar simulados e pedir explicações com exemplos. Dica: peça para a IA te fazer perguntas, em vez de só te dar respostas."),
            ("Apoio ou plágio?", "Ético: organizar tópicos, tirar dúvidas, revisar a gramática do seu texto, gerar ideias iniciais. Antiético: copiar a resposta e entregar como sua, trocar sua escrita por texto sintetizado, esconder o uso quando a regra exige declarar, inventar referências."),
            ("Integridade acadêmica", "Confira a regra da sua instituição e do professor. Declare o uso de IA quando necessário, cite o que não é seu e verifique toda referência: a IA pode inventar autores, livros e links. Detectores de IA não são confiáveis; guarde rascunhos e histórico como prova do seu processo."),
            ("Checklist antes de entregar", "Entendo tudo o que escrevi? Está na minha voz? Verifiquei dados e referências? Declarei o uso de IA? Respeitei a regra da disciplina?"),
        ],
        "atencao": "Se você não consegue explicar o trabalho com suas palavras, ele ainda não é seu.",
    },
    "etica-direitos": {
        "titulo": "Ética e direitos autorais",
        "intro": "Acessível não significa livre para usar. Entenda o que a lei e as licenças dizem sobre código, arte e mídia.",
        "topicos": [
            ("Propriedade intelectual", "Textos, imagens, músicas, jogos e códigos têm autoria protegida. No Brasil, a base é a Lei 9.610/1998 (direitos autorais); software tem lei própria, a Lei 9.609/1998."),
            ("Pirataria e seus riscos", "Copiar, distribuir ou usar obras e programas sem autorização pode gerar processos, e cracks, keygens e arquivos \"gratuitos\" ainda trazem risco de malware."),
            ("Reuso de código, arte e assets", "Recriar um jogo de navegador usando código, arte, sons ou nome de outro projeto sem autorização é violação. Ver o código no navegador não é permissão para copiar. Para aprender, estude a ideia e refaça com suas próprias criações."),
            ("Licenças de software", "Proprietária: uso restrito. MIT e Apache 2.0: permissivas, mantendo o aviso de autoria. GPL: derivados mantêm a mesma licença. Creative Commons (BY, NC, ND, SA): leia as condições antes de usar. Domínio público: confirme que a obra realmente está nele."),
            ("Código e texto gerados por IA", "A IA pode reproduzir trechos parecidos com obras de terceiros. Revise e entenda o que foi gerado. O status legal de obras geradas por IA ainda está em debate: consulte a política da sua instituição e das plataformas."),
            ("O papel de quem desenvolve", "Construa soluções originais, respeite licenças, dê crédito e documente as dependências do projeto. Cópia não é portfólio."),
        ],
        "atencao": "Se você não criou e não tem licença, pergunte antes de usar.",
    },
    "desinformacao": {
        "titulo": "Deepfakes e desinformação",
        "intro": "Texto, imagem, voz e vídeo podem ser fabricados com facilidade. O hábito de checar vale mais que o olho clínico.",
        "topicos": [
            ("Como funcionam", "Modelos geram textos convincentes, imagens de pessoas que não existem, clones de voz a partir de poucos segundos de áudio e vídeos com rostos trocados (deepfakes)."),
            ("Riscos reais", "Golpes com voz clonada, montagens íntimas e difamatórias, notícias falsas virais, perfis e documentos falsos."),
            ("Como checar em 6 passos", "1) Pare antes de compartilhar. 2) Veja quem publicou. 3) Procure a notícia em veículos confiáveis. 4) Faça busca reversa da imagem (Google Lens, TinEye). 5) Confira data, local e contexto. 6) Consulte agências de checagem, como Aos Fatos, Lupa e Comprova."),
            ("Metadados ajudam, mas não provam", "Dados embutidos na imagem podem sumir ou ser editados com facilidade. Use como pista, não como prova."),
            ("Sinais de mídia sintética", "Mãos e dentes distorcidos, texto estranho dentro da imagem, sombras e piscar estranhos, voz sem respiração natural. Os modelos melhoram rápido: a ausência desses sinais não prova que o conteúdo é real."),
            ("Se você for vítima", "Guarde provas (prints, links, data e hora) antes de apagar, denuncie na plataforma e procure a polícia. A SaferNet oferece canal de denúncia e orientação."),
        ],
        "atencao": "Chocante, urgente ou bom demais para ser verdade? Verifique antes de repassar.",
    },
    "ciberseguranca": {
        "titulo": "Cibersegurança",
        "intro": "Proteja suas contas e seus dados, inclusive quando conversa com ferramentas de IA.",
        "topicos": [
            ("O que não colocar em chats de IA", "Senhas, tokens e chaves de API, dados bancários, documentos pessoais, dados de saúde, informações de colegas e alunos, e material confidencial da escola ou empresa."),
            ("Contas e senhas", "Use senhas longas e únicas com um gerenciador de senhas, ative a verificação em duas etapas e nunca reutilize a senha do e-mail principal."),
            ("Phishing potencializado por IA", "Mensagens golpistas agora vêm bem escritas: erro de português não é mais bom sinal. Desconfie de urgência, prêmios e links encurtados, e confirme por outro canal."),
            ("Extensões e prompt injection", "Textos escondidos em páginas e arquivos podem tentar manipular uma IA. Instale extensões e plugins só de fontes oficiais e confira as permissões."),
            ("Pirataria e malware", "Cracks e \"mods\" gratuitos são porta de entrada comum para vírus e roubo de dados."),
            ("Privacidade e LGPD", "A Lei 13.709/2018 protege seus dados pessoais: você pode pedir acesso, correção e exclusão. Neste site coletamos o mínimo necessário."),
        ],
        "atencao": "Antes de clicar, instalar ou colar algo num chat, pergunte: isso é seguro e é meu para compartilhar?",
    },
}

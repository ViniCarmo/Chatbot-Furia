
# FURIA CS:GO Chatbot

Um chatbot inteligente para os fãs de CS:GO da FURIA Esports. Ele responde perguntas sobre jogadores, partidas, estatísticas, e muito mais, utilizando uma LLM com a integração da API do Gemini.

### 🚀 Funcionalidades
- **Respostas rápidas e precisas**: O bot responde a perguntas sobre o time de CS:GO da FURIA, suas partidas e jogadores, com base em dados atualizados.
- **Integração com o Gemini**: O chatbot usa a API do Gemini para fornecer respostas baseadas em inteligência artificial, com um modelo generativo para criar conversas mais fluídas.
- **Interatividade**: Você pode interagir com o bot, perguntar sobre estatísticas, eventos e até a história da FURIA no CS:GO.
- **Memória por usuário**: Cada interação é registrada, permitindo um fluxo de conversa contínuo e personalizado.
- **Treinado para responder apenas sobre a FURIA**: O bot é especializado em responder exclusivamente sobre o time FURIA no CS:GO, suas estatísticas, eventos e outros tópicos relacionados.

### 🧠 Tecnologias Utilizadas
- **Backend**: Python com `python-telegram-bot` para integração com o Telegram.
- **Inteligência Artificial**: API do Gemini, configurada para gerar respostas dinâmicas e contextuais.
- **Armazenamento de Dados**: Utiliza um armazenamento local de memória para registrar interações e manter o contexto da conversa.
- **Segurança**: As chaves da API são armazenadas de forma segura, utilizando o `.env` e a biblioteca `python-dotenv`.

### 📁 Estrutura do Projeto
```
furia-chatbot/
├── chatbot.py                 # Lógica do bot, integração com o Telegram e a API do Gemini
├── .env                       # Arquivo para armazenar as chaves de API (seguro e não versionado)
├── requirements.txt           # Dependências do projeto
└── README.md                  # Documentação do projeto
```

### ⚙️ Como Rodar o Projeto Localmente

1. **Clone o repositório**:
   ```
   git clone https://github.com/seu-usuario/furia-chatbot.git
   cd furia-chatbot
   ```

2. **Configuração do ambiente**:
   - Crie um ambiente virtual:
     ```
     python -m venv venv
     source venv/bin/activate  # Linux/macOS
     venv\Scriptsctivate     # Windows
     ```

   - Instale as dependências:
     ```
     pip install -r requirements.txt
     ```

3. **Configuração das APIs**:
   - Crie um arquivo `.env` na raiz do projeto com as suas chaves de API:
     ```
     GEMINI_API_KEY=your-gemini-api-key
     TELEGRAM_BOT_TOKEN=your-telegram-bot-token
     ```

4. **Rodar o bot**:
   - Execute o bot:
     ```
     python chatbot.py
     ```

5. **Interaja com o bot no Telegram**:
   - Abra o Telegram e procure pelo seu bot, iniciando a conversa com `/start`.

### 🧩 Integração com a API do Gemini
A API do Gemini é utilizada para fornecer respostas inteligentes e dinâmicas para os usuários. Com ela, o bot pode gerar respostas detalhadas sobre as estatísticas da FURIA, eventos passados e outros dados em tempo real, com base na conversa.

### 💡 Desafios
- **Manutenção do contexto**: A principal dificuldade foi manter o contexto das conversas ao longo de múltiplas interações, o que foi resolvido com um sistema de memória por usuário.
- **Gerenciamento das chaves de API**: As chaves de API foram cuidadosamente armazenadas de forma segura utilizando o `dotenv` para proteger as informações sensíveis.

import google.generativeai as genai

# Configurar a API
API_KEY = "AIzaSyD0pMM9Q_QtKO9nnN47vi10VSfncB_rZmo"
genai.configure(api_key=API_KEY)

# Criar modelo
model = genai.GenerativeModel("gemini-2.0-flash")

# Prompt base que define o comportamento do bot
prompt_base = (
    "Você é um especialista no time de CS:GO da FURIA Esports. "
    "Responda apenas perguntas relacionadas à equipe, jogadores, campeonatos ou estatísticas da FURIA no CS:GO. "
    "Se a pergunta não for sobre isso, diga educadamente que só pode falar sobre o time de CS:GO da FURIA.\n"
)

# Histórico da conversa
historico_conversa = [{"author": "user", "text": prompt_base}]

def enviar_mensagem(mensagem):
    historico_conversa.append({"author": "user", "text": mensagem})

    # Junta todo o histórico para manter contexto
    contexto = "\n".join([f'{msg["author"]}: {msg["text"]}' for msg in historico_conversa])
    response = model.generate_content(contexto)

    historico_conversa.append({"author": "chatbot", "text": response.text.strip()})

    return response.text.strip()

# Loop de interação
while True:
    texto = input("Você: ")
    if texto.lower() == "sair":
        break
    resposta = enviar_mensagem(texto)
    print("Chatbot:", resposta)

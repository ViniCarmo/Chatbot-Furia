import google.generativeai as genai

API_KEY = "AIzaSyD0pMM9Q_QtKO9nnN47vi10VSfncB_rZmo"

genai.configure(api_key=API_KEY)

model = genai.GenerativeModel("gemini-2.0-flash")

historico_conversa = []

def enviar_mensagem(mensagem):
    historico_conversa.append({"author": "user", "text": mensagem})

    prompt = " ".join([msg["text"] for msg in historico_conversa])
    response = model.generate_content(prompt)

    historico_conversa.append({"author": "chatbot", "text": response.text})

    return response.text

while True: 
    texto = input("Escreva aqui sua mensagem: ")
    if texto.lower() == "sair":
        break
    else:
        resposta = enviar_mensagem(texto)
        print("Chatbot:", resposta)

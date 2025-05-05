from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes
import google.generativeai as genai
from dotenv import load_dotenv
import os

load_dotenv(dotenv_path="key.env")

TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

genai.configure(api_key=GEMINI_API_KEY)
model = genai.GenerativeModel("gemini-2.0-flash")

prompt_base = (
    "Você é um especialista no time de CS:GO da FURIA Esports. "
    "Responda apenas perguntas relacionadas à equipe, jogadores, campeonatos ou estatísticas da FURIA no CS:GO. "
    "Se a pergunta não for sobre isso, diga educadamente que só pode falar sobre o time de CS:GO da FURIA.\n"
)

historico_usuarios = {}

def gerar_resposta(user_id, pergunta):
    
    if user_id not in historico_usuarios:
        historico_usuarios[user_id] = [prompt_base]
    
    historico_usuarios[user_id].append(f"Usuário: {pergunta}")

    contexto = "\n".join(historico_usuarios[user_id])

    resposta = model.generate_content(contexto).text.strip()

    historico_usuarios[user_id].append(f"Bot: {resposta}")

    return resposta

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.message.from_user.id
    historico_usuarios[user_id] = [prompt_base]  # Inicia um novo histórico para o usuário
    await update.message.reply_text("Olá! Sou o bot da FURIA CS:GO. Pergunte algo sobre o time!")

async def responder(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.message.from_user.id
    pergunta = update.message.text
    resposta = gerar_resposta(user_id, pergunta)
    await update.message.reply_text(resposta)

if __name__ == '__main__':
    app = ApplicationBuilder().token(TELEGRAM_BOT_TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, responder))

    print("Bot rodando...")
    app.run_polling()

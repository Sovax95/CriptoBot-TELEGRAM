import os
import requests
import random
from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")
API_URL = f"https://api.telegram.org/bot{BOT_TOKEN}"

RESPOSTAS_ENGRACADAS = [
    "Hmm... interessante 🤔",
    "Você fala e eu escuto, tipo terapeuta digital 😅",
    "Já considerou entrar na política? Isso foi profundo! 🗳️",
    "Repita isso 3 vezes olhando no espelho... ou não 😬"
]

async def process_message(payload):
    if "message" in payload and "text" in payload["message"]:
        chat_id = payload["message"]["chat"]["id"]
        user_text = payload["message"]["text"]

        if user_text.startswith("/"):
            resposta = {
                "/start": "Bem-vindo ao CryptoBot Promoter! 🚀",
                "/help": "Use este bot para interagir com campanhas e receber atualizações.",
                "/sobre": "Sou um bot promotor feito com FastAPI e muito café! ☕"
            }.get(user_text, "Comando não reconhecido 😅")
        else:
            resposta = random.choice(RESPOSTAS_ENGRACADAS) + f" Você disse: {user_text}"

        try:
            requests.post(f"{API_URL}/sendMessage", json={
                "chat_id": chat_id,
                "text": resposta
            })
        except Exception as e:
            print(f"Erro ao enviar mensagem: {e}")
    return {"status": "ok"}

def send_message_manual(data):
    message = data.get("message", "")
    try:
        requests.post(f"{API_URL}/sendMessage", json={
            "chat_id": CHAT_ID,
            "text": message
        })
    except Exception as e:
        print(f"Erro ao enviar mensagem manual: {e}")
    return {"status": "mensagem enviada", "message": message}

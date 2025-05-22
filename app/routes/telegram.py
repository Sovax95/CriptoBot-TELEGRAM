from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from app.services.telegram_bot import process_message, send_message_manual
import os

router = APIRouter()

@router.get("/")
def home():
    return {"message": "CryptoBot Promoter API rodando na nuvem 🚀"}

@router.post("/webhook")
async def webhook(request: Request):
    payload = await request.json()
    return await process_message(payload)

@router.post("/send_message")
async def send_message(request: Request):
    data = await request.json()
    return send_message_manual(data)

@router.get("/painel", response_class=HTMLResponse)
def painel():
    try:
        with open("app/templates/painel.html", "r", encoding="utf-8") as f:
            return f.read()
    except FileNotFoundError:
        return "<h1>Painel não encontrado 😢</h1>"

from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from app.services.telegram_bot import process_message, send_message_manual
import os

router = APIRouter()
templates = Jinja2Templates(directory="app/templates")

@router.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@router.post("/webhook")
async def webhook(request: Request):
    payload = await request.json()
    return await process_message(payload)

@router.post("/send_message")
async def send_message(request: Request):
    data = await request.json()
    return send_message_manual(data)

@router.get("/panel", response_class=HTMLResponse)
def panel():
    try:
        with open("app/templates/panel.html", "r", encoding="utf-8") as f:
            return f.read()
    except FileNotFoundError:
        return "<h1>Panel not found 😬</h1>"

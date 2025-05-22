from fastapi import FastAPI
from app.routes.telegram import router as telegram_router

app = FastAPI()
app.include_router(telegram_router)

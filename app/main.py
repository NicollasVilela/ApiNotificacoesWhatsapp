from fastapi import FastAPI

from app.database.sqlite_connection import criar_tabelas
from app.listeners.database_listener import processar_eventos_pendentes
from app.routes.notifications import router as notifications_router

criar_tabelas()

app = FastAPI(
    title="API de Notificações WhatsApp",
    description="API para monitoramento de eventos e envio automático de notificações.",
    version="1.0.0",
)

app.include_router(notifications_router)


@app.get("/")
def health_check():
    return {"status": "online", "message": "API de notificações funcionando"}


@app.post("/processar-eventos")
def processar_eventos():
    resultado = processar_eventos_pendentes()
    return resultado

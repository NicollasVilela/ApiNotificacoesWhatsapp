import os
import requests
from dotenv import load_dotenv

from app.utils.logger import logger

load_dotenv()

WHATSAPP_API_URL = os.getenv("WHATSAPP_API_URL", "")
WHATSAPP_TOKEN = os.getenv("WHATSAPP_TOKEN", "")


def enviar_mensagem_whatsapp(telefone: str, mensagem: str) -> dict:
    if not WHATSAPP_API_URL or not WHATSAPP_TOKEN:
        logger.info("Envio simulado para %s: %s", telefone, mensagem)
        return {
            "simulado": True,
            "telefone": telefone,
            "mensagem": mensagem,
            "status": "enviado",
        }

    payload = {
        "phone": telefone,
        "message": mensagem,
    }

    headers = {
        "Authorization": f"Bearer {WHATSAPP_TOKEN}",
        "Content-Type": "application/json",
    }

    response = requests.post(
        WHATSAPP_API_URL,
        json=payload,
        headers=headers,
        timeout=15,
    )
    response.raise_for_status()

    return response.json()

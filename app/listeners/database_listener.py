from app.services.notification_service import (
    buscar_eventos_pendentes,
    processar_notificacao,
)
from app.utils.logger import logger


def processar_eventos_pendentes() -> dict:
    eventos = buscar_eventos_pendentes()
    processados = []

    for evento in eventos:
        try:
            processados.append(processar_notificacao(evento))
        except Exception as erro:
            logger.error("Erro ao processar evento %s: %s", evento.get("id"), erro)

    return {
        "quantidade_pendente": len(eventos),
        "quantidade_processada": len(processados),
        "eventos": processados,
    }

from app.database.sqlite_connection import get_connection
from app.services.whatsapp_service import enviar_mensagem_whatsapp
from app.utils.logger import logger


def criar_evento_notificacao(telefone: str, mensagem: str) -> dict:
    with get_connection() as conn:
        cursor = conn.execute(
            "INSERT INTO eventos (telefone, mensagem) VALUES (?, ?)",
            (telefone, mensagem),
        )

        return {
            "id": cursor.lastrowid,
            "telefone": telefone,
            "mensagem": mensagem,
            "processado": False,
        }


def buscar_eventos_pendentes() -> list[dict]:
    with get_connection() as conn:
        rows = conn.execute(
            "SELECT id, telefone, mensagem, processado FROM eventos WHERE processado = 0"
        ).fetchall()

        return [dict(row) for row in rows]


def marcar_evento_como_processado(evento_id: int) -> None:
    with get_connection() as conn:
        conn.execute(
            "UPDATE eventos SET processado = 1 WHERE id = ?",
            (evento_id,),
        )


def processar_notificacao(evento: dict) -> dict:
    logger.info("Processando evento %s", evento["id"])

    retorno = enviar_mensagem_whatsapp(
        telefone=evento["telefone"],
        mensagem=evento["mensagem"],
    )

    marcar_evento_como_processado(evento["id"])

    return {
        "evento_id": evento["id"],
        "status": "processado",
        "retorno": retorno,
    }

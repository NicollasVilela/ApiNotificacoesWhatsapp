from pydantic import BaseModel
from fastapi import APIRouter

from app.services.notification_service import (
    buscar_eventos_pendentes,
    criar_evento_notificacao,
)

router = APIRouter(prefix="/notificacoes", tags=["Notificações"])


class NotificacaoCreate(BaseModel):
    telefone: str
    mensagem: str


@router.post("/")
def criar_notificacao(payload: NotificacaoCreate):
    return criar_evento_notificacao(
        telefone=payload.telefone,
        mensagem=payload.mensagem,
    )


@router.get("/pendentes")
def listar_pendentes():
    return buscar_eventos_pendentes()

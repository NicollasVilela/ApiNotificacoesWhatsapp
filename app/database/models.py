from dataclasses import dataclass


@dataclass
class EventoNotificacao:
    id: int
    telefone: str
    mensagem: str
    processado: int = 0

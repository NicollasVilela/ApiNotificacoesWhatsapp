from collections import deque

fila_notificacoes = deque()


def adicionar_na_fila(evento: dict) -> None:
    fila_notificacoes.append(evento)


def remover_da_fila() -> dict | None:
    if not fila_notificacoes:
        return None

    return fila_notificacoes.popleft()


def tamanho_fila() -> int:
    return len(fila_notificacoes)

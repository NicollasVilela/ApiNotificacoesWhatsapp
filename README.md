# ApiNotificacoesWhatsapp

# API de Notificações com WhatsApp

API REST para monitoramento de eventos em banco de dados e envio automático de notificações via WhatsApp.

## Tecnologias

- Python
- FastAPI
- SQLite
- Requests
- Docker

## Funcionalidades

- Cadastro de eventos pendentes
- Listener para identificar eventos não processados
- Envio simulado de mensagens WhatsApp
- Marcação de eventos como processados
- Logs e tratamento de exceções

## Como executar

```bash
docker build -t api-notificacoes-whatsapp .
docker run -p 8001:8001 api-notificacoes-whatsapp
```

Ou localmente:

```bash
pip install -r requirements.txt
uvicorn app.main:app --reload --port 8001
```

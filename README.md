# Chatbot WhatsAI

Projeto em desenvolvimento de um chatbot para WhatsApp. A aplicacao recebe eventos por webhook e foi estruturada para operar junto da Evolution API, com Redis e PostgreSQL no ambiente Docker.

> Status: incompleto. No estado atual, o webhook recebe a mensagem, identifica conversas diretas ou em grupo e registra informacoes no console. A logica de resposta automatica do chatbot ainda precisa ser implementada.

## Componentes

- **FastAPI**: expoe o endpoint `POST /webhook/`.
- **Evolution API**: faz a integracao com o WhatsApp.
- **Redis**: disponivel para cache e dados de sessao.
- **PostgreSQL**: disponivel para persistencia de dados.
- **Docker Compose**: sobe os servicos em conjunto.

## Pre-requisitos

- Python 3.12 ou superior, para execucao local; ou
- Docker Desktop com Docker Compose, para executar toda a infraestrutura.

## Configuracao

As variaveis de ambiente da Evolution API ficam no arquivo `.env` local. Esse arquivo contem dados sensiveis e nao deve ser versionado.

O arquivo atual usa configuracoes para autenticacao, sessao do WhatsApp, banco de dados e Redis, incluindo variaveis como `AUTHENTICATION_API_KEY`, `CONFIG_SESSION_PHONE_VERSION`, `DATABASE_CONNECTION_URI` e `CACHE_REDIS_URI`.

## Execucao com Docker

Com o `.env` configurado, execute:

```bash
docker compose up --build
```

Servicos e portas expostos pelo ambiente:

| Servico | Porta |
| --- | --- |
| Chatbot / FastAPI | `8000` |
| Evolution API | `8080` |
| PostgreSQL | `5432` |
| Redis | `6379` |

Para interromper os conteineres:

```bash
docker compose down
```

## Execucao local da API

Crie e ative um ambiente virtual, instale as dependencias e inicie o Uvicorn:

```bash
python -m venv .venv
```

No Windows (PowerShell):

```powershell
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
uvicorn app:app --reload --port 8000
```

Em outros sistemas:

```bash
source .venv/bin/activate
pip install -r requirements.txt
uvicorn app:app --reload --port 8000
```

## Webhook

O endpoint disponivel e:

```text
POST http://localhost:8000/webhook/
```

Configure a Evolution API para enviar os eventos recebidos do WhatsApp para esse endereco. Quando os servicos estiverem na mesma rede Docker, use o hostname do servico da aplicacao conforme a configuracao da sua instancia.

## Proximos passos sugeridos

- Validar o formato e a assinatura dos eventos do webhook.
- Implementar a interpretacao de mensagens e a geracao de respostas.
- Enviar respostas pelo endpoint da Evolution API.
- Persistir conversas, usuarios e contexto quando necessario.
- Adicionar testes, tratamento de erros e observabilidade.

## Seguranca

Nao publique o arquivo `.env`, chaves de API, tokens, senhas ou URIs de banco de dados. O arquivo `.gitignore` ja protege arquivos de ambiente, caches do Python, ambientes virtuais, logs e configuracoes locais de IDE.

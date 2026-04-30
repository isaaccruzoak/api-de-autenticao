# API de Autenticação (FastAPI + JWT + PostgreSQL)

Sistema real de autenticação com:
- cadastro
- login
- hash de senha com bcrypt
- access token + refresh token
- proteção de rotas

## Stack
- FastAPI
- SQLAlchemy
- PostgreSQL
- JWT (python-jose)
- Docker / Docker Compose

## Como executar

### Com Docker
```bash
docker compose up --build
```

A API ficará em `http://localhost:8000`.

### Sem Docker
1. Configure um PostgreSQL e as variáveis de ambiente.
2. Instale dependências:
```bash
pip install -r requirements.txt
```
3. Rode:
```bash
uvicorn app.main:app --reload
```

## Endpoints principais
- `POST /auth/register`
- `POST /auth/login`
- `POST /auth/refresh`
- `GET /users/me` (protegida)

## Variáveis de ambiente
Veja `.env.example`.

from fastapi import FastAPI

from .database import Base, engine
from .routers import auth, users

Base.metadata.create_all(bind=engine)

app = FastAPI(title="API de Autenticação")
app.include_router(auth.router)
app.include_router(users.router)


@app.get("/")
def healthcheck():
    return {"status": "ok"}

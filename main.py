from fastapi import FastAPI
import uvicorn

from config import Settings
from db.db import init_db
from routers import auth, quiz

settings = Settings()

async def lifespan(app: FastAPI):
    await init_db()
    yield

app = FastAPI(title=settings.app_name, debug=settings.debug, lifespan=lifespan)

app.include_router(quiz.router)
app.include_router(auth.router)

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=settings.debug)


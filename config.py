from fastapi import FastAPI
from . import models
from .database import engine
from .routers import user, record
from .config import Config

# Ініціалізуємо додаток FastAPI
app = FastAPI()

# Створюємо таблиці в базі даних
models.Base.metadata.create_all(bind=engine)

# Включаємо маршрутизатори
app.include_router(user.router)
app.include_router(record.router)

# Передаємо клас Config об'єкту додатку
app.config = Config()

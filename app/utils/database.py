import os
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv

# Загружаем переменные окружения из .env
load_dotenv()

# Получаем URL базы данных из .env
DATABASE_URL = os.getenv("DATABASE_URL")

# Создаем движок
engine = create_engine(DATABASE_URL)

# Создаем сессию
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Базовая модель
Base = declarative_base()

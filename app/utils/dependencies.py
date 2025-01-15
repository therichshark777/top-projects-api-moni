from .database import SessionLocal

# Зависимость для работы с сессией БД
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

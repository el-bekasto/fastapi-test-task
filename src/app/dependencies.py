from src.db.database import SessionLocal


def get_session():
    """
    Dependency. Нужен чтобы для каждой path-функции автоматически создавалось соединение с БД.
    :return:
    """
    session = SessionLocal()
    try:
        yield session
    finally:
        session.close()

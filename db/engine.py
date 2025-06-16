from datetime import datetime
from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine
from .models import Base

engine = create_async_engine('sqlite+aiosqlite:///car.db')
new_session = async_sessionmaker(engine, expire_on_commit=False)

# Создать таблицы (один раз)
def init_db():
    Base.metadata.create_all(bind=engine)


def get_db():
    db = new_session()
    try:
        yield db
    finally:
        db.close()

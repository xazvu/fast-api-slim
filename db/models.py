from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import String

class Base(DeclarativeBase):
    pass

class Car(Base):
    __tablename__ = "tasks"
    name: Mapped[str] = mapped_column(String(20), unique=True)
    description: Mapped[str] = mapped_column(String(1000))
    color: Mapped[str] = mapped_column(String(20))
    power: Mapped[int]
    price: Mapped[int] = mapped_column()
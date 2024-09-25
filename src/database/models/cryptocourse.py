from sqlalchemy import String, Float, Integer, ForeignKey
from sqlalchemy.orm import mapped_column, Mapped

from .base import Base


class CryptoCourse(Base):
    __tablename__: str = "CryptoCourse"

    ID: Mapped[str] = mapped_column(String(16), primary_key=True)
    ticker: Mapped[str] = mapped_column(ForeignKey("Cryptocurrency.ticker"))
    price: Mapped[float] = mapped_column(Float, default=0)
    type_: Mapped[str] = mapped_column("type", String(8))
    number: Mapped[int] = mapped_column(Integer)

    def __init__(
        self,
        *,
        ID: str,
        ticker: str,
        price: float,
        type_: str,
        number: int,
    ) -> None:
        self.ID = ID
        self.ticker = ticker
        self.price = price
        self.type_ = type_
        self.number = number
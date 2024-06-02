from typing import List
from typing import Optional
from sqlalchemy import ForeignKey
from sqlalchemy import String, Boolean, Integer, MetaData
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship

metadata = MetaData(schema="test_docker")
Base = declarative_base(metadata=metadata)

class User(Base):
    __tablename__ = "user"
    id: Mapped[int] = mapped_column(primary_key=True)
    first_name: Mapped[str] = mapped_column(String(255))
    last_name: Mapped[str] = mapped_column(String(255))
    username: Mapped[str] = mapped_column(String(255))
    email: Mapped[Optional[str]]

    orders: Mapped[List["Order"]] = relationship(back_populates="user")
    def __repr__(self) -> str:
        return f"User(id={self.id!r}, first_name={self.first_name!r}, last_name={self.last_name!r}, username={self.username!r}, email={self.email!r})"

class Item(Base):
    __tablename__ = "item"
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(255))
    price_in_cents: Mapped[int] = mapped_column(Integer)
    available: Mapped[bool] = mapped_column(Boolean, default=True)

    orders: Mapped[List["Order"]] = relationship(back_populates="item")
    def __repr__(self) -> str:
        return f"Item(id={self.id!r}, name={self.name!r}, price_in_cents={self.price_in_cents!r}, available={self.available!r})"
    
class Order(Base):
    __tablename__ = "order"
    id: Mapped[int] = mapped_column(primary_key=True)
    fulfilled: Mapped[bool] = mapped_column(Boolean)
    user_id: Mapped[int] = mapped_column(ForeignKey("user.id"))
    item_id: Mapped[int] = mapped_column(ForeignKey("item.id"))

    user: Mapped["User"] = relationship(
        back_populates="orders", cascade="all, delete-orphan"
    )
    item: Mapped["Item"] = relationship(
        back_populates="orders", cascade="all, delete-orphan"
    )
    
    def __repr__(self) -> str:
        return f"Order(id={self.id!r}, fulfilled={self.fulfilled!r})"
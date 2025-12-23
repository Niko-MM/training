from sqlalchemy import Column, Integer, String, ForeignKey
from db.session import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    nick = Column(String)
    age = Column(Integer)
    balance = Column(Integer, default=0)


class Transaction(Base):
    __tablename__ = "transaction"

    id_transaction = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    transaction_amount = Column(Integer)

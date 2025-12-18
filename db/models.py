from sqlalchemy import Column, Integer, String
from db.session import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    nick = Column(String)
    age = Column(Integer)
    balance = Column(Integer)



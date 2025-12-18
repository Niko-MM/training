from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from db.models import User
from db.session import async_session_maker


async def save_user(session: AsyncSession, user: User):
    session.add(user)
    await session.commit()
    await session.refresh(user)
    return user


async def create_user(nick: str, age: int, balance: int):
    if not nick or age <= 0 or balance < 0:
        raise ValueError("Некорректные данные")

    user = User(nick=nick, age=age, balance=balance)

    async with async_session_maker() as session:
        result =  await save_user(session=session, user=user)
        return result


async def get_all():
    async with async_session_maker() as session:
        result = await session.execute(select(User))
        return list(result.scalars())
    

async def get_user_by_id(id_):
    async with async_session_maker() as session:
        result = await session.execute(select(User).where(User.id == id_))
        user = result.scalar()
        return user

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from db.models import User, Transaction
from db.session import async_session_maker


async def save_user(session: AsyncSession, user: User):
    session.add(user)
    await session.commit()
    await session.refresh(user)
    return user


async def save_transaction(session: AsyncSession, transaction: Transaction):
    session.add(transaction)
    await session.commit()
    await session.refresh(transaction)
    return transaction


async def create_user(nick: str, age: int, balance: int):
    if not nick or age <= 0 or balance < 0:
        raise ValueError("Некорректные данные")

    user = User(nick=nick, age=age, balance=balance)

    async with async_session_maker() as session:
        result = await save_user(session=session, user=user)
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


async def add_transaction(user_id: int, amount: int):
    user = await get_user_by_id(user_id)

    if not user:
        raise ValueError("Пользователь не найден")

    if amount == 0:
        raise ValueError("Сумма не может быть нулевой")

    transaction = Transaction(user_id=user_id, amount=amount)

    async with async_session_maker() as session:
        result = await save_transaction(session, transaction)
        return result

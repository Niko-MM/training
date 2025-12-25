from db.operations import create_user, get_all, get_user_by_id, add_transaction
from db.session import init_db
import asyncio


async def main():
    await init_db()

    print("Рады вас приветствовать!")
    while True:
        print("Выберите функцию: ")
        print(
            "1 - Зарегестрироваться",
            "\n2 - Список пользователей",
            "\n3 - Найти пользователя по id",
            "\n4 - Пополнить счет",
            "\n5 - Выход",
        )
        user_choice = int(input("Выберите функцию: "))

        if user_choice == 5:
            print("До новыз встреч!")
            break

        elif user_choice == 1:
            nick = input("Введите ваш ник: ")
            age = int(input("Введите ваш возраст: "))
            result = await create_user(nick, age)
            print(f"{result.nick} успешно зарегестрированы! Ваш id - {result.id}")

        elif user_choice == 2:
            try:
                users = await get_all()
                if users:
                    for user in users:
                        print(f"{user.nick} - {user.balance}")
                        print("-" * 20)
                else:
                    print("Пользователей не найдено")
            except Exception as e:
                print(f"Ошибка {e}")

        elif user_choice == 3:
            find_id = int(input("Введите id, которое хотите найти: "))
            try:
                user = await get_user_by_id(find_id)
                if user:
                    print(f"Пользователь - {user.nick}")
                else:
                    print(f"Пользователь с id - {find_id} не найден")
            except Exception as e:
                print(f"error {e}")

        elif user_choice == 4:
            user_id = int(input("Введите id пользователя: "))
            transaction_amount = int(input("Введите сумму: "))
            result = await add_transaction(user_id=user_id, transaction_amount=transaction_amount)


if __name__ == "__main__":
    asyncio.run(main())

import requests


# Функция для обновления данных пользователя
def update_user_profile(user_id, name, email):
    url = f"https://jsonplaceholder.typicode.com/users/{user_id}"

    # Данные, которые мы будем отправлять для обновления
    data = {
        "name": name,
        "email": email
    }

    # Выполняем PUT-запрос для обновления данных пользователя
    response = requests.put(url, json=data)

    if response.status_code == 200:
        # Если запрос успешен, выводим обновленные данные
        print("Профиль пользователя обновлен!")
        updated_user = response.json()
        print(f"Обновленные данные:\nИмя: {updated_user['name']}\nEmail: "
              f"{updated_user['email']}")
    else:
        # Если произошла ошибка, выводим код ошибки
        print(f"Ошибка при обновлении данных пользователя. Статус код: "
              f"{response.status_code}")


# Пример вызова функции
update_user_profile(1, "Иван Иванович", "ivanov.ivan@example.com")

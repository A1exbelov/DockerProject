import requests

# URL API для удаления пользователей
base_url = "https://jsonplaceholder.typicode.com/users/"

# Список пользователей для удаления
user_ids_to_delete = [2, 4, 6]

# Отправляем DELETE-запрос для удаления нескольких пользователей
for user_id in user_ids_to_delete:
    url = f"{base_url}{user_id}"
    response = requests.delete(url)

    # Проверяем статус код ответа для каждого запроса
    if response.status_code == 200:
        print(f"Пользователь с ID {user_id} успешно удален!")
    else:
        print(f"Ошибка при удалении пользователя с ID {user_id}: "
              f"{response.status_code}")

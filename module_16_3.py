# Домашнее задание по теме "CRUD Запросы: Get, Post, Put Delete."
from fastapi import FastAPI, Path
from typing import Annotated

app = FastAPI()

users = {'1': 'Имя: Example, возраст: 18'}


@app.get('/users')  # запрос данных о users
async def get_user_page() -> dict:
    return users


@app.post('/user/{username}/{age}')  # добавление в словарь
async def user_register(username: Annotated[str, Path(min_length=5, max_length=20,
                                                  description='Enter username', examples='UrbanUser')],
                    age: Annotated[int, Path(ge=18, le=120, description='Enter age', examples=24)]):
    user_id = str(int(max(users, key=int)) + 1)
    users[user_id] = f'Имя: {username}, возраст: {age}'
    return f'User {user_id} is registered'


@app.put('/user/{user_id}/{username}/{age}')  # обновление в словаре
async def update_user(user_id: int, username: str, age: int) -> str:
    users[user_id] = f'Имя: {username}, возраст: {age}'
    return f'The user {user_id} is registered'


@app.delete('/user/{user_id}')  # удаляет из словаря users по ключу user_id
async def delete_user(user_id: str) -> str:
    users.pop(user_id)
    return f'User {user_id} has been deleted'

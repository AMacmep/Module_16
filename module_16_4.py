from fastapi import FastAPI, Body, HTTPException
from pydantic import BaseModel
from typing import List

app = FastAPI()

users = []

class User(BaseModel):  # Создание класса
    id: int = None
    username: str
    age: int = None

@app.get('/')  # Обработчик для корневого маршрута
async def read_root():
    return {"message": "Welcome to the users API!"}

@app.get('/users')  # Запрос данных, возвращает список users.
async def get_user_page() -> List[User]:
    return users

@app.post('/user/{username}/{age}')  # Добавляет в список users объект User.
async def user_register(username: str, age: int):
    # Создаем нового пользователя и добавляем в список
    new_id = len(users) + 1
    user = User(id=new_id, username=username, age=age)
    users.append(user)
    return user

@app.put('/user/{user_id}/{username}/{age}')  # Обновляет username и age пользователя.
async def update_user(user_id: int, username: str, age: int):
    for edit_user in users:
        if edit_user.id == user_id:
            edit_user.username = username
            edit_user.age = age
            return edit_user
    raise HTTPException(status_code=404, detail='User was not found')

@app.delete('/user/{user_id}')  # Удаляет пользователя.
async def delete_user(user_id: int):
    for ind_del, delete_user in enumerate(users):
        if delete_user.id == user_id:
            removed_user = users.pop(ind_del)
            return removed_user
    raise HTTPException(status_code=404, detail='User was not found')
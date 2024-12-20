# Домашнее задание по теме "Модели данных Pydantic"

from fastapi import FastAPI, Body, HTTPException
from pydantic import BaseModel
from typing import List

app=FastAPI()

users=[]

class User(BaseModel):#Создание класса
    id: int = None
    username: str
    age: int = None

@app.get('/users') #запрос данных возвращает список users.
async def get_user_page() -> List[User]:
    return users

@app.post('/user/{username}/{age}') # Добавляет в список users объект User.
async def user_register(user: User, username: str, age: int):
    len_user = len(users)
    if len_user == 0:
        user.id = 1
    else:
        user.id = users[len_user - 1].id + 1
    user.username = username
    user.age = age
    users.append(user)
    return user

@app.put('/user/{user_id}/{username}/{age}') # Обновляет username и age пользователя, если пользователь с таким user_id есть в списке users и возвращает его.
async def update_user(user_id: int, username: str, age: int, user: str = Body()):
    raise1 = True
    for edit_user in users:
        if edit_user.id == user_id:
            edit_user.username = username
            edit_user.age = age
            return edit_user
    if raise1:
        raise HTTPException(status_code=404, detail='User was not found')

@app.delete('/user/{user_id}') # Удаляет пользователя, если пользователь с таким user_id есть в списке users и возвращает его.
async def delete_user(user_id: int):
    raise2 = True
    ind_del = 0
    for delete_user in users:
        if delete_user.id == user_id:
            users.pop(ind_del)
            return delete_user
        ind_del += 1
    if raise2:
        raise HTTPException(status_code=404, detail='User was not found')
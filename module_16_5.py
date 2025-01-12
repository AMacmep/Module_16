# Домашнее задание по теме "Шаблонизатор Jinja 2."

from fastapi import FastAPI, Request, HTTPException, Path
from fastapi.responses import HTMLResponse
from pydantic import BaseModel
from fastapi.templating import Jinja2Templates
from typing import Annotated, List

app = FastAPI(swagger_ui_parameters={"tryItOutEnabled": True}, debug=True)

templates = Jinja2Templates(directory="templates")

users = []

class User(BaseModel):
    id: int
    username: str
    age: int

@app.get('/', response_class=HTMLResponse)
async def read_root(request: Request):
    return templates.TemplateResponse("users.html", {"request": request, "users_list": users})

@app.get('/users')
async def get_user_page() -> List[User]:
    return users

@app.post('/user/{username}/{age}')
async def user_register(username: Annotated[str, Path(min_length=5, max_length=20,
                                                      description='Enter username', examples='UrbanUser')],
                        age: Annotated[int, Path(ge=18, le=120, description='Enter age', examples=24)]):
    new_id = len(users) + 1
    user = User(id=new_id, username=username, age=age)
    users.append(user)
    return user

@app.get('/user/{user_id}', response_class=HTMLResponse)
async def get_user(user_id: int, request: Request):
    for user in users:
        if user.id == user_id:
            return templates.TemplateResponse("users.html", {"request": request, "user": user})
    raise HTTPException(status_code=404, detail='User not found')

    # Возвращаем шаблон с данными пользователя
    return templates.TemplateResponse("users.html", {"request": request, "user": user})

@app.put('/user/{user_id}/{username}/{age}')
async def update_user(user_id: int = Path(ge=1, le=100, description="Enter User ID", examples=1),
                       username: str = None, age: int = None):
    for edit_user in users:
        if edit_user.id == user_id:
            edit_user.username = username
            edit_user.age = age
            return edit_user
    raise HTTPException(status_code=404, detail='User was not found')

@app.delete('/user/{user_id}')
async def delete_user(user_id: int):
    for ind_del, delete_user in enumerate(users):
        if delete_user.id == user_id:
            removed_user = users.pop(ind_del)
            return removed_user
    raise HTTPException(status_code=404, detail='User was not found')
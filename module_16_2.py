# Домашнее задание по теме "Валидация данных".


from fastapi import FastAPI, Path
from typing import Annotated

app = FastAPI()  # Создаем экземпляр приложения FastAPI


@app.get('/')
async def home_page():
    return {'message': 'Главная страница'}


# Определение базового маршрута
@app.get("/user/admin")
async def root():
    return {"message": "Вы вошли как администратор"}


@app.get('/user/{user_id}')
async def user_login(user_id: int = Path(ge=1, le=100, description="Enter User ID", examples=1)) -> str:
    return f'Вы вошли как пользователь № {user_id}'


@app.get('/user/{username}/{age}')
async def user_page(username: Annotated[str, Path(min_length=5, max_length=20,
                                                  description='Enter username', examples='UrbanUser')],
                    age: Annotated[int, Path(ge=18, le=120, description='Enter age', examples=24)]):
    return f'Информация о пользователе. Имя: {username}, Возраст: {age}'

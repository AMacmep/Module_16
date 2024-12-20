# Домашнее задание по теме "Основы Fast Api и маршрутизация"


from fastapi import FastAPI


app = FastAPI()  # Создаем экземпляр приложения FastAPI

# Определение базового маршрута
@app.get('/user/admin')
async def root():
    return 'Вы вошли как администратор'


@app.get('/user/{user_id}')
async def user_login(user_id: int):
    return f'Вы вошли как пользователь № {user_id}'


@app.get('/user')
async def user_info(username: str, age: int):
    return f'Информация о пользователе. Имя: {username}, Возраст: {age}'


@app.get('/')
async def home_page():
    return 'Главная страница'

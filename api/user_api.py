from fastapi import APIRouter

from api import UserRegistrationValidator
from database.userservice import registration_user_db, get_exact_user_db, get_all_users_db, edit_user_db, check_user_phone_db

user_router = APIRouter(prefix='/users', tags=['Работа с пользователями'])


@user_router.get('/all_users')
async def all_users():
    users = get_all_users_db()
    return users


@user_router.post('/register')
async def register_new_user(data: UserRegistrationValidator):
    new_user_data = data.model_dump()

    checker = check_user_phone_db(data.phone_number)

    if checker:
        result = registration_user_db(**new_user_data)

        return result
    else:
        return 'Пользователь уже имеется!'



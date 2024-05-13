from fastapi import APIRouter

from database.beatservice import order_beat, create_beat, all_beats

Beat_router = APIRouter(prefix='/beats', tags=['Создание битов'])


@Beat_router.post('/create_beat')
async def create_beat_api(title: str, price: int):
    return create_beat(title,  price, )


@Beat_router.post('/order_beat')
async def order_beat(title: str, comment: str, price: int, user_id: int):
    return order_beat(title, comment, price, user_id)


@Beat_router.get('/all_beats')
async def all_beats():
    return all_beats()


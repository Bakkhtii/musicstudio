from fastapi import APIRouter

from database.trackservice import create_track_db

Track_router = APIRouter(prefix='/tracks', tags=['Сведение треков'])


@Track_router.post('/create_track')
async def create_track(time: str, comment: str, price: int, user_id: int):
    return create_track_db(time, comment, price, user_id)

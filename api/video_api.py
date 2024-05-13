from fastapi import APIRouter

from database.videoservice import create_video

video_router = APIRouter(prefix='/videos', tags=['Видео продакшн'])


@video_router.post('/video')
async def create_video_api(time: str, comment: str, price: int, user_id: int):
    return create_video(time, comment, price, user_id)

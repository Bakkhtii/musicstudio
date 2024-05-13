from fastapi import APIRouter

from database.voiceservice import record_voice

voice_router = APIRouter(prefix='/voice', tags=['Запись вокала'])


@voice_router.post('/voice')
async def record_voice_api(time: str, comment: str, price: int, user_id: int):
    return record_voice(time, comment, price, user_id)

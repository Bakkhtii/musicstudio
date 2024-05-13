from fastapi import FastAPI

from api.beat_api import Beat_router
from api.rent_api import Rent_router
from api.track_api import Track_router
from api.user_api import user_router
from api.video_api import video_router
from api.voice_api import voice_router
from database import Base, engine
Base.metadata.create_all(bind=engine)



app = FastAPI(docs_url='/')


app.include_router(user_router)
app.include_router(Beat_router)
app.include_router(Rent_router)
app.include_router(Track_router)
app.include_router(video_router)
app.include_router(voice_router)

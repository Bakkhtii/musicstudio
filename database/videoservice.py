from database import get_db
from database.models import VideoProduction


def create_video(time, comment, price, user_name):
    db = next(get_db())
    new_video = VideoProduction(time=time, comment=comment, price=price, user_name=user_name)
    db.add(new_video)
    db.commit()
    return f'Video production started successfully!'

# Другие функции для работы с видео продакшн могут быть добавлены по мере необходимости

from database import get_db
from database.models import CreateTrack


def create_track_db(time, comment, price, user_name):
    db = next(get_db())
    new_track = CreateTrack(time=time, comment=comment, price=price, user_name=user_name)
    db.add(new_track)
    db.commit()
    return f'Track created successfully!'

# Другие функции для работы со сведением треков могут быть добавлены по мере необходимости

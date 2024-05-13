from database import get_db
from database.models import CreateBeat


def order_beat(title, comment, price, user_id):
    db = next(get_db())
    new_beat = CreateBeat(title=title, comment=comment, price=price, user_name=user_id)
    db.add(new_beat)
    db.commit()
    return f'Success please wait!'


def create_beat(title, price):
    db = next(get_db())
    all_beat = CreateBeat(title=title, price=price)
    db.add(all_beat)
    db.commit()
    return 'Success'


def all_beats():
    db = next(get_db())
    all = db.query(CreateBeat).all()
    return all

# Другие функции для работы с битами могут быть добавлены по мере необходимости

from database import get_db
from database.models import CreateVoice


def record_voice(time, comment, price, user_name):
    db = next(get_db())
    new_voice = CreateVoice(time=time, comment=comment, price=price, user_name=user_name)
    db.add(new_voice)
    db.commit()
    return f'Voice recorded successfully!'

# Другие функции для работы с записью вокала могут быть добавлены по мере необходимости

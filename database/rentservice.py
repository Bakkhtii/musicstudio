from database import get_db
from database.models import RentEquipment


def rent_equipment(title, time, comment, price, user_name):
    db = next(get_db())
    new_rent = RentEquipment(title=title, time=time, comment=comment, price=price, user_name=user_name)
    db.add(new_rent)
    db.commit()
    return f'Equipment rented successfully!'

# Другие функции для работы с арендой оборудования могут быть добавлены по мере необходимости

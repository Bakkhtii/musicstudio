from fastapi import APIRouter

from database.rentservice import rent_equipment

Rent_router = APIRouter(prefix='/rent', tags=['Аренда оборудования'])


@Rent_router.post('/rent_eq')
async def rent_equipment(time: str, comment: str, price: int, user_id: int):
    return rent_equipment(time, comment, price, user_id)


@Rent_router.get('/all_rent')
async def all_rent():
    return all_rent()


@Rent_router.post('/our_rent')
async def our_rent(title: str, comment: str, price: str):
    return our_rent(title, comment, price)
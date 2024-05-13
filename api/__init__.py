from pydantic import BaseModel


# Валидатор для регистрации
class UserRegistrationValidator(BaseModel):
    firstname: str
    email: str
    phone_number: int

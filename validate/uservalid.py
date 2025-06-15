from pydantic import BaseModel

class UserCreate(BaseModel):
    name: str
    email: str
    password: str

class UserRead(UserCreate):
    id: int
    model_config = {
        "from_attributes": True
    }
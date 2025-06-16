from pydantic import BaseModel


class CarCreate(BaseModel):
    id: int
    name: str
    description: str
    color: str
    power: int
    price: int


class ReadCar(CarCreate):
    id: int
    model_config = {
        "from_attributes": True
    }
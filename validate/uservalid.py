from pydantic import BaseModel

#для создания машины
class CarCreate(BaseModel):
    name: str
    description: str
    color: str
    power: int
    price: int
    category_id: int

# для чтения машины
class ReadCar(CarCreate):
    id: int
    model_config = {
        "from_attributes": True
    }

#для котегории

class CreatCategory(BaseModel):
    name: str

class ReadCategory(CreatCategory):
    id: int

    model_config = {
        "from_attributes": True
    }
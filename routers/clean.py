from fastapi import APIRouter, Depends
from pydantic import BaseModel

router = APIRouter(
    prefix="/clean",
    tags=["clean"],
)
# pydantic модель для добавления новой задачи
class Add(BaseModel):
    name: str
    description: str | None = None


# для чтения задач из базы данных
class Read_task(Add):
    id: int
    model_config = {
        "from_attributes": True
    }




@router.post("/")
async def add_task(task: Add = Depends()):
    return {'data': task}
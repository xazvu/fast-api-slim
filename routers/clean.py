from typing import Annotated
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from db import models
from db.models import Car
from db.engine import get_db
from validate import uservalid

router = APIRouter(
    prefix="/main",
    tags=["main"],
)

@router.get("/car", response_model=list[uservalid.ReadCar])
def get_cat(db: Session = Depends(get_db)):
    return db.query(Car).all()


@router.post("/car", response_model=uservalid.CarCreate)
def create_car(car: uservalid.CarCreate, db: Session = Depends(get_db)):
    new_car = models.Car(name=car.name, description=car.description, color=car.color, power=car.power, price=car.price)
    db.add(new_car)
    db.commit()
    db.refresh(new_car)
    return new_car
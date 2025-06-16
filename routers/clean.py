from typing import Annotated
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from db import models
from db.models import Car, Category
from db.engine import get_db
from validate import uservalid

router = APIRouter(
    prefix="/main",
    tags=["main"],
)

# ручки для класса Car
@router.get("/car", response_model=list[uservalid.ReadCar])
def get_cat(db: Session = Depends(get_db)):
    return db.query(Car).all()


@router.post("/car", response_model=uservalid.CarCreate)
def create_car(car: uservalid.CarCreate, db: Session = Depends(get_db)):
    category = db.query(models.Category).filter(models.Category.id == car.category_id).first()
    if not category:
        raise HTTPException(status_code=400, detail="Category not found")

    new_car = models.Car(name=car.name, description=car.description, color=car.color, power=car.power, price=car.price, category_id=car.category_id)
    db.add(new_car)
    db.commit()
    db.refresh(new_car)
    return new_car


# ручки для класса Category
@router.get("/category", response_model=list[uservalid.ReadCategory])
def get_cat(db: Session = Depends(get_db)):
    return db.query(Category).all()



@router.post('/category', response_model=uservalid.CreatCategory)
def create_category(car: uservalid.CreatCategory, db: Session = Depends(get_db)):
    new_category = models.Category(name=car.name)
    db.add(new_category)
    db.commit()
    db.refresh(new_category)
    return new_category


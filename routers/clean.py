from typing import Annotated
from fastapi import APIRouter, Depends, Query, Path
from pydantic import BaseModel, EmailStr
router = APIRouter(
    prefix="/main",
    tags=["main"],
)

class Post(BaseModel):
    id: int
    title: str
    body: str


poster = [
    {'id': 1, 'title': 'News 1', 'body': 'Text 1'},
    {'id': 2, 'title': 'News 2', 'body': 'Text 2'},
    {'id': 3, 'title': 'News 3', 'body': 'Text 3'},
    {'id': 4, 'title': 'News 4', 'body': 'Text 4'}
]

@router.get('/posts')
async def posts() -> list[Post]:
    return [Post(**post) for post in poster]


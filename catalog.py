from fastapi import APIRouter
from typing import Annotated
from annotated_types import Ge

router = APIRouter(prefix='/catalog')

@router.get('/new')
def get_new_cars(price: Annotated[int, Ge(1)]):
    return {
        'price': price
    }
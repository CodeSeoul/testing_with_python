from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from .schemas import NameListSchema, NameReadSchema, NameCreateSchema
from .controllers import get_db_name, list_db_names, create_db_name, get_db_name_by_name
from app.dependencies.database import get_db

router = APIRouter()


@router.get("/", response_model=NameListSchema)
def list_names(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    name_list = list_db_names(db, skip, limit)
    return {'names': name_list}



@router.get("/{name_id}", response_model=NameReadSchema)
def get_name(name_id: int, db: Session = Depends(get_db)):
    name = get_db_name(db, name_id)
    if name is None:
        raise HTTPException(status_code=404, detail='Name not found')
    return name


@router.post("/", response_model=NameReadSchema)
def create_name(name: NameCreateSchema, db: Session = Depends(get_db)):
    db_name = get_db_name_by_name(db, name.name)
    if db_name:
        raise HTTPException(status_code=400, detail='Name already exists')
    return create_db_name(db, name)

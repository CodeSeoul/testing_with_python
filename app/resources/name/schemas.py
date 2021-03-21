from typing import List

from pydantic import BaseModel


class NameCreateSchema(BaseModel):
    name: str

    class Config:
        orm_mode = True


class NameReadSchema(NameCreateSchema):
    id: int

    class Config:
        orm_mode = True


class NameListSchema(BaseModel):
    names: List[NameReadSchema]

    class Config:
        orm_mode = True
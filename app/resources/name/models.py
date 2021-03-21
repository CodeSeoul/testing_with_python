from sqlalchemy import Column, Integer, String

from app.dependencies.database import Base


class Name(Base):
    __tablename__ = 'name'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True)
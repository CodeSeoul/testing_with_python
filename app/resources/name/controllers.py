from sqlalchemy.orm import Session

from . import models, schemas


def get_db_name(db: Session, name_id: int):
    """

    :param db:
    :param name_id:
    :return: models.Name
    """
    return db.query(models.Name).filter(models.Name.id == name_id).first()


def get_db_name_by_name(db: Session, name: str):
    return db.query(models.Name).filter(models.Name.name == name).first()


def list_db_names(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Name).offset(skip).limit(limit).all()


def create_db_name(db: Session, name: schemas.NameCreateSchema):
    db_name = models.Name(name=name.name)
    db.add(db_name)
    db.commit()
    db.refresh(db_name)
    return db_name

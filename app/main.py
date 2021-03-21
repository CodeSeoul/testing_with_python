from fastapi import FastAPI

from .dependencies.database import engine
from .resources.name.routes import router as name_router
from .resources.name import models as name_models

app = FastAPI()
# Create our model tables using SQLAlchemy
name_models.Base.metadata.create_all(bind=engine)

app.include_router(name_router, prefix='/names')

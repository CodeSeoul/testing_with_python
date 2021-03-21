# Testing With Python
This is a basic API we're using for demonstrating Pytest. For the complete version with test, checkout the `tests` branch.

This API is built on FastAPI. The database used is SQLite3. We're using SQLAlchemy as our ORM. Most of this was pulled from [FastAPI docs](https://fastapi.tiangolo.com/tutorial/sql-databases/) with modifications. 

## Setup
Requires Python 3.8 or later
```shell
pip install -r requirements.txt
```

## Running
```shell
uvicorn app.main:app --reload --reload-dir app
```

### Testing
### All Tests
```shell
pytest
```

### Integration Tests
```shell
pytest app/tests/integration
```

### Unit Tests
```shell
pytest app/tests/unit
```

### Code Coverage
```shell
pytest --cov=app
```

## Viewing
Visit http://localhost:8000/docs for viewing and testing with Swagger. Use http://localhost:8000/redoc if you prefer Redoc.

## Configuration
Database uses `test.db` by default. This is configurable using the `SQLALCHEMY_DATABASE_URL` environment variable. See `app/dependencies/database.py` for details.

## About This System
FastAPI is an API system with built-in Swagger/Redoc support and type annotation-based validations.
```
app/
    main.py - Our app entrypoint for uvicorn
    dependencies/
        database.py - Database setup and DI function for retrieving database object
    resources/
        name/
            controllers.py - Logic for doing database operations with the name resource
            models.py - SQLAlchemy models for database operations
            routes.py - Routing functions used by FastAPI for HTTP requests
            schemas.py - I/O Schema models used by FastAPI for validation and documentation
```

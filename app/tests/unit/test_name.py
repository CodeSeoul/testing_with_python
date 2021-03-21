from fastapi import HTTPException
from pytest import fail

from app.resources.name.models import Name
from app.resources.name import routes

def test_get_name_success(monkeypatch, generated_id: int, generated_name_text: str):

    expected_name = Name(id=generated_id, name=generated_name_text)
    def mock_get_db_name(_, name_id):
        assert name_id == generated_id
        return expected_name

    monkeypatch.setattr('app.resources.name.routes.get_db_name', mock_get_db_name)
    result = routes.get_name(generated_id, None)
    assert result == expected_name

def test_get_name_error(monkeypatch, generated_id: int):

    def mock_get_db_name(_, name_id):
        assert name_id == generated_id
        return None

    monkeypatch.setattr('app.resources.name.routes.get_db_name', mock_get_db_name)
    try:
        routes.get_name(generated_id, None)
        fail('get name should have generated a 404 for missing name')
    except HTTPException as e:
        assert e.status_code == 404
        assert e.detail == 'Name not found'

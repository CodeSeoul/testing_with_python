import sqlite3
import os
from random import randint

from fastapi.testclient import TestClient
from pytest import fixture

from app.main import app


@fixture(scope='session')
def client():
    return TestClient(app)


@fixture(scope='session')
def db_con() -> sqlite3.Connection:
    return sqlite3.connect(os.getenv('SQLALCHEMY_DATABASE_URL', './test.db'))


@fixture(scope='session')
def db_cur(db_con: sqlite3.Connection) -> sqlite3.Cursor:
    cur = db_con.cursor()
    try:
        yield cur
    finally:
        db_con.close()


@fixture
def generated_name_text():
    return f'sample name {randint(0, 1000)}'


@fixture
def sample_name(generated_name_text, db_con: sqlite3.Connection, db_cur: sqlite3.Cursor):
    db_cur.execute(f'insert into name(name) values (?)', [generated_name_text])
    insert_id = db_cur.lastrowid
    db_con.commit()
    print(f'insert id: {insert_id}')
    try:
        yield {'id': insert_id, 'name': generated_name_text}
    finally:
        db_cur.execute(f'delete from name where id = ?', [insert_id])
        db_con.commit()


@fixture
def cleanup_name(db_con: sqlite3.Connection, db_cur: sqlite3.Cursor):
    def delete_name(name_id: int):
        db_cur.execute('delete from name where id = ?', [name_id])
        db_con.commit()
    return delete_name

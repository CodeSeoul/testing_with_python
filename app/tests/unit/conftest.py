from random import randint

from pytest import fixture


@fixture
def generated_id() -> int:
    return randint(0, 1000)

@fixture
def generated_name_text():
    return f'sample name {randint(0, 1000)}'

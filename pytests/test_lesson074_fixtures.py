import pytest


@pytest.fixture()
def setup():
    print('I will execute first')
    yield
    print('I will execute last')


def test_fixture_demo(setup):
    print('I will execute inside the fixture_demo')

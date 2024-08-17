import pytest


def test_fixture_demo(setup):
    print('I will execute inside the fixture_demo')


@pytest.mark.usefixtures("setup")
class TestExecution():
    def test_fixture_demo1(self):
        print('I will execute inside the fixture_demo1')

    def test_fixture_demo2(self):
        print('I will execute inside the fixture_demo2')

    def test_fixture_demo3(self):
        print('I will execute inside the fixture_demo3')

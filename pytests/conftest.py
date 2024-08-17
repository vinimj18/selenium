import pytest


@pytest.fixture(scope='class')
def setup():
    print('I will execute first')
    yield
    print('I will execute last')


@pytest.fixture()
def data_load():
    print('Data is being retrieved')
    return ['Vinicius', 'Justen', 'vinimj.lixo18@gmail.com']


@pytest.fixture(params=['Chrome', 'Firefox', 'IE'])
def cross_browser(request):
    return request.param

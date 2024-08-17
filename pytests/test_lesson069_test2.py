import pytest
# test_lesson069_test2.py

# @pytest.mark.smoke


@pytest.mark.xfail
def test_is_equal_to():
    assert 1 + 1 == 1, 'Test failed because 1+1=2'


@pytest.mark.skip
def test_is_it_CreditCard():
    print("Yes it is")


def test_cross_browser(cross_browser):
    print(cross_browser)

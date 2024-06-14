import pytest


def test_firstprogram():
    print("Hello!")


@pytest.mark.smoke
@pytest.mark.xfail
def test_secondCreditCard():
    print("Good Morning")

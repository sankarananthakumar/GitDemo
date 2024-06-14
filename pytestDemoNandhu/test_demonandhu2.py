import pytest


@pytest.mark.smoke
@pytest.mark.skip
def test_firstprogram():
    msg = "Hello!"
    assert msg == "Hello!", "Test failed because strings are not matched"


def test_secondCreditCard():
    a = 4
    b = 6
    assert a + 2 == b, "Test failed"

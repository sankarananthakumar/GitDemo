import pytest


@pytest.fixture(scope="class")
def setup():
    print("I will be Executing first")
    yield
    print("I will Execute last")


@pytest.fixture()
def dataLoad():
    print("User profile Data is created")
    return ["rahul", "Shetty", "RahulShettyAcademy.com"]


@pytest.fixture(params=[("Chrome","Rahul","Shetty"),("FireFox","Shetty"), ("IE","SS")])
def crossBrowser(request):
    return request.param

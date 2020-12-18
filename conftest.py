import pytest


@pytest.fixture(scope="module")
def myfixture():
    print("只在module的一个方法中执行一次")

@pytest.fixture()
def myfunction():
    print("执行测试用例时代替setup")
    yield
    print("执行测试用例时代替teardown")



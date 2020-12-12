import pytest
from pythoncode.calculator import Calculator

class TestCalc:
#self.cal = Calculator()在类下面的方法中都要用到，如果每个方法里面都写入这一句会很麻烦，所以在类的开始只执行一次，然后在方法里面调用即可
    def setup_class(self):
        self.cal = Calculator()
        print("开始计算")
    def teardown_class(self):
        print("结束计算")

    def setup_method(self):
        print("setup:开始执行测试用例")
    def teardown_method(self):
        print("teardown:结束执行测试用例")

    @pytest.mark.parametrize("a,b,expect",[(3,5,8),(-1,-2,-3),(100,300,400)],ids=["interesting","minus","bigint"])
    def test_add(self,a,b,expect):
        assert expect == self.cal.add(a,b)

    @pytest.mark.parametrize("a,b,expect",[(6,3,3),(-8,-2,-6),(300,100,200)],ids=["interesting","minus","bigint"])
    def test_sub(self, a, b, expect):
        assert expect == self.cal.sub(a,b)


    @pytest.mark.parametrize("a,b,expect", [(3,2,6), (-2,-5,10), (100,100,10000)],ids=["interesting", "minus", "bigint"])
    def test_mul(self,a,b,expect):
        assert expect == self.cal.mul(a,b)


    @pytest.mark.parametrize("a,b,expect", [(10,2,5), (-8, -2, 4), (300, 100, 3)],ids=["interesting", "minus", "bigint"])
    def test_div(self,a,b,expect):
        assert expect == self.cal.div(a,b)



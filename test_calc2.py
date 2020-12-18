"""
使用【测试数据的数据驱动】的方法完成加减乘除测试
使用fixture替换setup和teardown
将fixture方法放在conftest.py里面，设置scope=module
修改运行规则，pytest.ini文件
练习2(选做)
控制用例的执行顺序，如：加减乘除
结合allure生成测试结果报告

#执行pytest 592_test.py --alluredir=./result2  把中间文件存储在当前目录下的result2文件中，只是一个临时文件
#     allure serve ./result2可在allure中查看生成的测试报告
#     也可以执行 allure generate ./result2直接在pycharm当前目录下生成allure-report测试报告
#      还可以执行allure generate ./result2 -o report2 将生成的测试报告保存在当前目录下的report2中

"""
import pytest
import yaml
import allure

def get_datas():
    with open("./calc2_data.yml") as f:
        datas = yaml.safe_load(f)
        dataadd = datas["dataadd"]
        datasub = datas["datasub"]
        datamul = datas["datamul"]
        datadiv = datas["datadiv"]
        myids = datas["myids"]
    return [dataadd,datasub,datamul,datadiv,myids]

class Calculator:
    def add(self,a,b):
        return a+b
    def sub(self,a,b):
        return a-b
    def mul(self,a,b):
        return a*b
    def div(self,a,b):
        return a/b

class TestCalc:
#self.cal = Calculator()在类下面的方法中都要用到，如果每个方法里面都写入这一句会很麻烦，所以在类的开始只执行一次，然后在方法里面调用即可
    def setup_class(self):
        self.cal = Calculator()
    def test_module1(self,myfixture):
        assert 1+1 == 2
    def test_module2(self,myfixture):
        assert 1+1 == 2


    @pytest.mark.one
    @pytest.mark.parametrize("a,b,expect",get_datas()[0],ids = get_datas()[4] )
    def test_add(self,a,b,expect,myfunction):
        assert expect == self.cal.add(a,b)


    @pytest.mark.two
    @pytest.mark.parametrize("a,b,expect", get_datas()[1], ids=get_datas()[4])
    def test_sub(self, a, b, expect,myfunction):
        assert expect == self.cal.sub(a,b)


    @pytest.mark.three
    @pytest.mark.parametrize("a,b,expect", get_datas()[2], ids=get_datas()[4])
    def test_mul(self,a,b,expect,myfunction):
        assert expect == self.cal.mul(a,b)


    @pytest.mark.four
    @pytest.mark.parametrize("a,b,expect", get_datas()[3], ids=get_datas()[4])
    def test_div(self,a,b,expect,myfunction):
        assert expect == self.cal.div(a,b)



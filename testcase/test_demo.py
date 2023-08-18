import pytest
import allure
from base.read_data import GetData
from base.api_requests import ApiRequest

testdata = GetData('data', 'demo.yml').get_yaml()
exceldata = GetData('excel_data', 'demo.xlsx').read_excel()
@pytest.mark.parametrize('data', exceldata)
@allure.feature('百度接口测试')
class TestClass():


    @pytest.fixture(scope='class',autouse=True)
    def setup_class(self):
        print('连接数据库')
        yield
        print("关闭数据库")

    # @pytest.mark.smoke

    # @pytest.mark.run(order=1)
    @allure.story("请求接口")
    @allure.title("请求百度状态")
    @allure.description("判断状态是否为'200'")
    def test_01(self, data):
        print("用例id:" + str(data['用例ID']))
        print("用例名称:" + str(data["用例名称"]))
        print("请求方式:" + str(data["请求方式"]))
        print("请求地址:" + str(data["请求地址"]))
        print("响应状态:" + str(data["响应状态"]))
        print("响应数据:"+ str(data["响应数据"]))
        res = ApiRequest().get(url=data['请求地址'])
        print(res.status_code)
        assert res.status_code == data['响应状态'], "判断响应状态是否为200,实际为{}".format(data["响应状态"])
        assert data["响应数据"] in res.text,"判断响应数据是否包含‘百度’"
    # @pytest.mark.skip()
    @allure.story("请求接口")
    @allure.title("请求百度页面元素")
    @allure.description("判断百度页面是否包含'百度'")
    def test_02(self, data):
        res = ApiRequest().get(url=data["请求地址"])
        assert "baidu" in res.text, "判断是否包含baidu字符串"


if __name__ == '__main__':
    pytest.main(["-s", "-v"])

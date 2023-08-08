import pytest

from base.read_data import GetData
from base.api_requests import ApiRequest
class TestClass():
    testdata = GetData('data','demo.yml').get_yaml()
    exceldata = GetData('excel_data','demo.xlsx').read_excel()

    def setup_class(self):
        pass


    def teardown_class(self):
        pass

    @pytest.mark.smoke
    @pytest.mark.parametrize('data',exceldata)
    def test_01(self,data):
        print("用例id:"+str(data['用例ID']))
        print("用例名称:" + str(data["用例名称"]))
        print("请求方式:" + str(data["请求方式"]))
        print("请求地址:" + str(data["请求地址"]))
        print("响应状态:" + str(data["响应状态"]))
        res = ApiRequest().get(url=data['请求地址'])
        print(res.status_code)
        assert res.status_code == data['响应状态']

if __name__ == '__main__':
    pytest.main(["-s","-v"])
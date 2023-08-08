import requests
from base.log import Logger
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)  # 禁用网站的不安全显示

class ApiRequest(object):
    def __init__(self):
        pass

    def get(self, url,parmas=None, headers=None):
        response = requests.get(url)
        return response

    def post(self,url,parmas=None,headers=None):
        response = requests.post(url)
        return response


import subprocess
import pytest
from base.public import publicmethod
if __name__ == '__main__':
    filename = 'test_demo.py'
    testcase = publicmethod().get_path('testcase')
    markcase = '-m' + 'smoke'
    pytest.main(["-s","-v",testcase,
    "--alluredir","report/result", "--junit-xml", "report/result.xml", "--clean-alluredir",
    "--durations=0"])
    subprocess.call('allure generate report/result/ -o report/html --clean',shell = True)


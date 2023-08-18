import xlrd
import xlwt
import yaml
from base.public import publicmethod
from base import log

class GetData():
    def __init__(self,*filename):
        self.file = publicmethod().get_path(*filename)
        self.all_data = None
        self.log = log.Log.logger()

    def get_yaml(self):
        with open(self.file,'r',encoding='utf-8') as f:
            try:
                self.all_data = yaml.safe_load(f)
            except yaml.YAMLError as exc:
                print(exc)
        self.log.info('读取文件数据: \n' + str(self.all_data))
        return self.all_data


    def read_excel(self):
        data = []
        book = xlrd.open_workbook(self.file)
        sheet = book.sheet_by_index(0)
        title = sheet.row_values(0)
        for row in range(1,sheet.nrows):
            row_value = dict(zip(title,sheet.row_values(row)))
            data.append(row_value)
        return data


if __name__ == '__main__':
    g= GetData('excel_data','demo.xlsx')
    print(g.read_excel()[0])






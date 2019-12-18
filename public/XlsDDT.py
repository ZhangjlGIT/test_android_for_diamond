#数据驱动
#使用时，直接调用，比如：
# ex = ExcelUtil()，或自定义参数 ex = ExcelUtil(excel_path=r'test.xls',index=1)
# data = ex.get_data()
# 列表赋值
# for i in range(0, len(data)):
#     print(data[i])
#     a, b = data[i]

import xlrd

class ExcelUtil():
    def __init__(self,excel_path=None,index=None):
        if excel_path == None:
            excel_path = r'file.xls'
        if index == None:
            index = 0
        self.data = xlrd.open_workbook(excel_path)
        self.table = self.data.sheets()[index]
        # 行数
        self.rows = self.table.nrows

    def get_data(self):
        result = []
        for i in range(self.rows):
            col = self.table.row_values(i)
            result.append(col)
        return result


if __name__ == '__main__':
    ex = ExcelUtil()
    print(ex.get_data())



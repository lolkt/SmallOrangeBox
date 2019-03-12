import xlrd
import xlwt


class ExcelXlrd(object):
    def __init__(self, lujing, sheet):
        date = xlrd.open_workbook(lujing)
        self.date = date
        openshell = date.sheets()[sheet]
        self.openshell = openshell

    # 获取sheel的行数
    def row_number(self):
        return self.openshell.nrows

    # 获取sheel的列数
    def col_number(self):
        return self.openshell.ncols

    # 获取sheet中整行的数据(数组)
    def rows(self, hang):
        return self.openshell.row_values(hang)

    # 获取sheet中整列的数据(数组)
    def cols(self, lie):
        return self.openshell.col_values(lie)

    # 获取sheet中第n行n列的数据
    def row_col(self, hang, lie):
        return self.openshell.cell_value(hang, lie)


class ExcelXlwt(object):
    # 新建表
    def __init__(self, sheelname):
        files = xlwt.Workbook(encoding='utf-8')
        self.files = files
        shell = files.add_sheet(sheelname)
        self.shell = shell

    # 设置表格的宽度
    def column_width(self, lie, kuan, biaozun):
        self.shell.col(lie).width = (kuan * biaozun)

    # 添加数据
    def add_to(self, hang, lie, shuju):
        self.shell.write(hang, lie, shuju)

        # 添加表头
    def for_shell(self, header, lie=0):
        for each_header in header:
            self.shell.write(0, lie, each_header)
            lie += 1

    # 保存
    def keep(self, lujing):
        self.files.save(lujing)


if __name__ == '__main__':

    file1 = ExcelXlwt(sheelname="hhh")
    header1 = [u"预期结果", u"实际结果", u"haha", u"heihei"]
    file1.for_shell(header=header1)
    file1.keep("hhh.xls")

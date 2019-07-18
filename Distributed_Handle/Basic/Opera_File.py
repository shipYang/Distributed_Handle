# -*- coding: utf-8 -*-
#!/usr/bin/python3
# @Time    : 2019/7/8 2:54 PM
# @Author  : zhaoyang
# @Site    : 
# @File    : Opera_File.py
# @Software: PyCharm
from Basic.Opera_Path import PATH
from Basic.Opera_Date import get_today

class Opera_File():

    def __init__(self):
        file_name = 'Exchange_Result_{}.log'.format(get_today())
        self.path = PATH('../Data_File/{}'.format(file_name))
        self.f = open(self.path, 'a+')


    def file_object(self):
        try:
            self.f = open(self.path, 'a+')
            return self.f
        except Exception as e:
            print(e)
            return


    def read_from_file(self):
        try:
            lines = self.f.readlines()
            return lines
        except Exception as e:
            print(e)
            return
        finally:
            self.f.close()

    def write_to_file(self,data):
        try:
            self.f.write(data)
            self.f.flush()
        except Exception as e :
            print(e)
            return
        finally:
            pass
            # self.f.close()
















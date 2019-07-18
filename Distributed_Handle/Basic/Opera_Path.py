# -*- coding: utf-8 -*-
#!/usr/bin/python3
# @Time    : 2019/7/8 2:52 PM
# @Author  : zhaoyang
# @Site    : 
# @File    : Opera_Path.py
# @Software: PyCharm

import os
PATH = lambda p: os.path.abspath(
        os.path.join(os.path.dirname(__file__), p)
    )

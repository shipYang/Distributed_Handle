# -*- coding: utf-8 -*-
#!/usr/bin/python3
# @Time    : 2019/7/8 2:56 PM
# @Author  : zhaoyang
# @Site    : 
# @File    : Start_Tasks.py
# @Software: PyCharm
from App.task import func
from concurrent.futures import ThreadPoolExecutor


max=2

with ThreadPoolExecutor(max_workers=max) as e:
    for _ in range(max + 1):
        e.submit(func.delay())



# -*- coding: utf-8 -*-
#!/usr/bin/python3
# @Time    : 2019/7/10 4:11 PM
# @Author  : zhaoyang
# @Site    : 
# @File    : Opera_Asyncio.py
# @Software: PyCharm
import asyncio

class Opera_Asynchronous:

    def __init__(self,func):
        self.func=func

    async def my_func(self):
        f = self.func
        f

    def my_coroutine(self):
        coroutine = self.my_func()
        loop = asyncio.get_event_loop()
        task = loop.create_task(coroutine)
        loop.run_until_complete(task)


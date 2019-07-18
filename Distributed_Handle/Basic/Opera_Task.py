# -*- coding: utf-8 -*-
#!/usr/bin/python3
# @Time    : 2019/7/10 4:29 PM
# @Author  : zhaoyang
# @Site    : 
# @File    : Opera_Task.py
# @Software: PyCharm
from Basic.Opera_Kafka import Opera_Kafka
from Basic.Opera_File import Opera_File
from Basic.Opera_Asyncio import Opera_Asynchronous

class Asyncio_Task:

    def asyncio_task(self):
        bootstrap_servers = ''
        topic_consumer = ''
        topic_producer = ''
        group_id = 'test123'


        ok = Opera_Kafka(bootstrap_servers, topic_consumer, group_id)
        oa = Opera_Asynchronous(ok.poll_persist_msg(topic_producer))
        of = Opera_File()

        oa.my_coroutine()






# -*- coding: utf-8 -*-
#!/usr/bin/python3
# @Time    : 2019/7/8 2:55 PM
# @Author  : zhaoyang
# @Site    : 
# @File    : Opera_Kafka.py
# @Software: PyCharm

from kafka import KafkaProducer
from kafka import KafkaConsumer
from kafka.errors import KafkaError
from Basic.Opera_File import Opera_File
f = Opera_File()
class Opera_Kafka():


    def __init__(self,bootstrap_servers,topic,group_id):
        self.bootstrap_servers=bootstrap_servers
        self.producer = KafkaProducer(bootstrap_servers=[self.bootstrap_servers])
        self.consumer = KafkaConsumer(topic, group_id=group_id, bootstrap_servers=[self.bootstrap_servers],
                                      auto_offset_reset='latest')


    def send_msg(self,topic,msg):
        try:
            self.producer.send(topic, value=msg)
        except KafkaError as e:
            print(e)
            self.producer.close(100)
        finally:
            pass

    def poll_persist_msg(self,topic_producer):
        try:
                # message=self.consumer.poll(timeout_ms=0)
                # print(message)
            for msg in self.consumer:
                 # print(msg)
                 f.write_to_file(str(msg)+'\n')
                 self.send_msg(topic_producer,msg)
        except KafkaError as e:
            print(e)
            self.consumer.close()
        finally:
            pass











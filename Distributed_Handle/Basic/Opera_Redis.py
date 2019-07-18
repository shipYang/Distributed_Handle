# -*- coding: utf-8 -*-
#!/usr/bin/python3
# @Time    : 2019/7/8 2:54 PM
# @Author  : zhaoyang
# @Site    : 
# @File    : Opera_Redis.py
# @Software: PyCharm

import redis

class Opera_Redis():

    def __init__(self,host,port,db):
        self.host=host
        self.port=port
        self.db=db

    def get_host(self):
        return self.host

    def get_port(self):
        return self.port

    def get_db(self):
        return self.db

    def conn_redis(self):
        host=self.get_host()
        port=self.get_port()
        db=self.get_db()

        try:
            pool = redis.ConnectionPool(host, port, db)
            r = redis.Redis(connection_pool=pool)
            return r
        except Exception as e:
            print(e)
            return


    def write_to_redis(self,r,key,value):
        r.set(key,value)



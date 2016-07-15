#!/usr/bin/env python3
# -*- coding:utf-8 -*-
__author__ = 'wjq'

import redis
import multiprocessing
from methods.InfoModel import *

class RedisInfo():

    def __init__(self , host , port , db):
        self.host = host
        self.port = port
        self.db = db
        self.redisPool = redis.ConnectionPool(max_connections=2 , host=host , port=port , db=db)


    def getInfo(self):
        rdb = redis.Redis(connection_pool=self.redisPool)
        return rdb.info(section='memory')

    def save(self):
        Info.create(date= datetime.datetime.now() , info=self.getInfo() , rhost=self.host , rport=self.port , rdb=self.db)

if __name__ == '__main__':
    monitor = RedisInfo('10.103.28.103' , 6379 , 0 )
    info = monitor.getInfo()
    print(info)
    monitor.save()

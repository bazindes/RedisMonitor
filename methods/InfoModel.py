#! /usr/bin/env python3
# -*- coding:utf-8 -*-
__author__ = 'wjq'

from peewee import *
from playhouse.db_url import connect
import datetime
import json
import bson
db = connect('mysql://root:123456@localhost:3306/cms_dev')

class Info(Model):
    id = PrimaryKeyField()
    rhost = CharField()
    rport = IntegerField()
    rdb = IntegerField()
    date = DateTimeField()
    info = CharField()
    class Meta:
        database = db

    def __repr__(self):
        return json.dumps(self.__dict__ , cls=DatetimeEncoder)
        # return '{\'id\': %d , \'rhost\': \'%s\' , \'rport\': %d , \'rdb\': %d , \'date\': \'%s\' , \'info\': %s}' % (self.id , self.rhost , self.rport , self.rdb , self.date , self.info)
    def __str__(self):
        return '{id:%d , rhost:%s , rport:%d , rdb:%d , date:%s , info:%s }' % (self.id , self.rhost , self.rport , self.rdb , self.date , self.info)

class JsonInfo():
    def __init__(self , id ,date ,  used_memory  , used_memory_human  , used_memory_rss  , used_memory_peak  , used_memory_peak_human , mem_fragmentation_ratio  ):
        self.id =id
        self.date = date
        self.used_memory = used_memory
        self.used_memory_human = used_memory_human
        self.used_memory_rss = used_memory_rss
        self.used_memory_peak = used_memory_peak
        self.used_memory_peak_human = used_memory_peak_human
        self.mem_fragmentation_ratio = mem_fragmentation_ratio
    def __repr__(self):
        return json.dumps(self.__dict__ , cls=DatetimeEncoder)

class DatetimeEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, datetime.datetime):
            return obj.strftime('%Y-%m-%dT%H:%M:%SZ')
        elif isinstance(obj, datetime.date):
            return obj.strftime('%Y-%m-%d')
        elif isinstance(obj, set):
            return list(obj)
        # Let the base class default method raise the TypeError
        return json.JSONEncoder.default(self, obj)

if __name__ == '__main__':
    Info.create(date=datetime.datetime.now() , info='{test:1234}' , rhost='10.100.14.93' , rport=6379 , rdb=0)


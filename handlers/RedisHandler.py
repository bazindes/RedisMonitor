#! /usr/bin/env python3
# coding:utf-8
__author__ = 'wjq'

import tornado.web
from methods.RedisInfo import *

class RedisHandler(tornado.web.RequestHandler):
    def get(self):
        host = self.get_argument('host')
        port = self.get_argument('port')
        date = self.get_argument('date')
        dateLast = self.get_argument('date_last')

        infos = Info.select().where(Info.rhost == host , Info.rport == port , date < Info.date < dateLast).execute()
        result = []

        for info in infos:
            i = info.info.replace('{' , '').replace('}' , '').split(',')
            used_memory = None
            used_memory_human = None
            used_memory_rss = None
            used_memory_peak = None
            used_memory_peak_human = None
            mem_fragmentation_ratio = None
            for k in i:
                j = k.lstrip().rstrip().split(':')
                j[0] = j[0].lstrip().rstrip().replace('\'', '')
                j[1] = j[1].lstrip().rstrip().replace('\'', '')
                if j[0] == 'used_memory':
                    used_memory = int(j[1])
                if j[0] == 'used_memory_human':
                    used_memory_human = j[1]
                if j[0] == 'used_memory_rss':
                    used_memory_rss = int(j[1])
                if j[0] == 'used_memory_peak':
                    used_memory_peak = int(j[1])
                if j[0] == 'used_memory_peak_human':
                    used_memory_peak_human = j[1]
                if j[0] == 'mem_fragmentation_ratio':
                    mem_fragmentation_ratio = float(j[1])

            result.append(
                JsonInfo(info.id ,
                         info.date ,
                         used_memory ,
                         used_memory_human ,
                         used_memory_rss ,
                         used_memory_peak ,
                         used_memory_peak_human ,
                         mem_fragmentation_ratio
                         )
            )

        self.write(str(result))

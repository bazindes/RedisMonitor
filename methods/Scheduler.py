#! /usr/bin/env python3
# -*- coding:utf-8 -*-
__author__ = 'wjq'

from apscheduler.schedulers.blocking import BlockingScheduler
from methods.RedisInfo import *
import multiprocessing

def start():
    scheduler = BlockingScheduler()
    scheduler.add_job(monitor , 'interval', seconds=60)
    scheduler.start()

def task(host , port):
    monitor = RedisInfo(host , port , 0 )
    monitor.save()

def monitor():
    try:
        pool = multiprocessing.Pool()
        with open('./redis.properties') as f:
            for line in f.readlines():
                if line.startswith('#'):
                    continue
                sever = line.split(' ')
                pool.apply_async(task , args=(sever[0] , sever[1]))
        pool.close()
        pool.join()
    except Exception as e:
        print(e)

if __name__ == '__main__':
    start()
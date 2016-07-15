#!/usr/bin/env python
# coding=utf-8
"""
the url structure of website
"""

from handlers.index import IndexHandler
from handlers.RedisHandler import RedisHandler

url = [
    (r'/', IndexHandler),
    (r'/redis', RedisHandler),
]
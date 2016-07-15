#!/usr/bin/env python3
# coding:utf-8
__author__ = 'wjq'

import tornado.web

class IndexHandler(tornado.web.RequestHandler):
    def get(self):
        self.render('index.html')

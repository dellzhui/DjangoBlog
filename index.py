#!/usr/bin/env python
# coding=utf-8

import logging
import sys
import os
import shutil
import imp

code_path = '/tmp/jang_2_1_blog_code'

def init_code():
    if os.path.exists(code_path):
        shutil.rmtree(code_path)
    shutil.copytree(os.getcwd(), code_path)
    sys.path.insert(0, code_path)
    os.chdir(code_path)
    print(os.listdir(code_path))

def exec_handler(environ, start_response):
    os.chdir(code_path)
    desc = None
    fn, modulePath, desc = imp.find_module('main')
    mod = imp.load_module('main', fn, modulePath, desc)
    request_handler = getattr(mod, 'handler')
    return request_handler(environ, start_response)

def initializer(context):
    init_code()

def handler(environ, start_response):
    # context = environ['fc.context']
    # request_uri = environ['fc.request_uri']
    # for k, v in environ.items():
    #   if k.startswith("HTTP_"):
    #     # process custom request headers
    #     pass
    # # do something here
    # status = '200 OK'
    # response_headers = [('Content-type', 'text/plain')]
    # start_response(status, response_headers)
    # return [HELLO_WORLD]
    return exec_handler(environ, start_response)

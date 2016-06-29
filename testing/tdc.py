#!/usr/bin/env python
# -*- coding: utf-8 -*-
# import init

import socket
import time
import os
import logging
import sys

vpath = sys.path[0]
sys.path.insert(0, vpath + '/../class')
sys.path.insert(1, vpath + '/../support')
sys.path.insert(2, vpath + '/../testing')
sys.path.insert(3, vpath + '/../html')

from generic import *
from class_site import *

try:
    from bs4 import BeautifulSoup
except ImportError, e:
    raise(e)

socket.setdefaulttimeout(30)

def __run__(params):
    url = { 'main_site': 'file://' + sys.path[3] +'/index.html'}
    site = Site(imprimirTela)
    try:
        site.open_site(url)
        site.input_name('Robson')
        site.choice_gender('male')
        site.click_bike()
        site.input_user_name('Robson Agapito')
        site.input_age('18')
        site.click_ok()
        site.verify_message_ok('Cadastro realizado com sucesso!')
    except Exception, e:
        add_error("CRITICAL: %s" % repr(e))
    print_result(array_error)    

print ""
ret = __run__('s')
print ""

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
from class_checkout import *

try:
    from bs4 import BeautifulSoup
except ImportError, e:
    raise(e)

socket.setdefaulttimeout(30)

imprimirTela = True

def __run__(params):


    username = 'mfsys2'
    password = 'LK5hv@4KUY'
    url = { 'main_site': 'file://' + sys.path[3] +'/index.html'}
    site = Site(imprimirTela)
  
    try:
        site.open_site(url)
        site.input_name('Robson')
        site.choice_gender('male')
        site.click_bike()
        site.input_user_name('Robson Agapito')
        site.input_age('18')
        site.click_send()
        site.verify_message()
    except Exception, e:
        add_error("CRITICAL: %s" % repr(e))

    if len(array_error) > 0:
        print_screen ("ERROR: " + array_error[0], imprimirTela)
        return [2,array_error[0]]
    else:
        print_screen ("MONITORACAO PASSOU COM SUCESSO!",imprimirTela)
    

ret = __run__('s')

print ret

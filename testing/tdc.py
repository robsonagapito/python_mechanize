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
#sys.path.insert(2, vpath + '/../testing')
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
    url = { 'main_site': 'file:///Users/robson/workspace/tdc_trilha_python_2016/html/index.html'}
    site = Site(imprimirTela)
  
    try:
        site.open_site(url)
        site.input_name('Robson')
        site.choice_genre('male')
    except Exception, e:
        add_error("CRITICAL: %s" % repr(e))

    if len(array_error) > 0:
        print_screen ("ERROR: " + array_error[0], imprimirTela)
        return [2,array_error[0]]
        #, perfdata(stime)]
    else:
        print_screen ("MONITORACAO PASSOU COM SUCESSO!",imprimirTela)
    
#stime = time.time()
#start_time = stime

ret = __run__('s')

print ret

#final_time = time.time()
#print_screen (start_time,imprimirTela)
#print_screen (final_time,imprimirTela)
#res_time = final_time - start_time
#print_screen (res_time,imprimirTela)
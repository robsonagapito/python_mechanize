#!/usr/bin/env python
# -*- coding: utf-8 -*-

import socket
import time
import os
import logging
import sys

vpath = os.path.abspath(".")
sys.path.insert(1, vpath + '/html')

from support.generic import *
from classes.newsite import *
from classes.cadastrook import *

try:
    from bs4 import BeautifulSoup
except ImportError, e:
    raise(e)

socket.setdefaulttimeout(30)

def __run__(params):
    #prepare
    url = { 'main_site': 'file://' + sys.path[1] +'/index.html'}
    site = NewSite(imprimirTela)
    cadastrook = CadastroOk(imprimirTela)
    #execution
    site.open_site(url)
    site.input_name('Robson')
    site.choice_gender('male')
    site.click_bike()
    site.input_user_name('Robson Agapito')
    site.input_age('18')
    ret = site.click_ok()
    message = cadastrook.message_ok(ret)
    #finalization
    print_result(array_error)    

print ""
ret = __run__('s')
print ""

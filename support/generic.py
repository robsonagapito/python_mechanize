#!/usr/bin/env python
# -*- coding: utf-8 -*-
import time
import mechanize
import types
from bs4 import BeautifulSoup

br = mechanize.Browser()
br.set_handle_robots(False)
array_error = []

def add_error(text):
    array_error.append(text)    

def show_pass(text,vimp = False):
    if vimp:
        print "  => " + text

def htmlParse(data, element, attr, attr_name):
    soup = BeautifulSoup(data)
    if (attr != ''):
        result = soup.findAll(element, attrs={attr: attr_name})
    else:
        result = soup.findAll(element)
    if not isinstance(result, types.NoneType):
        return result

def perfdata(stime):
    diff = round(time.time() - stime, 2)
    return 'exec_time=%.2f' % float(diff)

def print_screen(vtext, vimp = False):
    if vimp:
        print vtext

def return_element_string(data, element, attr, attr_name):
    soup = BeautifulSoup(data)
    result = soup.findAll(element, attrs={attr : attr_name})
    res = result[0].string
    res = res.strip()
    return res.decode("utf8")


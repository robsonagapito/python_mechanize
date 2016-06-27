#import logging
# -*- coding: utf-8 -*-

from generic import *

class Site:
    print_attr = False

    def __init__(self, vimprime):
        self.print_attr = vimprime

    def open_site( self, parUrl ):
        try:
            show_pass("Open site", self.print_attr)
            br.open(parUrl['main_site'])
        except Exception, e:
            #logging.exception(e)
            add_error("CRITICAL: Cannot open page => %s" % repr(e))

    def input_name(self, parValue):
        try:
            show_pass("Input name", self.print_attr)
            br.select_form('form1')
            br.form['firstname'] = parValue
        except Exception, e:
            add_error("CRITICAL: Cannot input name => %s" % repr(e))

    def choice_genre(self, parValue):
        try:
            show_pass("Choice genre", self.print_attr)
            br.select_form('form1')
            br.form.radio.first.check
        except Exception, e:
            add_error("CRITICAL: Cannot choice genre => %s" % repr(e))

    def click_bike(self, parValue):
        try:
            show_pass("Click bike", self.print_attr)
        except Exception, e:
            add_error("CRITICAL: Cannot click bike")

    def click_car(self, parValue):
        try:
            show_pass("Click car", self.print_attr)
        except Exception, e:
            add_error("CRITICAL: Cannot click car")

    def input_user_name(self, parValue):
        try:
            show_pass("Input user name", self.print_attr)
        except Exception, e:
            add_error("CRITICAL: Cannot input user name")

    def input_age(self, parValue):
        try:
            show_pass("Input age", self.print_attr)
        except Exception, e:
            add_error("CRITICAL: Cannot input age")

    def click_send():
        try:
            show_pass("Click send", self.print_attr)
        except Exception, e:
            add_error("CRITICAL: Cannot click send")

    def verify_message(self, parValue):
        try:
            show_pass("Click send", self.print_attr)

        except Exception, e:
            add_error("CRITICAL: Cannot verify message")
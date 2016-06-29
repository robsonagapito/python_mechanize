# -*- coding: utf-8 -*-

from generic import *

class Site:
    print_attr = False
    response = ''

    def __init__(self, vimprime):
        self.print_attr = vimprime

    def open_site( self, parUrl ):
        try:
            show_pass("Open site", self.print_attr)
            br.open(parUrl['main_site'])
        except Exception, e:
            add_error("CRITICAL: Cannot open page => %s" % repr(e))

    def input_name(self, parValue):
        try:
            show_pass("Input name", self.print_attr)
            br.select_form('form1')
            br.form['firstname'] = parValue
        except Exception, e:
            add_error("CRITICAL: Cannot input name => %s" % repr(e))

    def choice_gender(self, parValue):
        try:
            show_pass("Choice gender", self.print_attr)
            br.select_form('form1')
            br.form['gender'] = [parValue]
            
        except Exception, e:
            add_error("CRITICAL: Cannot choice gender => %s" % repr(e))

    def click_bike(self):
        try:
            show_pass("Click bike", self.print_attr)
            br.find_control("bike").items[0].selected=True
        except Exception, e:
            add_error("CRITICAL: Cannot click bike")

    def click_car(self, parValue):
        try:
            show_pass("Click car", self.print_attr)
            br.find_control("car").items[0].selected=True

        except Exception, e:
            add_error("CRITICAL: Cannot click car => %s" % repr(e))

    def input_user_name(self, parValue):
        try:
            show_pass("Input user name", self.print_attr)
            br.select_form('form1')
            br.form['user'] = parValue

        except Exception, e:
            add_error("CRITICAL: Cannot input user name => %s" % repr(e))

    def input_age(self, parValue):
        try:
            show_pass("Input age", self.print_attr)
            br.select_form('form1')
            br.form['idade'] = parValue            
        except Exception, e:
            add_error("CRITICAL: Cannot input age => %s" % repr(e))

    # def click_save(self):
    #     try:
    #         show_pass("Click save", self.print_attr)
    #         br.select_form('form1')
    #         self.reponse = br.submit()          
    #     except Exception, e:
    #         add_error("CRITICAL: Cannot click send => %s" % repr(e))

    def click_ok(self):
        try:
            show_pass("Click OK", self.print_attr)
            br.select_form('form1')
            br.submit()
        except Exception, e:
            add_error("CRITICAL: Cannot click OK => %s" % repr(e))

    # def verify_message_save(self, parValue):
    #     try:
    #         show_pass("Verify message Save", self.print_attr)
    #         compare(text_id(self.response, 'lblresposta'), parValue)
    #     except Exception, e:
    #         add_error("CRITICAL: Cannot verify message => %s" % repr(e))

    def verify_message_ok(self, parValue):
        try:
            show_pass("Verify message Ok", self.print_attr)
            compare(text_id(br.response().read(), 'body'), parValue)
        except Exception, e:
            add_error("CRITICAL: Cannot verify message => %s" % repr(e))            
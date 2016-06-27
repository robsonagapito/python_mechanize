#!/usr/bin/env python
# -*- coding: utf-8 -*-
from generic import *
import logging
import re
import sys
import types
import mechanize

class Checkout:
    print_attr = False
    
    def __init__(self, vimprime):
        self.print_attr = vimprime

    def open_page(self,url):
        try:
            show_pass("Open page Checkout",self.print_attr)
            br.open(url['checkout'])
            return br
        except Exception, e:
            #logging.exception(e)
            add_error("CRITICAL: Cannot open the Checkout page")
            #return [2, "CRITICAL: Cannot open the Checkout page", perfdata(stime)]

    def login_user(self, url, user, passw):
        try:
            show_pass("Login user",self.print_attr)
            for form in br.forms():
                if form.attrs['id'] == 'form_existent':
                    br.form = form
                    control = form.find_control("login_modal")
                    control.value = user
                    br.open(url['checkout_check_user'])
                    if not 'Migrado' in br.response().get_data():
                        add_error("CRITICAL: Error redirecting to login page")
                        #return [2, "CRITICAL: Error redirecting to login page", perfdata(stime)]
                    br.open(url['checkout_login'])
                    br.form = [ form for form in br.forms() if form ][0]
                    control = form.find_control("Login")
                    if control.value != 'mfsys2':
                        add_error("CRITICAL: User is not mfsys2")
                        #return [2, "CRITICAL: User is not mfsys2", perfdata(stime)]
                    br['Password'] = passw
                    response = br.submit()
                    return response
        except Exception, e:
            #logging.exception(e)
            add_error("CRITICAL: Cannot complete the form data for Checkout Page")
            #return [2, "CRITICAL: Cannot complete the form data for Checkout Page", perfdata(stime)]

    def is_sblock_form(self, vname):
        return "id" in self.attrs and self.attrs['id'] == vname

    def login_user_2(self, br, url, user, passw):
        try:
            show_pass("Login user",self.print_attr)
            br.select_form(nr = 1)
            br.form['login_modal'] = user
            br.submit()
            br.open(url['checkout_login'])
            br.select_form(nr = 0)
            br.form['Password'] = passw    
            response = br.submit()
            return response
        except Exception, e:
            #logging.exception(e)
            add_error("CRITICAL: Cannot complete the form data for Checkout Page")
            #return [2, "CRITICAL: Cannot complete the form data for Checkout Page", perfdata(stime)]

    def verify_order_review(self, response, vlr, title, period, product):  
        try:  
            show_pass("Verify order review",self.print_attr)

            vtitle = return_element_string(response.get_data(), 'h2', 'class', 'title')
            if vtitle != title:
                add_error("CRITICAL: " + vtitle + " is not title on order review. (Expected: " + title + ")")  

            vproduct = return_element_string(response.get_data(), 'td', 'class', 'product')  
            if product not in vproduct:
                add_error("CRITICAL: " + vproduct + " is not on product list. (Expected: " + product + ")")  
            
            vperiod = return_element_string(response.get_data(), 'label', 'class', 'periodicity_name')  
            if vperiod != period:
                add_error("CRITICAL: " + vperiod + " is not periodicity on product list. (Expected: " + period + ")")  

            vvlr = return_element_string(response.get_data(), 'td', 'class', 'value last')  
            if vvlr != vlr:
                add_error("CRITICAL: " + vvlr + " is not value on product list. (Expected: " + vlr + ")")  

            br.select_form(nr = 0)
            response = br.submit()
            return response
        except Exception, e:
            #logging.exception(e)
            add_error("CRITICAL: Cannot complete the form data for Checkout Page")

    def verify_payment(self, response, symb, vlr, pay):
        try: 
            show_pass("Verify payment",self.print_attr)

            vsymb = return_element_string(response.get_data(), 'span', 'class', 'symbol')  
            if vsymb != symb:
                add_error("CRITICAL: " + vsymb + " is not symbol on payment. (Expected: " + symb + ")")  
            
            vvlr = htmlParse(response.get_data(), 'td', 'class', 'value last')[0].text.strip()
            if not vlr in vvlr:
                add_error("CRITICAL: " + vvlr + " is not value on payment. (Expected: " + vlr + ")")  
            
            #vpay = return_element_string(response.get_data(), 'strong', 'class', 'name')  
            vpay = htmlParse(response.get_data(), 'strong', 'class', 'name')[0].text.strip()
            if pay != vpay.encode(encoding='UTF-8',errors='strict'):
                add_error("CRITICAL: " + vpay + " is not payment form on payment. (Expected: " + pay + ")") 
        
        except Exception, e:
            #logging.exception(e)
            add_error("CRITICAL: Cannot complete the form payment for Checkout Page")


    def verify_payment_links(self, br, links):
        show_pass("Verify payment links",self.print_attr)

        linksChecked = 0
        for link in br.links():
            for lnk in links:
                if lnk == link.url:
                    linksChecked = linksChecked+1

        if linksChecked < links.__len__():
            add_error("CRITICAL: Could not find all links on payment page")
            #return [2, "CRITICAL: Could not find all links on payment page", perfdata(stime)]

    def verify_payment_ip(self):
        show_pass("Verify payment IP",self.print_attr)
        data = htmlParse(br.response().get_data(), 'fieldset', 'class', 'contracts')[0]
        r = re.compile(r'(?P<ip>\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})')
        ipaddress = r.search(data.cite.strong.text.strip()).group('ip')
        if not ipaddress:
            add_error("CRITICAL: The IP Address information does not exist on payment page")
            #return [2, "CRITICAL: The IP Address information does not exist on payment page", perfdata(stime)]


    def payment_continue(self):
        try:
            show_pass("Payment continue",self.print_attr)
            br.form = [ form for form in br.forms() if form ][0]
            br.submit().read()
        except Exception, e:
            #logging.exception(e)
            add_error("CRITICAL: Cannot complete the payment")
            #return [2, "CRITICAL: Cannot complete the payment", perfdata(stime)]

    def print_boleto(self):
        try:
            show_pass("Print boleto",self.print_attr)
            response = br.follow_link(text_regex=r'Imprimir boleto', nr=0)
            return response
        except Exception, e:
            #logging.exception(e)
            add_error("CRITICAL: Cannot open the boleto page")
            #return [2, "CRITICAL: Cannot open the boleto page", perfdata(stime)]

    def verify_boleto(self, response, vlr, cep):
        try:
            show_pass("Verify boleto",self.print_attr)
            result = htmlParse(response.get_data(), 'div', 'class', 'valor item')[0]
            if not vlr in str(result):
                add_error("CRITICAL: Could not find " + vlr + " on boleto's Valor documento field")
                #return [2, "CRITICAL: Could not find 538,92 on boleto's Valor documento field", perfdata(stime)]
            result = htmlParse(response.get_data(), 'div', 'id', 'colunadireita')[0]
            result = str(result).split('Valor do documento')[1].split('div')[0]
            if not vlr in result:
                add_error("CRITICAL: Could not find "+ vlr + " on boleto's column's Valor documento field")
                #return [2, "CRITICAL: Could not find 538,92 on boleto's column's Valor documento field", perfdata(stime)]
            result = htmlParse(br.response().get_data(), 'div', 'id', 'sacado')[0].text.strip().encode('utf-8')
            r = re.compile(r'(.*) - (?P<postal_code>\d{5}-\d{3}) - (.*)')
            postal_code = [ r.search(line).group('postal_code') for line in result.split('\n') if not isinstance(r.search(line), types.NoneType) ][0]
            if postal_code != cep:
                add_error("CRITICAL: CEP " + cep + " does not exist on boleto page")
                #return [2, "CRITICAL: CEP 05707-000 does not exist on boleto page", perfdata(stime)]
            result = str(htmlParse(response.get_data(), 'img', '', '')[2])
            if not 'barcode' in result:
                add_error("CRITICAL: Barcode does not exist on boleto page")
                #return [2, "CRITICAL: Barcode does not exist on boleto page", perfdata(stime)]
        except Exception, e:
            #logging.exception(e)
            add_error("CRITICAL: Cannot validate all fields from boleto page")
            #return [2, "CRITICAL: Cannot validate all fields from boleto page", perfdata(stime)] 

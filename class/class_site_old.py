from generic import *
import logging
# -*- coding: utf-8 -*-

class Site:
    print_attr = False

    def __init__(self, vimprime):
        self.print_attr = vimprime

    def open_site( self, thelist ):
        try:
            show_pass("Open site Locaweb", self.print_attr)
            br.open(thelist['locaweb'])
        except Exception, e:
            #logging.exception(e)
            add_error("CRITICAL: Cannot open the locaweb page")
            #return [2, "CRITICAL: Cannot open the locaweb page", perfdata(stime)]

    def choice_product(self, prod, title):
        try: 
            show_pass("Choice product", self.print_attr)
            br.follow_link(text_regex=r'%s' % prod, nr=1)
            if br.title().find(title) == -1:
                add_error("CRITICAL: Problems on product menu")
                #return [2, "CRITICAL: Problems on step 1", perfdata(stime)]
        except Exception, e:
            #logging.exception(e)
            add_error("CRITICAL: Cannot open the locaweb page")
            #return [2, "CRITICAL: Cannot open the locaweb page", perfdata(stime)]        

    def verify_product_plan(self, product):  
        show_pass("verify product plan", self.print_attr)     
        response = br.follow_link(text_regex=r'Planos', nr=0) 
        if br.title().find('Planos') == -1:
            add_error("CRITICAL: Problems on step 2")
            #return [2, "CRITICAL: Problems on step 2", perfdata(stime)]    
        result = htmlParse(response.get_data(), 'span', 'class', 'plan-title-inner')[0].text.strip()
        if result != product:
            add_error("CRITICAL: " + product + " does not exist")
            #return [2, "CRITICAL: Hospedagem Plus does not exist", perfdata(stime)]
        return response

    def choice_product_periodicity(self,response, perc, vlr, plan):
        show_pass("choice product periodicity", self.print_attr)
        response = br.follow_link(text_regex=r'Planos', nr=0)
        result = htmlParse(response.get_data(), 'ul', 'class', 'plan-select select-form plan-select-season space-bottom-small hidden')[1]
        if result.find('li', attrs={'data-rel': 'plnAnu'}).text.strip() != plan + " - " + perc + " OFFTotal de R$ " + vlr:
            add_error("CRITICAL: " + plan + " option does not exist")
            #return [2, "CRITICAL: Plano Anual option does not exist", perfdata(stime)]

    def choice_product_periodicity_2(self, response, perc, vlr, plan):
        show_pass("choice product periodicity", self.print_attr)
        response = br.follow_link(text_regex=r'Planos', nr=0)
        result = htmlParse(response.get_data(), 'select', 'class', 'plan-select select-form')[0]
        if result.find('option', attrs={'value': '12'}).text.strip() != plan + " -" + perc:
            add_error("CRITICAL: " + plan + " option does not exist")
            #return [2, "CRITICAL: Plano Anual option does not exist", perfdata(stime)]


    def buy_product(self,url):
        try:
            show_pass("Buy product", self.print_attr)
            response = br.open(url['contratacao'])
        except Exception, e:
            #logging.exception(e)
            add_error("CRITICAL: Cannot open the Contratacao product page")
            #return [2, "CRITICAL: Cannot open the Contratacao Hospedagem de Sites page", perfdata(stime)]
    
    def verify_resume_plans(self):
        show_pass("Verify resume plans", self.print_attr)
        for form in br.forms():
            if form.attrs['id'] == 'frmplans':
                control = form.find_control('periodo')
                if control.value != 'plnAnu':
                    add_error("CRITICAL: Plano Anual radio button is not selected")
                    #return [2, "CRITICAL: Plano Anual radio button is not selected", perfdata(stime)]  
             

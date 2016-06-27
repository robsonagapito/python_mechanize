#!/usr/bin/env python
# -*- coding: utf-8 -*-
import socket
import time
import os
import logging
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
    url = { 'locaweb':            'http://www.locaweb.com.br',
            'contratacao':        'http://www2.locaweb.com.br/contratar-smtp-locaweb/autenticacao.html?plan=0&period=12',
            'checkout':           'http://www2.locaweb.com.br/contratar-smtp-locaweb/autenticacao.html?login=&period=12&plan=0',
            'checkout_login':     'http://www2.locaweb.com.br/templates/locaweb-ficha-smtp/process.php?systems2.login=mfsys2&login=%s&period=12&plan=0' % username}
    links = ['http://assets.locaweb.com.br/site/contratos/contrato-smtp.pdf']
    site = Site(imprimirTela)
    checkout = Checkout(imprimirTela)
  
    try:
        site.open_site(url)
        site.choice_product("SMTP Locaweb",'Planos SMTP')
        response = site.verify_product_plan('Plano I')
        site.choice_product_periodicity_2(response, "10%", "0", "Anual")
        site.buy_product(url)
        site.verify_resume_plans()
        br = checkout.open_page(url)
        response = checkout.login_user_2(br, url, username, password)
        response = checkout.verify_order_review(response,'R$ 324,00', 'Contratar SMTP Locaweb', '1 ano', 'SMTP Locaweb I')
        checkout.verify_payment(response,'R$','324,00', 'Boleto bancário')
        checkout.verify_payment_links(br, links)
        checkout.verify_payment_ip()
        checkout.payment_continue()
        response = checkout.print_boleto()
        checkout.verify_boleto(response, '324,00', '05707-000') 

    except Exception, e:
        #logging.exception(e)
        add_error("CRITICAL: %s" % repr(e))

    if len(array_error) > 0:
        print_screen ("ERROR: " + array_error[0], imprimirTela)
        return [2,array_error[0], perfdata(stime)]
    else:
        print_screen ("MONITORACAO PASSOU COM SUCESSO!",imprimirTela)
    
stime = time.time()
start_time = stime

ret = __run__('s')

print ret

final_time = time.time()
print_screen (start_time,imprimirTela)
print_screen (final_time,imprimirTela)
res_time = final_time - start_time
print_screen (res_time,imprimirTela)
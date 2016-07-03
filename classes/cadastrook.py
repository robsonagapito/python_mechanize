#!/usr/bin/env python
# -*- coding: utf-8 -*-

from support.generic import *

class CadastroOk(object):

    print "entrou cadasto ok"

    def __init__(self, vimprime):
        self.print_attr = vimprime

    def message_ok(self,response):
        try:
            show_pass("Message Ok", self.print_attr)
            text_id(response, 'body')
        except Exception, e:
            add_error("CRITICAL: Cannot verify message => %s" % repr(e))
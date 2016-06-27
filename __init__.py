#!/usr/bin/env python
# -*- coding: utf-8 -*-

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
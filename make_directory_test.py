#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 16 23:20:24 2021

@author: lion
"""

import os

# define the name of the directory to be created
path = "Ali"

# define the access rights
#access_rights = 0o755

try:
    os.mkdir(path)
except OSError:
    print ("Creation of the directory %s failed" % path)
else:
    print ("Successfully created the directory %s" % path)
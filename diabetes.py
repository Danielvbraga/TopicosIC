#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Oct  8 11:51:33 2018

@author: daniel
"""

from sklearn.datasets import load_diabetes

diabetes = load_diabetes()
#itens da base
diabetes.keys()

print(diabetes.DESCR)
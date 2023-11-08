#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov  2 15:42:00 2023

@author: calvinmcdonough
"""

import csv

with open('listOfPrimes.csv', newline='') as csvfile:
    data = list(csv.reader(csvfile))
    primes = []

    print (type(data[1][1]))
    
    print( 2**10000000, "yes")
        
        
   
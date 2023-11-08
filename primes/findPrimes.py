#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov  2 15:20:56 2023

@author: calvinmcdonough
"""
import pandas as pd
import math
def main():
    primes = [2]

    for i in range(3,10**6,2):
        print(i)
        if is_prime(i,primes):
            primes.append(i)
            
    #print(primes)
    bigPrime = 1
    for i in primes:
        bigPrime = bigPrime * i
        print(i)
        
    #print(bigPrime+1)
    print("this is the length: " , len(str((bigPrime+1)**2)))
    
        
    #pd.DataFrame(primes).to_csv('listOfPrimes.csv') 
        
        
def is_prime(n, primes):
  z = int(math.sqrt(n))
  i = 0
 
  
  while i<len(primes)and primes[i]<=z:
      
      if n % primes[i] == 0:
          return False
      i+=1
        
  return True
    
    
        
      
  
  return True    

main()
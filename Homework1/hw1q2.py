#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

@author: slefever1

Decision tree model using if statement
"""

def checkWeather():
    
    print('Sunny, Rainy, or Overcast (s/r/o): ')
    outlook = input()
    print('Humidity high or normal (h/n): ')
    humidity = input()
    print('Wind strong or weak (s/w): ')
    wind = input()

    if outlook == 'o':
        return True
    elif outlook == 's':
        if humidity == 'h':
            return False
        elif humidity == 'n':
            return True
    elif outlook == 'r':
        if wind == 's':
            return False
        elif wind == 'w':
            return True
        
tennisCheck = checkWeather()
if tennisCheck:
    print('Go play tennis')
else:
    print('No tennis for you')


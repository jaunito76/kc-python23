# -*- coding: utf-8 -*-
"""
Created on Mon Sep  4 20:34:53 2023
@author: corrietinsley
"""
x=float(input('enter a number or die: '))
guess=0.0
epsilon=0.0001
while (guess * guess < x):
    guess = guess + epsilon
print(f'the square root of {x} is {guess}')   
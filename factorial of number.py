# -*- coding: utf-8 -*-
"""
Created on Mon Sep 16 09:35:09 2019

@author: Rushikesh
"""

def factorial(n):
    product=1
    for i in range(1,n+1):
        product=product*i
    return(product)
    
n=int(input("Enter Positive Number"))
if(n==0):
    print("Factorial of Number is 1 ")
elif(n<0):
    print("Please Enter the Positive Int Value ")
    
else:
    f=factorial(n)
    print("Factorial of ",n," is",f)
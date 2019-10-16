# -*- coding: utf-8 -*-
"""
Created on Sat Sep  7 22:11:08 2019

@author: Rushikesh
"""

def bubble_sort(a):
    n=len(a)
    
    for i in range(n):
        for j in range(0,n-i-1):
            if(a[j]>a[j+1]):
                tmp=a[j]
                a[j]=a[j+1]
                a[j+1]=tmp
                
a=[1,4,2,5,6,7,0]
bubble_sort(a)

for i in a:
    print(i)

                
# -*- coding: utf-8 -*-
"""
Created on Sun Sep  8 15:50:25 2019

@author: Rushikesh
"""

def binary_search(a,x):
    first_pos=0
    last_pos=len(a)-1
    flag=0
    count=0
    
    while(first_pos<=last_pos and flag==0):
        count=count+1
        mid=(first_pos+last_pos)//2
        if(x==a[mid]):
            flag=1
            print("Element is Found at Location ",str(mid))
            print("The Number of Itteration are ",str(count))
            return
        else:
            if(x<a[mid]):
                last_pos=mid-1
            else:
                first_pos=mid+1
                
    print("Element is Not Found")
    
    
a=[]
for i in range(1,501):
    a.append(i)
    
binary_search(a,70)
                
        
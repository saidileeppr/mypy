a="17121A05"
l=["g9",'f8','f9','g0','f0','h0','h1','h2','k7','j0']
l1=[]
for i in l:
    l1.append(a+i)
n=input("enter msg:")
import os
for  i in range(len(l1)):
    os.system("write",l1[i],n) 

 

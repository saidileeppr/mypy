a="17121A05"
n=input("ENter msg:")
l=["g9",'f8','f9','g0','f0','h0','h1','h2','k7','j0']
l1=[]
for i in l:
    l1.append("write "+a+i+' '+n)
import os
for  i in l1:
    os.system("%s"%i)

 

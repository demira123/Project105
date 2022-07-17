import math
import statistics as st
import csv

x = [60,61,65,63,98,99,90,95,91,96]
mean=st.mean(x)
print(mean)

squaredList = []

for i in x :
    q = i - mean
    q = q**2 
    squaredList.append(q)

sum=0
for i in squaredList:
    sum=sum+i
    

n = len(x) - 1

stdv=math.sqrt(sum/n)

print(stdv)
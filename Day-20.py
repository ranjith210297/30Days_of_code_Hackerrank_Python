#!/bin/python3

import sys

n = int(input().strip())
a = list(map(int, input().strip().split(' ')))
# Write Your Code Here

count = 0
for i in range(len(a)):
    for j in range(len(a)-1):
        if(a[j]>a[j+1]):
            a[j],a[j+1] = a[j+1],a[j]
            count+=1
    if count==0:
        break
print("Array is sorted in "+str(count)+" swaps.")
print("First Element: "+str(a[0]))
print("Last Element: "+str(a[n-1]))
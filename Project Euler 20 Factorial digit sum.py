#https://www.hackerrank.com/contests/projecteuler/challenges/euler020/problem

import math

def sums(n):
    tot=0
    while(n>0):
        dig=n%10
        tot=tot+dig
        n=n//10
    return tot 
    
n = [int(input()) for _ in range(int(input()))]
out=[]
totsum=[]
for i in n:
    out.append(math.factorial(i))
for i in out:
    totsum.append(sums(i))
for i in totsum:
    print(i)
del out,totsum
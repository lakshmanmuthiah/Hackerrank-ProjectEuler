#https://www.hackerrank.com/contests/projecteuler/challenges/euler003/problem

import sys
import math 

def primeFactors(n): 
    s=[]
    while n % 2 == 0: 
        s.append(2)
        n = n / 2
    for i in range(3,int(math.sqrt(n))+1,2): 
        while n % i== 0: 
            s.append(int(i))
            n = n / i 
    if n > 2: 
        s.append(int(n))
    return max(s)

t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    print(primeFactors(n))

#https://www.hackerrank.com/contests/projecteuler/challenges/euler034/problem
        
n = int(input())
a=[1,1,2,6,24,120,720,5040,40320,362880]
totsum=0 
for i in range(10,n): 
    b = [int(x) for x in str(i)]
    c=0
    for j in b:
        c=c+a[j]
    if(c%i==0): 
        totsum=totsum+i
print(totsum)
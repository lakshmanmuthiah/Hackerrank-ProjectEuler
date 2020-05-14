#https://www.hackerrank.com/contests/projecteuler/challenges/euler048/problem

import math

def sumsqre(n):
    print(int(str(sum(pow(i, i, 10 ** 10) for i in range(n + 1)))[-10:]) - 1)

n = int(input())
sumsqre(n)
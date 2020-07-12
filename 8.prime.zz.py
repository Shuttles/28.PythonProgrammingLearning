#!/usr/bin/env python
# coding=utf-8

MAX_N = 10001

is_prime = [0] * MAX_N
prime = []

for i in range(2, MAX_N):
    if not is_prime[i]:
        prime.append(i)
    for j in prime:
        if i * j >= MAX_N:
            break
        is_prime[i * j] = 1
        if i % j == 0:
            break

print(prime)


#!/usr/bin/env python
# coding=utf-8
MAX_N = 10000

is_prime = [0]
prime = [0]

for i in range(MAX_N):
    prime.append(0)
    is_prime.append(0)

#泽哥写法
'''
prime = [0 for i in range(MAX_N + 5)]
'''

#线性筛初始化函数
def init():
    for i in range(2, MAX_N + 1):
        if is_prime[i] == 0:
            prime[0] += 1
            prime[prime[0]] = i
        for j in range(1, prime[0] + 1):
            if i * prime[j] > MAX_N:
                break
            is_prime[i * prime[j]] = 1
            if i % prime[j] == 0:
                break

def main():
    init()
    print("第%dth素数是%d" % (prime[0], prime[prime[0]]))

if __name__ == '__main__':
    main()

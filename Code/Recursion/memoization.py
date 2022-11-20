#Tối ưu thuật toán fibonnacci
#Sử dụng cache để tránh lặp lại công việc

import time
from functools import lru_cache

def fib(n):
    """Returns the n-th Fibonacci number"""
    if n == 0 or n == 1:
        return n
    return fib(n-1) + fib(n-2)

@lru_cache
def fib_lru(n):
    if n == 0 or n == 1:
        return n
    return fib_lru(n-1) + fib_lru(n-2)

#Caching thủ công sử dụng dictionary
def fib_cache(n, cache = None):
    if cache is None:
        cache = {}
    if n in cache:
        return cache[n]
    if n == 0 or n == 1:
        return n
    result = fib_cache(n-1, cache) + fib_cache(n-2, cache)
    cache[n] = result
    return result

n = 900
start = time.perf_counter()
fib_cache(n)
end = time.perf_counter()
print("Cache phiên bản thủ công. Seconds taken: {:.7f}".format(end - start))
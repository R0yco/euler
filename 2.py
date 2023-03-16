import math

def fib(a, b, i):
    if i == 0:
        return a
    return fib(b, a+b, i-1)

def find_fib_index(ceil):
    index = 1
    while True:
        current_fib = fib(1, 2, index)
        if current_fib > ceil:
            return index-1
        index += 1






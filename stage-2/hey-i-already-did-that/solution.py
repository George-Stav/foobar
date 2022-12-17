#!/usr/bin/env python2

def subtract(x, y, b):
    n = int(x, base=b) - int(y, base=b)
    if n==0:
        return '0'
    # Convert from base 10 to base b
    nums = []
    while n:
        n, remainder = divmod(n, b)
        nums.append(str(remainder))
    return ''.join(reversed(nums))

def solution(n, b):
    k = len(n)
    d = {}
    i = 0

    # Due to the deterministic nature of the sequence, a second appearance of any number n
    # indicates a cycle. If such a cycle is detected, terminate the while-loop and return the
    # length of the cycle.
    while n not in d.keys():
        d[n] = i
        i += 1
        x = ''.join(sorted(n, reverse=True))
        y = ''.join(sorted(n))
        n = subtract(x, y, b).rjust(k, '0')

    return len(d) - d[n]

print(solution('1211', 10))
print(solution('210022', 3))

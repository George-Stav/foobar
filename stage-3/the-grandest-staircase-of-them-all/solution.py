#!/usr/bin/env python2

import pprint
pp = pprint.PrettyPrinter(indent=4)

def first_solution(n):
    dl = {}
    for i in range(3, n+1):
        cl = []
        # print(range(i-1, int(i/2)-1, -1))
        for j in range(i-1, int(i/2)-1, -1):
            if j > i-j:
                cl.append((j, i-j))
                if i-j in dl.keys():
                    cl += [(j,)+x for x in dl[i-j]]
            elif (j == i-j or j == i-j-1) and j in dl.keys():
                cl += [(j,)+x for x in dl[i-j] if j > x[0]]
        dl[i] = cl

    # pp.pprint(dl)
    print(len(dl[n])+1 if n >= 10 else len(dl[n]) )
    return len(dl[n])+1 if n >= 10 else len(dl[n])

import functools
import sys

sys.setrecursionlimit(500*3 + 10)

def second_solution(n):
    memo = [[0 for _ in range(n+2)] for _ in range(n+2)]
    print(helper(memo, 1, n)-1)

def helper(memo, x, z):
    if memo[x][z]:
        return memo[x][z]

    if not z:
        return 1
    if z < x:
        return 0

    r = helper(memo, x+1, z-x) + helper(memo, x+1, z)
    memo[x][z] = r
    return r


# first_solution(200)
second_solution(200)

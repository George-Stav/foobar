#!/usr/bin/env python2

from time import time

def first_solution(l):
    if len(l) < 3:
        return 0
    t = []
    for k, z in enumerate(l[2:]):
        for j, y in enumerate(l[1:]):
            for i, x in enumerate(l):
                if (y%x == 0 and j+1>i) and (z%y == 0 and k+2>j+1):
                    t.append([x,y,z])

    # print(len(t))
    # print(len(t), t)
    return len(t)

def second_solution(l):
    if len(l) < 3:
        return 0
    t = []
    xs = {x:i for i, x in enumerate(l) if (4*x <= l[-1] or 2*x <= l[-1] or x == l[-1]) and i+3 <= len(l)}
    ys = {y:j+1 for x, i in xs.items() for j, y in enumerate(l[1:]) if i<j+1 and (2*y <= l[-1] or y == l[-1]) and j+3 <= len(l) and y%x == 0}
    zs = {z:k+2 for y, j in ys.items() for k, z in enumerate(l[2:]) if j<k+2 and z%y == 0}

    t = []
    for x, i in xs.items():
        for y, j in ys.items():
            for z, k in zs.items():
                if (y%x == 0 and i<j) and (z%y == 0 and j<k):
                    t.append([x, y, z])

    print(t)

def third_with_memo(l):
    if len(l) < 3:
        return 0
    l.reverse()

    t1 = []
    tfn = 0
    for k, z in enumerate(l[:-2]):
        t2 = [z]
        for j, y in enumerate(l[k+1:]):
            if z%y == 0:
                t2.append(y)
        if len(t2) > 3:
            t1.append(t2)
        elif len(t2) == 3 and t2[0]%t2[1] == 0 and t2[1]%t2[2] == 0:
            tfn += 1

    memo = {}
    for p in t1:
        z = p[0]
        for j, y in enumerate(p[1:-1]):
            n = tfn
            key = str([z] + p[j+1:])
            if key in memo.keys():
                tfn += memo[key]
            elif z == y:
                tfn += len(p) - (j+2)
            else:
                for x in p[j+2:]:
                    if y%x == 0:
                        tfn += 1
                        memo[key] = tfn - n

    return tfn

def third_solution(l):
    # Relies too much on pairs (e.g. [1] * 2000)
    # Has time issues when pairs are not present (e.g. [pow(2, x) for x in range(0, 20)] * 100)
    if len(l) < 3:
        return 0
    l = l[::-1]

    t1 = []
    tfn = 0
    for k, z in enumerate(l[:-2]):
        if t1 and t1[-1][0] == z:
            t1.append(t1[-1][1:])
            continue
        t2 = [z]
        for j, y in enumerate(l[k+1:]):
            if z%y == 0:
                t2.append(y)
        if len(t2) > 3:
            t1.append(t2)
        elif len(t2) == 3 and t2[0]%t2[1] == 0 and t2[1]%t2[2] == 0:
            tfn += 1

    for p in t1:
        z = p[0]
        for j, y in enumerate(p[1:-1]):
            if z == y:
                tfn += len(p) - (j+2)
            else:
                for x in p[j+2:]:
                    if y%x == 0:
                        tfn += 1

    return tfn


def dynamic_solution(l):
    c = [0] * len(l)
    count = 0
    for i in range(0,len(l)):
        for j in range(0, i):
            if l[i] % l[j] == 0:
                c[i] = c[i] + 1
                count = count + c[j]
    return count

start = time()
print(dynamic_solution([1]*2000))
first = time()
print("rogue solution took: ", first - start)
print(third_solution([1]*2000))
print("third solution took: ", time() - first)

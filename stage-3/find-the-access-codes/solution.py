#!/usr/bin/env python2

from itertools import groupby

def first_solution(l):
    if len(l) < 3:
        return 0
    t = []
    for k, z in enumerate(l[2:]):
        for j, y in enumerate(l[1:]):
            for i, x in enumerate(l):
                if (y%x == 0 and j+1>i) and (z%y == 0 and k+2>j+1):
                    t.append([x,y,z])

    print(len(t), t)
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

def third_solution(l):
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

    for p in t1:
        z = p[0]
        for j, y in enumerate(p[1:-1]):
            if z == y:
                tfn += len(p) - (j+2)
                continue

            for x in p[j+2:]:
                if z%y == 0 and y%x == 0:
                    tfn += 1

    print(tfn)
    return tfn



# third_solution([1, 1, 1])
first_solution([2, 3, 4, 5, 6, 7, 8, 12, 12])
third_solution([2, 3, 4, 5, 6, 7, 8, 12, 12])
# third_solution([1, 2, 3, 4, 5, 6])

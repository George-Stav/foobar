#!/usr/bin/env python2

import numpy as np
import fractions as F

def print_matrix(m):
    for row in m:
        print "[",
        for item in row:
            print item, ",",
        print "]"


# Absorbing Markov Chains
def solution(m):
    ts = [] # terminal states
    nts = {} # non-terminal states (key=index | value=denominator)
    for i, x in enumerate(m):
        if sum(x) == 0:
            ts.append(i)
        else:
            nts[i] = sum(x)

    r = []
    q = []

    for index, denom in nts.items():
        temp_r = []
        for t in ts:
            temp_r.append(m[index][t]/float(denom))
        r.append(temp_r)

        temp_q = []
        for t in nts.keys():
            temp_q.append(m[index][t]/float(denom))
        q.append(temp_q)

    f = np.linalg.inv(np.identity(len(q)) - q)
    product_fr = np.matmul(f, r)
    fractions = []

    for row in product_fr:
        temp = []
        for n in row.tolist():
            temp.append(F.Fraction(n).limit_denominator())
        fractions.append(temp)

    common_denom = reduce(F.gcd, fractions[0]).denominator
    answer = []

    for n in fractions[0]:
        factor = common_denom/n.denominator
        answer.append(n.numerator * factor)
    answer.append(common_denom)

    print(answer)


solution([[0, 2, 1, 0, 0], [0, 0, 0, 3, 4], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]])
solution([[0, 1, 0, 0, 0, 1], [4, 0, 0, 3, 2, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0]])
solution([[0,1,0],[0,0,0],[0,0,0]])

#!/usr/bin/env python2

import random

def pair(t):
    l = []
    if (t[0]+t[1]) % 2 != 0: # adding to odd means infinite loop
        return True
    while True:
        if t in l or t[::-1] in l: # infinite loop
            print "loop detected:", t
            return True
        elif t[0] == t[1]: # tie
            print "tie detected: ", t
            return False

        print(t)
        l.append(t)
        t = (min(t)*2, abs(t[0] - t[1]))

def solution(banana_list):
    successful_pairs = [(i, i+j+1) for i, n1 in enumerate(banana_list[:-1])
                        for j, n2 in enumerate(banana_list[i+1:]) if pair((n1, n2))]
    successful_pairs_i = [(n1, n2) for i, n1 in enumerate(banana_list[:-1])
                        for j, n2 in enumerate(banana_list[i+1:]) if pair((n1, n2))]
    print(banana_list)
    print(successful_pairs_i)
    print(successful_pairs)

    r = []
    for i, p1 in enumerate(successful_pairs[:-1]):
        l = [p1[0], p1[1]]
        for p2 in successful_pairs[i+1:]:
            if p2[0] not in l and p2[1] not in l:
                l.append(p2[0])
                l.append(p2[1])
        if len(l) == len(banana_list):
            return 0
        else:
            r.append(len(banana_list) - len(l))

    if len(successful_pairs) == 1:
        return 0
    elif r:
        return min(r)
    else:
        return len(banana_list)

# print(solution([1,21,3,7,13,19,1,13]))
# print(solution([1,21,3,7,13,19]))
# print([random.randint(1, 1073741824) for _ in range(10)])
# l = [random.randint(1, 1073741824) for _ in range(2)]
# try:
#     print(solution(l))
# except KeyboardInterrupt:
#     print l

import matplotlib.pyplot as plt

def plot_pairs(t):
    l = []
    if (t[0]+t[1]) % 2 != 0: # adding to odd means infinite loop
        return True
    plt.axis([0, 1073741823, 0, 1073741823])

    i=0
    while i<10000:
        if t in l or t[::-1] in l: # infinite loop
            print "loop detected:", t
            return True
        elif t[0] == t[1]: # tie
            print "tie detected: ", t
            return False

        print(t)
        l.append(t)
        t = (min(t)*2, abs(t[0] - t[1]))

        plt.scatter(t[1], t[0])
        plt.pause(0.005)
        i += 1

    plt.show()

plot_pairs((random.randint(1, 1073741824),random.randint(1, 1073741824)))

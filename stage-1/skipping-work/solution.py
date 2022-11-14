#!/usr/bin/env python2

import timeit

# easy (inefficient) solution
# def solution(x, y):
#     if len(x) > len(y):
#         for i in x:
#             if i not in y:
#                 return i
#     else:
#         for i in y:
#             if i not in x:
#                 return i

def solution(x, y):
    x = set(x)
    y = set(y)
    if len(x) > len(y):
        for i in x:
            if i not in y:
                return i
    else:
        for i in y:
            if i not in x:
                return i

solution(range(1,100), range(1,101))
# print solution([13, 5, 6, 2, 5], [5, 2, 5, 13]) # 6
# print solution([14, 27, 1, 4, 2, 50, 3, 1], [2, 4, -4, 3, 1, 1, 14, 27, 50]) # -4

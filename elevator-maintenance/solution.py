#!/usr/bin/env python2

import timeit

def solution(l):
    return sorted(l)

def mergeSort(a):
    if len(a) > 1:
        # r is the point where the array is divided into two subarrays
        r = len(a) // 2 # be careful with this, python2 may behave differently
        L = a[:r]
        M = a[r:]

        # Sort the two halves
        mergeSort(L)
        mergeSort(M)

        i = j = k = 0

        # Until we reach either end of either L or M, pick larger among
        # elements L and M and place them in the correct position at A[p..r]
        while i < len(L) and j < len(M):
            if compare(L[i], M[j]):
                a[k] = L[i]
                i += 1
            else:
                a[k] = M[j]
                j += 1
            k += 1

        # When we run out of elements in either L or M,
        # pick up the remaining elements and put in A[p..r]
        while i < len(L):
            a[k] = L[i]
            i += 1
            k += 1

        while j < len(M):
            a[k] = M[j]
            j += 1
            k += 1

def compare(a, b):
    al = a.split(".")
    bl = b.split(".")
    print al, bl

    if a[0] == b[0]:
        # 2 vs 2.x
        if len(al) == 1 or len(bl) == 1:

    else:
        return a[0] < b[0]

# print solution(["1.11", "2.0.0", "1.2", "2", "0.1", "1.2.1", "1.1.1", "2.0"])
a = ["1.11", "2.0.0", "1.2", "2", "0.1", "1.2.1", "1.1.1", "2.0"]
b = [5,2,4,6,6,1,2,5]
print a
mergeSort(a)
print a

#!/usr/bin/env python2

def solution(l):
    # print(",".join(mergesort(l)))
    print ",".join(mergesort(l))

def mergesort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left = arr[:mid]
        right = arr[mid:]

        mergesort(left)
        mergesort(right)

        i = j = k = 0

        while i < len(left) and j < len(right):
            if compare(left[i], right[j]):
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1

    return arr

def compare(a, b):
    al = a.split(".")
    bl = b.split(".")

    # compare by major, minor or revision numbers
    for x in zip(al, bl):
        # If major version number is the same (e.g. 2.0 vs 2.1)
        # then continue to comparing the minor version number, and so on.
        if x[0] != x[1]:
            return int(x[0]) <= int(x[1])

    # This case happens when one of the two version numbers is missing one or more integers
    # e.g. 2 vs 2.0 OR 1.2.1 vs 1.2
    return len(al) < len(bl)

solution(["1.11", "2.0.0", "1.2", "2", "0.1", "1.2.1", "1.1.1", "2.0"])

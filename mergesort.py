import sys      
import time     
from sort_helper import *
def merge(arr, p, q, r):
    n1 = q - p + 1
    n2 = r - q

    L = [None] * (n1+1)
    R = [None] * (n2+1)

    for i in range(n1):
        L[i] = arr[p + i]

    for j in range(n2):
        R[j] = arr[q + j + 1]

    L[n1] = sys.maxsize
    R[n2] = sys.maxsize

    i = 0
    j = 0

    for k in range(p, r+1):
        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1


def merge_sort(arr, p, r):
    if p < r:
        q = (p + r) // 2
        merge_sort(arr, p, q)
        merge_sort(arr, q+1, r)
        merge(arr, p, q, r)

for x in SIZE_LIST:
    read_file(x)
    print(f"Original array is {values}")
    start = time.time()
    merge_sort(values, 0, len(values)-1)
    end = time.time()
    print(f"Sorted array is {values}")
    print(f"Time taken was {end-start:.5f} seconds")
    print()
    values.clear()

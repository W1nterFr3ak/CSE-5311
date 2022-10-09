from sort_helper import *
import time


def sep(arr, p, r):
    x = arr[r][3]
    i = p - 1

    for j in range(p, r):
        if arr[j][3] <= x:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i+1], arr[r] = arr[r], arr[i+1]
    return i + 1

def quick_sort(arr, p, r):
    if p < r:
        q = sep(arr, p, r)
        quick_sort(arr, p, q-1)
        quick_sort(arr, q + 1, r)

for val in SIZE_LIST:
    read_file(val)
    print(f"Original array is")
    for i in values:
        print(i)

    start = time.time()
    quick_sort(values, 0, len(values)-1)
    end = time.time()
    print(f"Sorted array is")
    for i in values:
        print(i)

    print(f"Time taken was {end-start:.5f} seconds")
    print()
    values.clear()

from sort_helper import *
# from pprint import pprint
import time

def generate_date(size):
    with open(f"arr{size}.txt", "w") as tf:
        for i in range(size):
            total = 0
            for j in range(3):
                number = random.randint(0, 6000)
                if j == 2:
                    tf.write(f"{number}, {total}\n")
                else:
                    tf.write(str(number) + ",")
                total += number
            total = 0

def insertion_sort():
    for j in range(1, len(values)):
        key = values[j]
        i = j - 1
        while i >= 0 and values[i][3] > key[3]:
            values[i + 1] = values[i]
            i = i - 1
        values[i + 1] = key

for x in SIZE_LIST:
    print(f"Step {x} n")
    generate_date(x)
    read_file(x)
    print(f"Original array is ")
    
    for i in values:
        print(i)

    start = time.time()
    insertion_sort()
    end = time.time()
    print(f"Sorted array is")

    for i in values:
        print(i)
    
    print(f"Time taken was {end-start:.5f} seconds")
    print()
    values.clear()

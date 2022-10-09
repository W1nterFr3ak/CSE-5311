import random   

SIZE_LIST = [20, 100, 1000, 4000]
values = []                      



def read_file(size):
    with open(f'arr{size}.txt', 'r') as tf:
        field = tf.read().strip().split('\n')
        for num in field:
            # if num.split(',')[-1].isdigit():
            #     values.append(int(num))
            values.append(num.split(","))





# read_file(20)
# print(values)
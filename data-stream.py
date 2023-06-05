import random
import math
import numpy as np
from basic_skiplist import Basic_skiplist
from promote_one_level_skiplist import Promote_one_level_skiplist
from promote_top_skiplist import Promote_top_skiplist
from promote_random_level_skiplist import Promote_random_level_skiplist


def data_gen(num_points, limit):
    res = []
    for _ in range(num_points):
        data_point = random.randint(1, limit)
        res.append(data_point)
    return res


def uniform_data_gen(num):
    skiplist1 = Basic_skiplist()
    skiplist2 = Promote_one_level_skiplist()
    # data_arr = data_gen(num, range)
    for _ in range(num):
        # generates a random float between 0 and 1 (inclusive)
        # data = data_arr[num]
        data = random.randint(0, limit)
        skiplist1.search_and_insert(data, data)
        skiplist2.search_and_insert(data, data)
        if(_ == num-2):
            print("vooo")
    # skiplist1.display()
    print("Size>>", skiplist1.size())
    print(">>>>>>>", skiplist1.level_element_count)
    print("Level count>>", skiplist1.levels_count)
    print("no of comp", skiplist1.num_of_comparison)

    print("Size>>", skiplist2.size())
    print(">>>>>>>", skiplist2.level_element_count)
    print("Level count>>", skiplist2.levels_count)
    print("no of comp", skiplist2.num_of_comparison)

# Some numbers must have more rpeference than other numbers
def exp_data_gen(size):
    skiplist1 = Basic_skiplist()
    skiplist2 = Promote_random_level_skiplist()

    random_numbers = np.random.exponential(scale, size)

    abc= {}
    for i in range(random_numbers.size):
        i = round(random_numbers[i], 3)
        i = round(i*10)
        if(i in abc):
            abc[i] = abc[i]+1
        else:
            abc[i] = 1

    print(abc)

    for i in range(num_points):
        # generates a random integer from the exponential distribution
        data_point = round(random_numbers[i])
        skiplist1.search_and_insert(data_point, data_point)
        skiplist2.search_and_insert(data_point, data_point)
    # skiplist.display()
    print("Size>>", skiplist1.size())
    print(">>>>>>>", skiplist1.level_element_count)
    print("Level count>>", skiplist1.levels_count)
    print("no of comp", skiplist1.num_of_comparison)
    

    print("Size>>", skiplist2.size())
    print(">>>>>>>", skiplist2.level_element_count)
    print("Level count>>", skiplist2.levels_count)
    print("no of comp", skiplist2.num_of_comparison)
    # skiplist2.display()



# example usage
num_points = 1000000
scale = 1.2
limit = 100000


uniform_data_gen(num_points)

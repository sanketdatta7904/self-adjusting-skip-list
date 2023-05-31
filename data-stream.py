import random
import math
import numpy as np
from basic_skiplist import Basic_skiplist
from promote_one_level_skiplist import Promote_one_level_skiplist
from promote_top_skiplist import Promote_top_skiplist



def data_gen(num_points, limit):
    res = []
    for _ in range(num_points):
        data_point = random.randint(1, limit)
        res.append(data_point)
    return res



# def uniform_data_gen(num):
#     skiplist = Skiplist()
#     for i in range(num):
#         # generates a random float between 0 and 1 (inclusive)
#         data_point = random.randint(0, 1000)
#         skiplist.insert(data_point, data_point, skiplist.locate_key, flag=True)
#     skiplist.display()
#     print("Size>>", skiplist.size())
#     print(">>>>>>>", skiplist.level_element_count)
#     print(">>>", skiplist.deleteMap)
#     print("Level count>>", skiplist.levels_count)
#     print("no of comp", skiplist.num_of_comparison)

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
    skiplist2 = Promote_one_level_skiplist()

    random_numbers = np.random.exponential(scale, size)

    print(random_numbers)
    abc= {}
    # for i in range(random_numbers.length):
    #     if(i in abc):

    # print(data_point)
    # for i in range(num_points):
    #     # generates a random integer from the exponential distribution
        
    #     data_point = random.choices(range(start, end + 1), weights=weights, k=num_points)
    #     skiplist.insert(data_point, data_point)
    # # skiplist.display()
    # print("Size>>", skiplist.size())
    # print(">>>>>>>", skiplist.level_element_count)
    # print(">>>", skiplist.deleteMap)
    # print("Level count>>", skiplist.levels_count)
    # print("no of comp", skiplist.num_of_comparison)


# example usage
num_points = 100000
scale = 1.0
limit = 1000


uniform_data_gen(num_points)

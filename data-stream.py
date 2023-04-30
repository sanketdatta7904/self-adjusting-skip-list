import random
import math
from skiplist import Skiplist


def uniform_data_gen(num):
    skiplist = Skiplist()
    for i in range(num):
        # generates a random float between 0 and 1 (inclusive)
        data_point = random.randint(0, num*num)
        skiplist.insert(data_point, data_point)
    skiplist.display()
    print("Size>>", skiplist.size())
    print("Level count>>", skiplist.levels_count)


def exp_data_gen(num_points, lambd):
    skiplist = Skiplist()
    for i in range(num_points):
        # generates a random integer from the exponential distribution
        data_point = int(-math.log(1 - random.random()) / lambd)
        skiplist.insert(data_point, data_point)
    skiplist.display()
    print("Size>>", skiplist.size())


# example usage
num_points = 10000
lambd = 0.3
# exp_data_gen(num_points, lambd)


uniform_data_gen(num_points)

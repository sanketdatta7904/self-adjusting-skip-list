import random
import math
from skiplist import Skiplist


def uniform_data_gen(num):
    skiplist = Skiplist()
    for i in range (num):
        data_point = random.randint(0, num*num)  # generates a random float between 0 and 1 (inclusive)
        skiplist.insert(data_point, data_point)
    skiplist.display()
    print("Size>>", skiplist.size())


def exp_data_gen(num_points, lambd):
    skiplist = Skiplist()
    for i in range(num_points):
        data_point = int(-math.log(1 - random.random()) / lambd)  # generates a random integer from the exponential distribution
        skiplist.insert(data_point, data_point)
    skiplist.display()
    print("Size>>", skiplist.size())


# example usage
num_points = 1000
lambd = 0.3
# exp_data_gen(num_points, lambd)


uniform_data_gen(num_points)

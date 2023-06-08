import random
import math
import time
import numpy as np
from basic_skiplist import Basic_skiplist
from promote_one_level_skiplist import Promote_one_level_skiplist
from promote_top_skiplist import Promote_top_skiplist
from promote_random_level_skiplist import Promote_random_level_skiplist

# num_points = 100000
# scale = 1.2
# limit = 1000

def data_gen(num_points, limit):
    res = []
    for _ in range(num_points):
        data_point = random.randint(1, limit)
        res.append(data_point)
    return res


def run(num_of_points, limit, variation, scale=0):
    abc= {}
    data = []
    if(variation == "uar"):
        for i in range(num_of_points):
            new_int = random.randint(0, limit)
            data.append(new_int)
    elif(variation == "exp"):
        rand_data =  np.random.exponential(scale, num_of_points)
        for i in range(rand_data.size):
            i = round(rand_data[i], 3)
            i = round(i*1000)
            data.append(i)
            if(i in abc):
                abc[i] = abc[i]+1
            else:
                abc[i] = 1
        print(abc)
            
        
    skiplist1 = Basic_skiplist()
    skiplist2 = Promote_one_level_skiplist()
    skiplist3 = Promote_top_skiplist()
    skiplist4 = Promote_random_level_skiplist()
    skiplist1_time = []
    skiplist2_time = []
    skiplist3_time = []
    skiplist4_time = []
    # data_arr = data_gen(num, range)
    for i in range(num_of_points):
        # generates a random float between 0 and 1 (inclusive)
        # data = data_arr[num]
        skiplist1_time_each = time.time()
        skiplist1.search_and_insert(data[i], data[i])
        skiplist1_time_each_end = time.time()
        skiplist1_time.append(skiplist1_time_each_end-skiplist1_time_each)

        skiplist2_time_each = time.time()
        skiplist2.search_and_insert(data[i], data[i])
        skiplist2_time_each_end = time.time()
        skiplist2_time.append(skiplist2_time_each_end-skiplist2_time_each)

        skiplist3_time_each = time.time()
        skiplist3.search_and_insert(data[i], data[i])
        skiplist3_time_each_end = time.time()
        skiplist3_time.append(skiplist3_time_each_end-skiplist3_time_each)

        skiplist4_time_each = time.time()
        skiplist4.search_and_insert(data[i], data[i])
        skiplist4_time_each_end = time.time()
        skiplist4_time.append(skiplist4_time_each_end-skiplist4_time_each)

  
    # skiplist1.display()
    resObj = {
        "times":{
            "skiplist1_basic": skiplist1_time,
            "skiplist1_basic_avg": sum(skiplist1_time)/len(skiplist1_time),
            "skiplist2_one": skiplist2_time,
            "skiplist2_one_avg": sum(skiplist2_time)/len(skiplist2_time),
            "skiplist3_top": skiplist3_time,
            "skiplist3_top_avg": sum(skiplist3_time)/len(skiplist3_time),
            "skiplist4_rand": skiplist4_time,
            "skiplist4_rand_avg": sum(skiplist4_time)/len(skiplist4_time),

        },
        "movement_count":{
            "skiplist1_basic": skiplist1.num_of_comparison,
            "skiplist2_one":skiplist2.num_of_comparison,
            "skiplist3_top": skiplist3.num_of_comparison,
            "skiplist4_rand":skiplist4.num_of_comparison,

        }
    }
    # print(resObj)
    return resObj
    



# uniform_data_gen(num_points)

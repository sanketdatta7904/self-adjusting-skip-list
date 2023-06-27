
Skiplist Experiment in python(4 variations)

packages used: time, math, random

1. If you want to experiment on data stream, 
    Running command: python dataStream.py
    Please enter
        1. Total numbers count
        2. range of numbers
        3. type of data stream (uar/exp)
        4. in earlier option of "exp" is chosen then enter the scale of distribution(ex: 1/2.5/3)
        
2. If you want to test on single data to see the skiplist actions
    Running command: python test.py
    then choose which kind of skiplist you want to test on. 
    Options:(1/2/3/4) 
        1. Basic skiplist
        2. Promote one level up
        3. Promote to top level
        4. Promote to random level
    Then enter your choice for (1 -> Insert, 2 -> Delete, 3 -> Find, 4 -> Display, 5 -> Exit)
    In this test you can insert/delete/find element one by one
    *the find option here does not promote element. It is just for basic search. In insert option if you give same element already present in the skiplist, then based on the skiplist type it will promote that element.







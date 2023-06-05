import math
import random
import copy

# define custom exception class specially for remove element function if element isnot found


class Exception(Exception):
    pass

# define node class for the skip list


class Node:

    def __init__(self):
        # initialize all four directional pointers and value/key to None
        self.after = None
        self.above = None
        self.before = None
        self.below = None
        self.value = None
        self.key = None


class Skiplist:
    def __init__(self):
        # initialize elements count and levels count to 0
        self.elements_count = 0
        self.levels_count = 0
        self.top_left_element = None
        self.level_element_count = {}

        self.num_of_comparison = 0

        # insert two top level sentinel nodes at the start with one containing negative infinity
        # and the other containing positive infinity, is to provide boundary conditions. Also to provide
        # efficient access to the beginning and end of the skip list
        self.insert_top_level()
        self.insert_top_level()

    def insert(self, key, value):
        # start at the top left element and find the element with the given key (if it exists)
        found_element, no_of_ops = self.locate_key(key)
        pointer = found_element

        # if the key already exists, update its value and return the old value
        if found_element.key == key:
            old_value = found_element.value
            found_element.value = value
            return old_value

        # otherwise, increment the element count and insert the new element
        self.elements_count = self.elements_count + 1
        level = 0
        element = self.insert_after_above(pointer, None, key, value, level)
        # Keeping track of every level's element count
        # self.increase_level_count(level)

        
        
        prob = 0.5

        count = 1
        while random.random() > prob:
            # flip a coin to determine whether to insert a new level
            count = count + 1
            level = level + 1
            while pointer.above is None:
                pointer = pointer.before

            pointer = pointer.above
            element = self.insert_after_above(pointer, element, key, value, level)

            # self.increase_level_count(level)
            

            if count >= self.levels_count:
                self.insert_top_level()
                if(self.levels_count>15):
                    logn = math.log2(self.elements_count)
                    prob = 1-(1/logn)

        return no_of_ops
    
    def increase_level_count(self, level):
        if (level in self.level_element_count):
            self.level_element_count[level] = self.level_element_count[level] + 1  
        else:
            self.level_element_count[level] = 1

    def decrease_level_count(self, level):
        if (level in self.level_element_count):
            self.level_element_count[level] = self.level_element_count[level] - 1  


    def remove_element(self, key):
        # start at the top left element and find the element with the given key
        pointer, key, value, depth_of_node = self.find_first_occurrence(key)
        # raise a custom exception indicating the key was not found
        if pointer.key != key:
            raise Exception('NOT_FOUND')
        # remove the element from all levels of the skip list
        while pointer is not None:
            depth_of_node = depth_of_node-1
            if(pointer.before.key == -math.inf and pointer.after.key == math.inf):
                #   Remove empty levels in the top
                pointer.before.above = None
                pointer.after.above = None
                self.levels_count = self.levels_count - 1
                self.top_left_element = pointer.before
            pointer.before.after = pointer.after
            pointer.after.before = pointer.before
            self.decrease_level_count(depth_of_node)
            pointer = pointer.below
        self.elements_count = self.elements_count - 1

    def find_first_occurrence(self, key):
        # start at the top left element and find the element with the given key (if it exists)
        element, no_of_ops = self.locate_key(key, exact_match=True, first_occur=True)
        if(element == None):
            return (None, None, None, None, 0)
        depthOfnode = 1
        copyElem = element
        while(copyElem.below is not None):
            depthOfnode = depthOfnode+1
            copyElem = copyElem.below
        return (element, element.key, element.value, depthOfnode, no_of_ops)

    def size(self):
        # return the current element count
        return self.elements_count

    def closest_key_after(self, key):
        #  returns the key of the smallest element greater than the given key in the Skip List.
        return self.locate_closest_key(key, 'after')

    def closest_key_before(self, key):
        # returns the key of the largest element less than or equal to the given key in the Skip List.
        return self.locate_closest_key(key, 'before')

    def display(self):
        # Prints the configurations of the skip list, including all levels and elements
        print('-' * 16)
        element = first_element_in_level = self.top_left_element
        level = self.levels_count - 1

        while element is not None:
            if element.key == -math.inf:
                print('\nLevel (', level, ')', end=' ')
            elif element.key == math.inf:
                print(element.key)
                first_element_in_level = element = first_element_in_level.below
                level = level - 1
                continue

            print('', element.key, '(', element.value, ')', end=' || ')
            element = element.after
        print('-' * 16)

    def locate_key(self, key, exact_match=False, first_occur=False):
        no_of_ops = 0
        pointer = self.top_left_element
        # Traverse down the skip list until reaching the bottom level
        while pointer.below is not None:
            pointer = pointer.below
            no_of_ops = no_of_ops+1
        # Traverse right until finding the largest element with a key less than or equal to the given key
            while pointer.after.key <= key:
                pointer = pointer.after
                no_of_ops  = no_of_ops +1
                if(first_occur == True and pointer.key == key):
                    return pointer, no_of_ops
        # If an exact match is required and the found element's key is not equal to the given key, return None else return pointer
        if (exact_match and pointer.key != key):
            return None, no_of_ops
        else:
            return pointer, no_of_ops
        


    def locate_closest_key(self, key, target):
        # Locate the node with the exact match for the given key
        located_element = self.locate_key(key, exact_match=True)

        # If a node with the exact match is found, return the key of the target element in the desired direction
        if located_element:
            target_element = getattr(located_element, target)
            # Check if the target element is infinity, which means there are no keys after/before the input key
            is_inf = (target_element.value ==
                      math.inf or target_element.value == -math.inf)

            if target_element and not is_inf:
                return target_element.key
        # If no node with the exact match is found or if the target element is infinity, return None
        return None

    def insert_top_level(self):
        # Enter a new level with -infinity(left) and +infinity(right) at the top of the skiplist
        self.levels_count = self.levels_count + 1

        self.top_left_element = self.insert_after_above(
            None, self.top_left_element, -math.inf, -math.inf, None
        )
        self.top_left_element.before = self.insert_after_above(
            self.top_left_element, self.top_left_element.after, math.inf, math.inf, None
        )

    def insert_after_above(self, after, above, key, value, level):
        # Takes key and value pair and inserts new node with given level
        # after is the place after which the node should come-- after(left) >> node
        # above is the place above which the node should come-- above(down)>> node(up)
        node = Node()
        node.key = key
        node.value = value
        node.before = after
        node.below = above

        if after is not None:
            node.after = after.after
            if after.after is not None:
                after.after.before = node
            after.after = node

        if above is not None:
            node.above = above.above
            above.above = node
        if(level is not None):
            self.increase_level_count(level)

        return node
    
    def remove_level(self, level, pointer):
        while(pointer.key != -math.inf):
            pointer = pointer.before
        if(pointer.below.below != None):
            while(pointer.key != math.inf):
                temp = pointer.below.below
                temp.above = pointer
                pointer.below = pointer.below.below
                pointer = pointer.after
        else:
            while(pointer.key != math.inf):
                pointer.below = None
                pointer = pointer.after
        self.recount_level_element(level)
        self.levels_count = self.levels_count -1

    def recount_level_element(self, level):
        del self.level_element_count[level]
        for key in list(self.level_element_count.keys()):
            if(key >level):
                self.level_element_count[key-1] = self.level_element_count.pop(key)

    def clean_skiplist(self):
        pointer = self.top_left_element
        while(pointer.below.after.key == math.inf):
            pointer = pointer.below
            pointer.above = None
            pointer.after.above = None
            self.levels_count = self.levels_count - 1
            self.top_left_element = pointer   
                 

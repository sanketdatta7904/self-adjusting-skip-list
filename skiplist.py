import math
import random

# define custom exception class specially for remove element function if element isnot found
class Exception(Exception):
    pass

# define node class for the skip list
class Node:

    def __init__(self):
        # initialize all four directional pointers and value/key to None
        self.after  = None
        self.above  = None
        self.before = None
        self.below  = None
        self.value  = None
        self.key    = None


class Skiplist:
    def __init__(self):
        # initialize elements count and levels count to 0
        self.elements_count = 0
        self.levels_count = 0
        self.top_left_element = None

        # insert two top level sentinel nodes at the start with one containing negative infinity 
        # and the other containing positive infinity, is to provide boundary conditions. Also to provide
        # efficient access to the beginning and end of the skip list 
        self.insert_top_level()
        self.insert_top_level()

    def insert(self, key, value):
        # start at the top left element and find the element with the given key (if it exists)
        found_element = pointer = self.locate_key(key)

        # if the key already exists, update its value and return the old value
        if found_element.key == key:
            old_value = found_element.value
            found_element.value = value
            return old_value

        # otherwise, increment the element count and insert the new element
        self.elements_count = self.elements_count + 1
        element = self.insert_after_above(pointer, None, key, value)
        count = 1
        while random.random() > 0.5:
            # flip a coin to determine whether to insert a new level
            count = count + 1
            while pointer.above is None:
                pointer = pointer.before

            pointer = pointer.above
            element = self.insert_after_above(pointer, element, key, value)

            if count == self.levels_count:
                self.insert_top_level()

    def remove_element(self, key):
        # start at the top left element and find the element with the given key
        found_element = pointer = self.locate_key(key)

        # remove the element from all levels of the skip list
        while pointer is not None:
            pointer.before.after = pointer.after
            pointer.after.before = pointer.before
            pointer = pointer.above

        # if the key was found, return its value
        if found_element.key == key:
            return found_element.value
        # otherwise, raise a custom exception indicating the key was not found
        else:
            raise Exception('NOT_FOUND')

    def findElement(self, key):
        # start at the top left element and find the element with the given key (if it exists)
        element = self.locate_key(key, exact_match=True)

        # if the key was found, return its value
        return element.value if element else None

    def size(self):
        # return the current element count
        return self.elements_count

    def closestKeyAfter(self, key):
        #  returns the key of the smallest element greater than the given key in the Skip List.
        return self.locate_closest_key(key, 'after')

    def closestKeyBefore(self, key):
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

    def locate_key(self, key, exact_match=False):
        pointer = self.top_left_element
        # Traverse down the skip list until reaching the bottom level
        while pointer.below is not None:
            pointer = pointer.below
        # Traverse right until finding the largest element with a key less than or equal to the given key
            while pointer.after.key <= key:
                pointer = pointer.after
        # If an exact match is required and the found element's key is not equal to the given key, return None else return pointer
        if (exact_match and pointer.key != key ):
            return None 
        else:
            return pointer

    def locate_closest_key(self, key, target):
        # Locate the node with the exact match for the given key
        located_element = self.locate_key(key, exact_match=True)

        # If a node with the exact match is found, return the key of the target element in the desired direction
        if located_element:
            target_element = getattr(located_element, target)
            # Check if the target element is infinity, which means there are no keys after/before the input key
            is_inf = (target_element.value == math.inf or target_element.value == -math.inf)

            if target_element and not is_inf:
                return target_element.key
        # If no node with the exact match is found or if the target element is infinity, return None
        return None

    def insert_top_level(self):
        # Enter a new level with -infinity(left) and +infinity(right) at the top of the skiplist
        self.levels_count = self.levels_count + 1
        self.top_left_element = self.insert_after_above(
            None, self.top_left_element, -math.inf, -math.inf
        )
        self.top_left_element.before = self.insert_after_above(
            self.top_left_element, self.top_left_element.after, math.inf, math.inf
        )

    def insert_after_above(self, after, above, key, value):
        # Takes key and value pair and inserts new node with given level
        # after is the place after which the node should come-- after(left) >> node
        # above is the place above which the node should come-- above(down)>> node(up)
        node = Node()

        node.key        = key
        node.value    = value
        node.before = after
        node.below    = above

        if after is not None:
            node.after = after.after
            after.after = node

        if above is not None:
            node.above    = above.above
            above.above = node

        return node
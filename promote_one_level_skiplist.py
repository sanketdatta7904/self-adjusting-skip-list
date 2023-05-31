from skiplist import Skiplist
import copy
# Skiplist where element is promoted to top level once searched
import math

class Promote_one_level_skiplist (Skiplist):

    def search_and_insert(self, key, value = None):
        pointer, target_key, target_value, level, no_of_ops = self.find_first_occurrence(
            key)
        if(pointer == None):
            no_of_ops = self.insert(key, value)
            self.num_of_comparison = self.num_of_comparison+no_of_ops
        else:
            self.num_of_comparison = self.num_of_comparison+no_of_ops
            key = target_key
            value = target_value
            if (self.levels_count-1 > level):
                found_before = pointer.before
                while(found_before.above is None):
                    found_before = found_before.before
                found_before = found_before.above
                pointer = self.insert_after_above(
                    found_before, pointer, key, value, level)
                testPointer = pointer
                # while(testPointer.key != -math.inf):
                #     testPointer = testPointer.before
                # if(testPointer.below == None):
                #     print("stop")
             
                if(level in self.level_element_count and level-1 in self.level_element_count):
                    if(self.level_element_count[level] == self.level_element_count[level-1]):
                        self.remove_level(level, pointer)

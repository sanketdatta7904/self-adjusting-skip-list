from skiplist import Skiplist
import random
import copy
# Skiplist where element is promoted to top level once searched


class Promote_random_level_skiplist (Skiplist):

    def search_and_insert(self, key, value=None):
        element, target_key, target_value, level, no_of_ops = self.find_first_occurrence(
            key)
        pointer = element
        if(pointer == None):
            no_of_ops = self.insert(key, value)
            self.num_of_comparison = self.num_of_comparison+no_of_ops
        else:
            self.num_of_comparison = self.num_of_comparison+no_of_ops
            key = target_key
            value = target_value
            while (random.random() > 0.5) and (self.levels_count-1 > level):
                # flip a coin to determine whether to insert a new level
                while pointer.above is None:
                    pointer = pointer.before

                pointer = pointer.above
                element = self.insert_after_above(pointer, element, key, value, level)

                if(level in self.level_element_count and level-1 in self.level_element_count):
                    if(self.level_element_count[level] == self.level_element_count[level-1]):
                        self.remove_level(level, pointer)
                    else:
                        level = level +1
                if level >= self.levels_count:
                    self.insert_top_level()

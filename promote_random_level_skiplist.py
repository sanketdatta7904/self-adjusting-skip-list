from skiplist import Skiplist
import random
import copy
# Skiplist where element is promoted to top level once searched


class Promote_random_level_skiplist (Skiplist):

    def find_and_elevate_to_random_levels(self, target_key):
        element, key, value, depth_of_node = self.find_first_occurrence(
            target_key)
        pointer = element
        while (random.random() > 0.5) and (self.levels_count-1 > depth_of_node):
            # flip a coin to determine whether to insert a new level
            depth_of_node = depth_of_node + 1
            while pointer.above is None:
                pointer = pointer.before

            pointer = pointer.above
            element = self.insert_after_above(pointer, element, key, value)

            if depth_of_node >= self.levels_count:
                self.insert_top_level()

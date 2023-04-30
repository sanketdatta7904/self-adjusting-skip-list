from skiplist import Skiplist
import copy
# Skiplist where element is promoted to top level once searched


class Promote_top_skiplist (Skiplist):

    def find_and_promote_to_top(self, target_key):
        # Inserts the element to all the levels untill top
        pointer, key, value, depth_of_node = self.find_first_occurrence(
            target_key)

        while self.levels_count-1 > depth_of_node:
            depth_of_node = depth_of_node + 1

            found_before = pointer.before
            while(found_before.above is None):
                found_before = found_before.before
            found_before = found_before.above
            pointer = self.insert_after_above(
                found_before, pointer, key, value)

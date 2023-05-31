from skiplist import Skiplist


class Basic_skiplist(Skiplist):

    def search_and_insert(self, key, value=None):
        # start at the top left element and find the element with the given key (if it exists)
        pointer, target_key, target_value, depth_of_node, no_of_ops = self.find_first_occurrence(
            key)
        level = depth_of_node
        if(pointer == None):
            no_of_ops = self.insert(key, value)
        self.num_of_comparison = self.num_of_comparison+no_of_ops
            

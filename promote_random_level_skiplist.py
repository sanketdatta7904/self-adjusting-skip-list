from skiplist import Skiplist
import random
import copy
# Skiplist where element is promoted to top level once searched
class Promote_random_level_skiplist (Skiplist):
      
    def findElementImp1(self, key):
        # start at the top left element and find the element with the given key (if it exists)
        element = self.locate_key(key, exact_match=True, first_occur=True)
        depthOfnode = 1
        copyElem = copy.deepcopy(element)
        while(copyElem.below is not None):
            depthOfnode = depthOfnode+1
            copyElem = copyElem.below
        self.insertUntillTop(element,element, element.key, element.value, depthOfnode)
        # if the key was found, return its value
        return element.value if element else None
    
    def insertUntillTop(self, pointer, element, key, value, depthOfNode):
       
       while random.random() > 0.5:
            # flip a coin to determine whether to insert a new level
            depthOfNode = depthOfNode + 1
            while pointer.above is None: 
                pointer = pointer.before

            pointer = pointer.above     
            element = self.insert_after_above(pointer, element, key, value)

            if depthOfNode >= self.levels_count:
                self.insert_top_level()

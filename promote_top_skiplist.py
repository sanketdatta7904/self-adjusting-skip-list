from skiplist import Skiplist
import copy
# Skiplist where element is promoted to top level once searched
class Promote_top_skiplist (Skiplist):
      
    def findElementImp1(self, key):
        # start at the top left element and find the element with the given key (if it exists)
        element = self.locate_key(key, exact_match=True, first_occur=True)
        depthOfnode = 1
        copyElem = copy.deepcopy(element)
        while(copyElem.below is not None):
            depthOfnode = depthOfnode+1
            copyElem = copyElem.below
        self.insertUntillTop(element, element.key, element.value, depthOfnode)
        # if the key was found, return its value
        return element.value if element else None
    
    def insertUntillTop(self, pointer, key, value, depthOfNode):
        # Inserts the element to all the levels untill top
        count = depthOfNode
        while self.levels_count-1>count:
            count = count + 1

            found_before = pointer.before
            while(found_before.above is None):
                found_before = found_before.before
            found_before = found_before.above
            pointer = self.insert_after_above(found_before, pointer, key, value)


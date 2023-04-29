from skiplist import Skiplist
import copy
# Skiplist where element is promoted to top level once searched
class PromoteOneLevelSkiplist (Skiplist):
      
    def findElementImp1(self, key):
        # start at the top left element and find the element with the given key (if it exists)
        element = self.locate_key(key, exact_match=True, first_occur=True)
        self.insertUntillOneLevel(element, element.key, element.value)

    
    def insertUntillOneLevel(self, pointer, key, value):

        found_before = pointer.before
        while(found_before.above is None):
            found_before = found_before.before
        found_before = found_before.above
        pointer = self.insert_after_above(found_before, pointer, key, value)
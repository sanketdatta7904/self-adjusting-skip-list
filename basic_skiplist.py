from skiplist import Skiplist


class Basic_skiplist(Skiplist):

    def find_element(self, key):
        # start at the top left element and find the element with the given key (if it exists)
        element = self.locate_key(key, exact_match=True)

        # if the key was found, return its value
        return element.value if element else None

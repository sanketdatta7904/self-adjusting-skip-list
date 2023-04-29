
from skiplist import  Skiplist
from basic_skiplist import Basic_skiplist
from promote_top_skiplist import Promote_top_skiplist

def test_insert():
        s = Promote_top_skiplist()
        s.insert(5, "five")
        s.insert(2, "two")
        s.insert(8, "eight")
        s.insert(4, "four")
        s.insert(1, "one")
        s.insert(10, "ten")
        s.insert(7, "seven")
        s.insert(6, "six")
        s.display()
        # s.findElementImp1(1)
        s.findElementImp1(5)
        s.display()
        

test_insert()
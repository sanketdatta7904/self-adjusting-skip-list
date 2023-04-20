
from skiplist import  Skiplist

def test_insert():
        s = Skiplist()
        s.insert(5, "five")
        s.insert(2, "two")
        s.insert(8, "eight")
        s.insert(4, "four")
        s.insert(1, "one")
        s.insert(10, "ten")
        s.insert(7, "seven")
        s.insert(6, "six")
        s.display()
test_insert()
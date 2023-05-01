
from skiplist import Skiplist
from basic_skiplist import Basic_skiplist
from promote_top_skiplist import Promote_top_skiplist
from promote_one_level_skiplist import Promote_one_level_skiplist
from promote_random_level_skiplist import Promote_random_level_skiplist
import json

def test_insert():
    s = Promote_one_level_skiplist()
    s.insert(5, "five")
    s.insert(2, "two")
    s.insert(8, "eight")
    s.insert(4, "four")
    s.insert(1, "one")
    s.insert(10, "ten")
    s.insert(7, "seven")
    s.insert(6, "six")
    s.display()
    print(json.dumps(s.level_element_count))
    n = int(input())
    while(n!= 0):
        s.remove_element(n)
        s.display()
        print(json.dumps(s.level_element_count))

        n = int(input())



test_insert()

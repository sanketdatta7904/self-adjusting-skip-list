
from skiplist import Skiplist
from basic_skiplist import Basic_skiplist
from promote_top_skiplist import Promote_top_skiplist
from promote_one_level_skiplist import Promote_one_level_skiplist
from promote_random_level_skiplist import Promote_random_level_skiplist
import json

def test_insert():
    s = Promote_random_level_skiplist()
    s.search_and_insert(5, "five")
    s.search_and_insert(2, "two")
    s.search_and_insert(8, "eight")
    s.search_and_insert(4, "four")
    s.search_and_insert(1, "one")
    s.search_and_insert(10, "ten")
    s.search_and_insert(7, "seven")
    s.search_and_insert(6, "six")
    s.display()
    print(json.dumps(s.level_element_count))
    n = int(input())
    while(n!= 0):
        s.search_and_insert(n)
        s.display()
        print(json.dumps(s.level_element_count))

        n = int(input())



test_insert()

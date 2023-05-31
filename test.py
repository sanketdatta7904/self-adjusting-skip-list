from skiplist import Skiplist, Exception
from basic_skiplist import Basic_skiplist
from promote_one_level_skiplist import Promote_one_level_skiplist


def test_with_option():
    option = 0
    while True:
        print('Enter one of the following options:')
        print('(1 -> Insert, 2 -> Delete, 3 -> Find, 4 -> Display, 5 -> Exit):')
        try:
            option = int(input())
            if option >= 1 and option <= 5:
                return option
        except:
            continue


def test_controller(skiplist):
    while True:
        option = test_with_option()
        if option == 1:
            # insert operation
            st = input(
                'Enter key and value (only integer) separated by a space')
            lst = st.split()
            key = int(lst[0])
            val = int(lst[1])
            oldVal = skiplist.search_and_insert(key, val)
            print('Old value = {}'.format(oldVal))
        elif option == 2:
            # delete operation
            key = int(input('Enter integer key needed be removed: '))
            try:
                val = skiplist.remove_element(key)
                print('Value for key removed = {}'.format(val))
            except Exception:
                print('Key {} does not exist'.format(key))
        elif option == 3:
            # find operation
            key = int(input('Enter integer key to be looked up: '))
            val = skiplist.find_and_elevate_one_level(key)
            if val == None:
                print('Key {} not found'.format(key))
            else:
                print('Value for key {} = {}'.format(key, val))
        elif option == 5:
            # exit
            quit()
        skiplist.display()


test_controller(Promote_one_level_skiplist())

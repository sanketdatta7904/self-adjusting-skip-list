from skiplist import Skiplist, Exception
from basic_skiplist import Basic_skiplist

def testOption():
    option = 0
    while True:
        print('Enter one of the following options:')
        print('(1 -> Insert, 2 -> Delete, 3 -> Find, 4 -> Display, 5 -> Exit):')
        try:
            option = int(input())
            if option >=1 and option <= 5:
                return option
        except:
            continue

def testIntKeyValues(dict):
    while True:
        option = testOption()
        if option == 1:
            # insert operation
            st = input('Enter key and value (only integer) separated by a space')
            lst = st.split()
            key = int(lst[0])
            val = int(lst[1])
            oldVal = dict.insert(key,val)
            print('Old value = {}'.format(oldVal));
        elif option == 2:
            # delete operation
            key = int(input('Enter integer key needed be removed: '))
            try:
                val = dict.remove_element(key)
                print('Value for key removed = {}'.format(val))
            except Exception:
                print('Key {} does not exist'.format(key))
        elif option == 3:
            # find operation
            key = int(input('Enter integer key to be looked up: '))
            val = dict.findElement(key)
            if val == None:
                print('Key {} not found'.format(key))
            else:
                print('Value for key {} = {}'.format(key,val))
        elif option == 5:
            # exit
            quit()
        dict.display()

testIntKeyValues(Basic_skiplist())
from skiplist import Skiplist, Exception
from basic_skiplist import Basic_skiplist
from promote_one_level_skiplist import Promote_one_level_skiplist
from promote_top_skiplist import Promote_top_skiplist
from promote_random_level_skiplist import Promote_random_level_skiplist


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
            # insert operation(WITH PROMOTION)
            st = input(
                'Enter key and value (only integer) separated by a space')
            lst = st.split()
            key = int(lst[0])
            val = int(lst[1])
            oldVal = skiplist.search_and_insert(key, val)
            print('Old value = {}'.format(oldVal))
            skiplist.display()

        elif option == 2:
            # delete operation
            key = int(input('Enter integer key needed be removed: '))
            try:
                val = skiplist.remove_element(key)
                print('Value for key removed = {}'.format(val))
            except Exception:
                print('Key {} does not exist'.format(key))
            skiplist.display()

        elif option == 3:
            # Exclusively find operation(No PROMOTION)
            key = int(input('Enter integer key to be looked up: '))
            val = skiplist.locate_key(key, True, True)
            if val == None:
                print('Key {} not found'.format(key))
            else:
                print('Value for key {} = {}'.format(key, val[0].value))
        elif option == 5:
            # exit
            quit()

if __name__ == '__main__':
    print("Starting the Skiplist experiment")
    print("Please enter which kind of skiplist you want to try")
    print("Example: 1/2/3/4")
    print("1: Basic skiplist \n2. Promote one level up\n3. Promote to top level\n4. Promote to random level")
    choice = int(input())
    if(choice == 1):
        print("You chose basic skiplist")
        test_controller(Basic_skiplist())
    elif(choice == 2):
        print("You chose Promote one level up skiplist")
        test_controller(Promote_one_level_skiplist())
    elif(choice == 3):
        print("You chose Promote to top level skiplist")
        test_controller(Promote_top_skiplist())
    elif(choice == 4):
        print("You chose Promote to random level skiplist")
        test_controller(Promote_random_level_skiplist())

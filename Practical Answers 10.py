#Question 1
def is_sorted(my_list) :
    """This function returns is_sorted if each element in the list is greater
than or equal to the element before it"""
    for i in range(1, len(my_list)) :
        if my_list[i] < my_list[i-1] :
            return False
    return True

if __name__ == "__main__" :
    def test_is_sorted( a_list, expected ) :
        if is_sorted(a_list) == expected :
            print "Success: , a_list, ( is if expected else "is not"),\
                  "sorted, as expected"
        else :
            print "FAILURE: ", a_list, "returned", r, "expected", expected
#Question 2

list_one = [x for x in range(1,10)]
list_two = [x for x in range(2, 20, 2)]


def chop(my_list):
    last_item_index = len(my_list) - 1  # adjust for 0th index
    del my_list[last_item_index]
    del my_list[0]
    return None

print list_one, id(list_one)
print "chop() returns:", chop(list_one)
print "chop chop..."
print list_one, id(list_one), "\n"

#Question 3

def middle(my_list):
    return my_list[1:(len(my_list) - 1)]
print list_two, id(list_two)
new_list = middle(list_two)
print "middle() returns: ", new_list
print new_list, id(new_list)


#Question 4

data = []

for i in range (2000,3201):
    if ( i%7 == 0 ) and ( i%5 != 0):
        data.append(i)

for i in data:
    print(i , end= ',')
#Question 5

def throws():
	    return 5/0


	try:
	    throws()
	except ZeroDivisionError:
	    print "division by zero!"
	except Exception, err:
	    print 'Caught an exception'
	finally:
	    print 'In finally block for cleanup'

#Question 6

b = int(input("Input the base : "))
h = int(input("Input the height : "))

area = b*h/2

print("area = ", area)

#Question 7

def hours():
print('Open 9-5 daily')
import zoo
zoo.hours()
Open 9-5 daily

#Question 8

import zoo as menagerie
menagerie.hours()
Open 9-5 daily

#Question 9

from zoo import hours as info
info()
Open 9-5 daily

#Question 10

def has_duplicates(my_list):
    i = 0
    while i < len(my_list):
        if my_list.count(my_list[i]) > 1:
            return True
        elif i == (len(my_list) - 1):
            return False
        i += 1


#Question 11

def generate_random_birthdays():
    return [random.randint(1, 365) for student in range(NUMBER_OF_STUDENTS)]

def stats(TRIALS):

    duplicate_count = 0
    for i in range(TRIALS):
        if has_duplicates(generate_random_birthdays()):
            duplicate_count += 1
    print "In %d classrooms with %d students, %.1f%% had students\
 with duplicate birthdays." % (TRIALS, NUMBER_OF_STUDENTS, (float(duplicate_count) / TRIALS) * 100)

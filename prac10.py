#Student number: 19077424
#Prac 10

#Question1
def is_sorted(x) :
    for i in range(1, len(x)) :
        if x[i] < x[i-1] :
            return False
    return True

#Question 2

def chop(z):
    last_item_index = len(z) - 1 
    del z[last_item_index]
    del z[0]
    return None
print(chop([1,2,3,a]))

#Question 3

numlist_1 = [a for a in range(1,20)]
numlist_2 = [b for b in range(2, 20, 2)]

def middle(e):
    return e[1:(len(e) - 1)]

print( list_2, id(list_2))

new_list = middle(list_2)

print("middle() returns: ", new_list)
print(new_list, id(new_list))

#Question 4

num_List = []

for n in range (2000,3201):
    if ( n%7 == 0 ) and ( n%5 != 0):
        num_List.append(n)

for n in num_List:
    print(n ,',')
    
#Question 5
    
def catchE():
	    return 5/0
	
	try:
	    catchE()
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

#Question 8

import zoo as menagerie
menagerie.hours()

#Question 9

from zoo import hours as info
info()

#Question 10

def has_duplicates(h):
    c = 0
    while c < len(h):
        if h.count(h[c]) > 1:
            return True
        elif c == (len(ht) - 1):
            return False
        c += 1

#Question 11
def gbirthdays():
    return [random.randint(1, 365) for p in range(num_student)]

def stats(v):

    cnt = 0
    for u in range(v):
        if has_duplicates(gbirthdays()):
            cnt += 1
    print "In %d classrooms with %d students, %.1f%% had students\
 with duplicate birthdays." % (v, num_student, (float(cnt) / v) * 100)


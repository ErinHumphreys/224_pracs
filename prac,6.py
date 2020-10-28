
#Question 1
# Store the numbers 78, 89 and 56 in a list. Using conditionals, determine whether the number
# 81 is larger than all three of the numbers
numbers = [78,89,56]
count  = 0
##while count <= 2:
##     if numbers(count) <81:
##       print("false")
##       count += 1
##     else:
##         print("true")

while count < len(numbers):
    number = numbers[count]
    if number <= 81 :
        print("false")
        break
    count += 1
else:
    print("true")



#Question 2
# Make a list of names that includes at least four people. Write an if test that prints a message
# about the room being crowded, if there are more than three people in your list. if there are
# exactly three people in the room, print a message about the room being just right. If there are
# less than 3 people in the room print a message about the room being a bit too empty.

names = ['erin','stevie','cleo','randy']
if len(names) > 3:
    print('more than 3 people in the room')
if len(names) == 3:
    print('there are exactly 3 people in the room, the room is perfectly occupied')
if len(names) < 3:
    print('room is abit empty')



#Question 3
##input number : "enter a number between 0 and 100"
# Choose a number between 0 and 100. Create a series of nested if statements to determine
# whether number is between 0 and 30, 31 and 50, 51 and 75 or greater than 75.

new_number = int(input("enter a number between 0 and 100 "))
if new_number > 0 and new_number < 30:
    print('number is between 0 and 30')
if new_number > 31 and new_number < 50:
    print('number is between 31 and 50')
if new_number > 51 and new_number <75:
    print('number is between 51 and 75')
if new_number > 75:
    print('number is greater than 75')

#Question 4
# Choose a number between 0 and 1000. Write an expression that tests if the number chosen is
# even or a multiple of 5, or both.

user_number = int(input("enter a number between 0 and 1000 "))
if user_number % 5 ==0:
    print('true')
else:
    print('false')

#Question 5
# Create a variable storing your name. Determine the length of your name. If your name is
# longer than 10 characters output “I have a long name”, if not output “my name is short”.
# user_name = str(input("enter your name "))

if len(user_name) > 10:
    print('I have a long name')
else:
    print('my name is short')

#Question  6
# Write a program that takes a list and creates a new list that contains all the elements of the first
# list minus all the duplicates.

cars = [nissan, honda, bmw, benz, toyota]
new_cars = list(set(cars))
print(new_cars)

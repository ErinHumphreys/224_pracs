
#Question 1

# Write a function named right_justify that takes a string named s as a parameter and prints the
# string with enough leading spaces so that the last letter of the string is in column 70 of the
# display.

def right_justify(s):
    print( "%70s" % s)

#Question 2

# If you are given three sticks, you may or may not be able to arrange them in a triangle. For
# example, if one of the sticks is 12 inches long and the other two are one inch long, it is clear
# that you will not be able to get the short sticks to meet in the middle. For any three lengths,
# there is a simple test to see if it is possible to form a triangle:
# “If any of the three lengths is greater than the sum of the other two, then you cannot form a
# triangle. Otherwise, you can”
# Write a function named is_triangle that takes three integers as arguments, and that prints
# either “Yes” or “No,” depending on whether you can or cannot form a triangle from
# sticks with the given lengths.

def is_triangle(a,b,c):
    if(a>b+c) or (b>a+c) or (c>a+b):
        print('no')
    else:
        print('yes')

#Question 3

# Write a function that prompts the user to input three stick lengths, converts them to
# integers, and uses is_triangle to check whether sticks with the given lengths can form a
# triangle.

def is_triangle():
    a= int(raw_input("enter a"))
    b= int(raw_input("enter b"))
    c= int(raw_input("enter c"))

    if is_triangle(a,b,c):
        print('a,b,c is a triangle')
    else:
        print('a,b,c is not a triangle')

#Question 4

# Write a function to sum three given integers. However, if two values are equal sum will be
# zero.

def total_sum():
    if (a==b) or (b == c) or (a==c):
        total_sum = 0
    else:
        total_sum = a+b+c

#Question 5
# Write a Python program to get the largest number from a list of 5 values inputted by the user

#Question 6
# Write a function that takes a character (i.e. a string of length 1) and returns True if it is a vowel,
# False otherwise.

def vowel_checker(x):
    if x == 'a' or 'e' or 'i' or 'o' or 'u':
        return "True"
    else:
        return "False"

#Question 7:
# Define a function is_palindrome() that recognizes palindromes (i.e. words that look the same
# written backwards). For example, is_palindrome("radar") should return True and
# is_palindrome(“programming” should return False)

def palindrome(word):
    if len(word) <= 1:
        return True
    if word[0] == string(len(word)-1):
        return palindrome(word[1:len(string-1]))
    else:
        return False

#Question 8
# Define a function histogram() that takes a list of integers and prints a histogram to the screen.
# For example, histogram([4, 9, 7]) should print the following:

def histogram(l):
    for v in range(len(l)):
        print(l[v] * '*')
    List = [4,9,7]
    histogram(List)


#Question 1
def good(a,b,c):
    return [a,b,c]

print(good('Harry','Ron','Hermione'))

#Question 2
word = 'banana'

def count(z,x):
  counter = 0
  for letter in word:
        if letter == 'a':
            counter = counter +1

  print(counter)
print(count(word,'a'))

#Question 3

def calc(number):
    return (number**2)

usernum = input('please enter a number to be squared: ')
print(calc(usernum))

#Question 4

def calc1(number1,number2):
    return number1**number2

usernum1 = input('please enter a number to be squared: ')
usernum2 = input('please enter another number to be the exponent: ')
print(calc1(usernum1,number2))

#Question 5


def new_calc(num1,num2):
    return num1 + num2
user1=int(input('enter a number:'))
user2 - int(input('enter another number:'))

print(new_calc(user1,user2))

#Question 6

def integer(answer):
    user_num = input('Enter any number: ')
    if user_num % 2 ==0:
        return 'Number is equal.'+ answer
    else:
        return 'Number is not equal' + answer



#Question 7

def new_list(x):
    return [x]
print(new_list(good('Harry','Ron','Hermione'),count(word,'a'),calc(usernum),calc1(usernum1,number2),new_calc(user1,user2),integer()))


#Question 8


#Question 1
e2f = {'dog':'chien', 'cat':'chat', 'walrus' : 'morse'}
print(e2f)

#Question 2
print(e2f['walrus'])

#Question 3
f2e = {a:b for b,a in e2f.items()}
print(f2e)

#Question 4
print(f2e['chien'])

#Question 5
life = {'animals' :{
        'cats' : ['Henri','Grumpy','Lucy'] ,
        'octopi' : {} ,
        'emus' : {}},
        'plants' : {},
        'other' : {}}

#Question 6
print(life.keys())

#Question 7
print(life['animals'])

#Question 8
print(life['animals']['cats'])

#Question 9
name =  input("Enter your name: " )
age = int (input("Whats your age: "))
year =  (2017 - age) + 100
print(name , "You will turn a 100 in: ", year  )

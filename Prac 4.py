
#Question 1
color_list= ["Red","Green", "White","Black"]
print(color_list[0:4:3])

#Question 2
fruit1 = ["Apples","Orange","Peaches","Nectarines"]
fruit = fruit1[3]
fruit1.pop()
"Nectarines"
fruit1.insert(0,fruit)
print(fruit1)

#Question 3
languages = ["java","haskell", "Go","Python"]
animals = ["pigeon","python","shark"]
names = ["Johan","Frank", "Sarah"]
print("Pyhton" in languages)

print("Python" in animals)

print("Python" in names)

#Question 4
names = ['Groucho', 'Chico', 'Mario', 'Harpo', 'Gummo', 'Zeppo', 'Harry', 'Mario', 'Mariah', 'Jeffrey','Mario', 'Solomon', 'Mario', 'Mario']
print(names.count('Mario'))

#Question 5
scores = [87, 34, 65,32, 78, 43, 98, 23, 65, 87, 43, 56, 38, 38, 78]
scores.sort()
scores_new = scores
print(scores_new)

#Question 6
scores.sort(reverse = True )
print(scores)

#Question 7
values = ["lamp", "car", "mustache", "bread", "salad", "cheese", "paint","chair"]
food = values[3:6]
print(food)

#Question 8
extras = ["egg","bacon"]
food.extend(extras)
print(food)

#Question 9
a = [5, 10, 15, 20, 25]
b = a[::3]
print(b)

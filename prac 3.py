guess_me = 7
start = 1

while guess_me < 10:
    if start == guess_me:
        print("Winner!!")
        break;
    elif start < guess_me:
        print("Too Low")
        start +=1
    elif start > guess_me:
        print("Too high")
        start+=1


name= "Erin"
for x in reversed(name):
    print(x)
new_list = []
for s in range(1,21):
    new_list.append(s**2)
print(new_list)    

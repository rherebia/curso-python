import random

myRandomList = []

for i in range(25) :
    myRandomList.append(random.randrange(1,100,1))
    
print(myRandomList)
print("Quantity of items in list: ", len(myRandomList))
print("Test Multidimensional Sequence")

myTableTuple = ( (1, 2, 3), (4, 5, ), (6, 7, 8) )

print("Values in table tuple")

for row in myTableTuple :
    for item in row :
        print(item, end=" ")
    print()
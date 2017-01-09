print("Test Multidimensional Sequences")

myTableList = [ [1, 2, 3], [4, 5, 6], [7, 8, 9] ]

print("Value in table list")

for row in myTableList :
    for item in row :
        print(item, end=" ")
    print()
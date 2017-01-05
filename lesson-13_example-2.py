print("Test Lists")

myNewList = []

myNewList.insert(0, 'Euclides')
myNewList.insert(3, 'Devmedia')
myNewList.insert(1, 'Curitiba')
myNewList.insert(2, 'Rio de Janeiro')

print("Position 0: ", myNewList[0])
print("Position 1: ", myNewList[1])
print("Position 2: ", myNewList[2])
print("Position 3: ", myNewList[3])

myNewList[1] = 987

print("Position 1 (new value): ", myNewList[1])

print("Quantity: " len(myNewList))
print("Sorting and Searching Lists")

myList = [34,5,2,85,99,15,1,74,85,93,44,7,69,1,85]

print("\nItems in original order: ")

for item in myList :
    print(item,)
    
myList.sort()

print("\nItems after sorting: ")

for item in myList :
    print(item,)

myList.reverse()

print("\nItems after reverse sorting: ")

for item in myList :
    print(item,)

print("\nSize of list: ", len(myList))
print("\nCount items in list: ", myList.count(85))
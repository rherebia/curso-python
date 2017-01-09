print("Sorting and Searching Lists")

myListOfStrings = ["Euclides", "Devmedia", "Python", "Programming", "Hello", "World", "List", "Search", "Course"]

searchString = input("Type search string: ")

if searchString in myListOfStrings :
    print("Found at index: ", myListOfStrings.index(searchString))
else :
    print("Not found")
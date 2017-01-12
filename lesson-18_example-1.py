print("Test Dictionaries Methods")

myMonthsDictionary = { 1:"January", 2:"February", 3:"March", 4:"April", 5:"May", 6:"June", 7:"July", 8:"August", 9:"September", 10:"October", 11:"November", 12:"December" }

print("The myMonthsDictionary items are: ", myMonthsDictionary.items())

print("The myMonthsDictionary keys are: ", myMonthsDictionary.keys())

print("The myMonthsDictionary values are: ", myMonthsDictionary.values())

print("The quantity of items are: ", len(myMonthsDictionary))

myInput = input("Type your birthday month: ")
myInput = int(myInput)

if myInput in myMonthsDictionary :
    print("Your birthday month is: ", myMonthsDictionary[myInput])
else :
    print("Month not exists")
    
newCopiedDictionary = myMonthsDictionary.copy()
newCopiedDictionary[3] = "nothing"

print("Copied dictionary:\n", newCopiedDictionary)
print("Source dictionary:\n", myMonthsDictionary)

newUpdateDictionary = {0:"Nothing", 13:"Out of range"}
myMonthsDictionary.update(newUpdateDictionary)

print(myMonthsDictionary)

myMonthsDictionary.clear()

print(myMonthsDictionary)
print("The quantity of items are: ", len(myMonthsDictionary))
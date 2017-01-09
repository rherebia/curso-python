print("Test Dictionary")

myDictionaryHeight = { "Euclides":1.86, "Silva":1.73, "João":1.92, "Pereira":1.67 }

print("All Height: ", myDictionaryHeight)

print("\nSilva current height: ", myDictionaryHeight["Silva"])

myDictionaryHeight["Silva"] = 1.78

print("\nSilva NEW current height: ", myDictionaryHeight["Silva"])

myDictionaryHeight["Marcos"] = 1.63

print("Dictionary after insert: ", myDictionaryHeight)

del myDictionaryHeight["Pereira"]

print("Dictionary after delete: ", myDictionaryHeight)
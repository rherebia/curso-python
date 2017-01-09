print("Test Dictionary")

def histogram(text) :
    myDictionary = dict()
    for c in text :
        if c not in myDictionary :
            myDictionary[c] = 1
        else :
            myDictionary[c] += 1
    return myDictionary

def print_histogram(dictionary) :
    for c in dictionary :
        print(c, dictionary[c])
    
result = histogram("Devmedia is a great company to learn programming")

print_histogram(result)
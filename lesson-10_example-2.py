print("Test of Functions")

def factorial(n) :
    if n == 1 :
        return 1
    else :
        result = n * factorial(n - 1)
        print("intermediate result for ", n, ": ", result)
        return result
        
number = input("Type the number: ")
number = int(number)

print("Final result: ", factorial(number))
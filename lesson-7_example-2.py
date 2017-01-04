print("Test WHILE")

factorial_number = input("Enter with number: ")
factorial_number = int(factorial_number)

if factorial_number > 0 :
    step = factorial_number
    total = factorial_number
    
    while step > 1 :
        step = step - 1
        total = total * step
        
    print("The factorial of %d is %d" % (factorial_number,total))
elif factorial_number == 0 :
    print("The factorial of 0 is 1")
else :
    print("Not exists factorial of negative number")
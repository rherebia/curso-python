print ("Test Equality and Relational Operators")

number1 = input("Enter first number: ")
number1 = int(number1)

number2 = input("Enter second number:   ")
number2 = int(number2)

if number1 == number2 :
    print ("%d is equal to %d" % (number1, number2))
    
if number1 != number2 :
    print ("%d is not equal to %d" % (number1, number2))
    
if number1 < number2 :
    print ("%d is less than %d" % (number1, number2))
    
if number1 > number2 :
    print ("%d is greater than %d" % (number1, number2))
    
if number1 <= number2 :
    print ("%d is less than or equal %d" % (number1, number2))
    
if number1 >= number2 :
    print ("%d is greater than or equal %d" % (number1, number2))
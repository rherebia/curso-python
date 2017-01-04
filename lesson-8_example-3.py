print("Teste FOR - sum odd numbers")

total = 0

number = input("Enter with number ")
number = int(number)

if (number % 2) == 0 :
    number = number -1
    
for i in range(number, 0, -2) :
    total = total + i
    print("i is", i)
    
print("the sum of odd numbers is ", total)
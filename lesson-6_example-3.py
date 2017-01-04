print ("Teste IF / ELSE")

grade1 = input("Enter your grade: ")
grade1 = int(grade1)

if grade1 >= 7 :
    print("Your PASS!")
    
    if grade1 >= 9 :
        print("Your grade is A")
    elif grade1 >= 8 :
        print("Your grade is B")
    elif grade1 >= 7 :
        print("Your grade is C")
else :
    print("NOT PASS")
print ("Teste IF / ELSE")

grade1 = input("Enter your grade: ")
grade1 = int(grade1)

if grade1 >= 9 :
    print("Your grade is A")
    print("Congratulation")
elif grade1 >= 8 :
    print("Your grade is B")
    print("Good")
elif grade1 >= 7 :
    print("Your grade is C")
    print("Maybe")
elif grade1 >= 6 :
    print("Your grade is D")
    print("Bad")
else :
    print("Your grade is E")
    print("Oh No")
    
print ("The End")
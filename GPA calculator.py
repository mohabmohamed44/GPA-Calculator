print("Enter Marks obtained in 5 Subjects")
input("Name of your 1st subject: ")
markOne = int(input("Degree: "))
input("Name of your 2nd subject: ")
markTwo = int(input("Degree: "))
input("Name of your 3rd subject: ")
markThree = int(input("Degree: "))
input("Enter name of your 4th Subject: ")
markFour = int(input("Degree: "))
input("Enter name of your 5th subject: ")
markFive = int(input("Degree: "))

print("Your total degree: ")
total = (((markOne + markTwo + markThree + markFour + markFive) / 500) * 4)
print(total)

if 3.5 <= total <= 4:
    print("Your Grade is A1")
elif 3.1 <= total < 3.4:
    print("Your Grade is A2")
elif total >= 3 and total < 3:
    print("Your Grade is B1")
elif 2.5 <= total < 2.9:
    print("Your Grade is B2")
elif 2 <= total < 2.4:
    print("Your Grade is C1")
elif 1.5 <= total < 1.9:
    print("Your Grade is C2")
elif total >= 1 and total < 1:
    print("Your Grade is D")
elif total >= 0 and total < 0:
    print("Your Grade is E1")

else:
    print("Invalid Input!")

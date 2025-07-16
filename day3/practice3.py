#if, else, and elif statements
#Comparison operators
#Indentation
#Nested conditions
#Practice problems
age =  int(input("Enter Your Age:"))
if age > 18:
    print("You are Adult")
else:
    print("You are Not Adult")
# Indentation is IMPORTANT
num = 6
if num > 5:
    print("Number Greater than 5")
    print("Inside the if block")
print("Outsid the if Block")
#elif Statement (else if)
marks = float(input("Enter Your Marks:"))
if marks >= 90:
    print("Grade A")
elif marks >=80:
    print("Grade B")
elif marks >=70:
    print("Grade C")
else:
    print("Grade F")
#Nested Conditions
v_age = int(input("Enter Your Age:"))
v_country = str(input("Enter Your Country:"))
if v_country.lower()=='pakistan':
    if v_age >= 18:
        print("You can Vote")
    else:
        print("You are Too Young to Vote")
else:
    print("only Pakistani Citizen Votes here!")
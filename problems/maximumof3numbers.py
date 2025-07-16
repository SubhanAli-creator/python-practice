#Maximum of Three Numbers
def largest(num1,num2,num3):
    if num1==num2==num3:
        print("All Numbers are Equal")
    elif num1>num2 and num1>num3:
        print(f'Number {num1} is Maximum')
    elif num2>num1 and num2>num3:
        print(f'Number {num2} is Maximum')
    else:
        print(f'Number {num3} is Maximum')
num1 = float(input("Enter Number 1:"))
num2 = float(input("Enter Number 2:"))
num3 = float(input("Enter Number 3:"))
largest(num1,num2,num3)
#Built in  Method
#print(f"Maximum number is: {max(num1, num2, num3)}")
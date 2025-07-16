#Multiplication Table
def table(digit):
    for i in range(1,11):
        print(f'{digit}*{i}={digit*i}')
digit = int(input("Enter the Number to Print Table:"))
table(digit)
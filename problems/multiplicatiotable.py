#Multiplication Table
def table(digit, upto=10):
    for i in range(1, upto + 1):
        print(f'{digit} * {i} = {digit * i}')

digit = int(input("Enter the number: "))
upto = int(input("Print table up to: "))
table(digit, upto)

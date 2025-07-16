#Sum of All Digits
def sum_of_digit(digit):
    digit = abs(digit)
    total = 0
    while digit > 0:
        single = digit%10
        digit//=10
        sum+=single
    return total
number = int(input("Enter Your Number: "))
print(sum_of_digit(number))
        

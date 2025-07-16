#Even Odd Check
def check_even_odd(num):
    return "EVEN" if num%2==0 else "ODD"
num = int(input("Enter Your Number: "))
print(check_even_odd(num))
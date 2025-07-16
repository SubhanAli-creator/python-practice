def palindrome(text):
    return text == text[::-1]
text = str(input("Enter Your Text:")).lower()
print("Palindrome") if palindrome(text) else print("Not Palindrome")

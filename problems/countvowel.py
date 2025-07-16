#Count Vowels in String
def count_vowel(text):
    total = 0
    vowels = ['a','e','i','o','u']
    for x in text.strip():
        if x.lower() in vowels:
            total+=1
    return total
text = str(input("Enter Text: "))
print(count_vowel(text))
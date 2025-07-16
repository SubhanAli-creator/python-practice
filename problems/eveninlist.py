#Find Even Elements in List
def even_list(lst):
    n_list = [x for x in lst if x%2==0]
    return n_list
lst = [2, 5, 8, 11, 14]
result = even_list(lst)
print("Even numbers:", result if result else "None")
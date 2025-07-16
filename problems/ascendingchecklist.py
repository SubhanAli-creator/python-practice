#Check if List is Sorted (Ascending)
def is_sorted(lst):
    is_sorted = True
    for i in range(len(lst)-1):
        if lst[i] > lst[i+1]:
            return False
    return True
lst = [1,2,3,4,5]
print("Sorted" if is_sorted(lst) else "Not Sorted")
   
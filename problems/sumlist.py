#Sum of All Elements of List
def sum_of_list(lst):
    sum = 0
    for i in range(len(list)):
        sum+=lst[i]
    return sum
lst = [1,2,3,4,5]
print(f'Sum of list is : {sum_of_list(lst)}')
    
    
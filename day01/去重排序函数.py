


def sort(lst):
    new_lst = sorted(set(lst))
    return new_lst

lst = [1,2,1,1,2,6,3,2,5,4,4]
print(lst)
print(sort(lst))
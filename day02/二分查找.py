def find(lst,x):
    left = 0
    right = len(lst) - 1
    while left < right:
        mid = (left + right) // 2
        if lst[mid] < x:
            left = mid + 1
        elif lst[mid] > x:
            right = mid -1
        else:
            return mid

lst = [1,2,3,4,5,6,7,8,9]
x = 3
print(find(lst,x))

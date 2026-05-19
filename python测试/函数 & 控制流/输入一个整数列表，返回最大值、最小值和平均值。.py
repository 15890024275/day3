def sort(lst):
    min = lst[0]
    max = lst[0]
    avg = 0
    sum = 0
    for i in lst:
        if min > i:
            min = i
        if max < i:
            max = i
        sum += i
        avg = sum / len(lst)
    return (f"最小值{min},最大值{max},平均值{avg}")

lst = [1,2,3,4,5,6]
print(sort(lst))

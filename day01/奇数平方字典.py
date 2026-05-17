nums = [1,2,3,4,5,6]
dict = {}
for num in nums:
    if num % 2 == 0:
        dict[num] = "偶"
    else:
        dict[num] = "奇"

print(dict)


student = {"zhangsan" : 91,"lisi" : 93,"wangwu" : 96}

lst = [(name,score) for name,score in student.items()]
max_score = lst[0][1]
max_name = ""
for s in lst:
    if s[1] > max_score:
        max_score = s[1]
        max_name = s[0]
print(f"{max_name}同学的成绩最好是{max_score}")


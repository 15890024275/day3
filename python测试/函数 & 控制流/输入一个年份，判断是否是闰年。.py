def years(n):
    if n % 4 == 0 and n % 100 != 0 or n % 400 == 0:
        return f"{n}是闰年"
    else:
        return f"{n}不是闰年"


print(years(2020))
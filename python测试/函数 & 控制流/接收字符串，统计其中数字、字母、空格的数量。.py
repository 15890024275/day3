def count_chars(s):

    digits = 0

    letters = 0

    spaces = 0

    for char in s:

        if char.isdigit():  # 判断是否是数字

            digits += 1

        elif char.isalpha():  # 判断是否是字母

            letters += 1

        elif char.isspace():  # 判断是否是空格

            spaces += 1

    return f"数字: {digits}, 字母: {letters}, 空格: {spaces}"

# 测试

s = "Hello 123 你好"

print(count_chars(s))
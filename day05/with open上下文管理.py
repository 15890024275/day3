with open("a.txt","a",encoding="utf-8") as f:
    f.write("hello")

with open("a.txt","r",encoding="utf-8") as f:
    print(f.read())
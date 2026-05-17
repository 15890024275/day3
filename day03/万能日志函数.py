from datetime import datetime


def logs(*args,**kwargs):
    time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    msg = " ".join(map(str,args))
    return (f"[{time}] {msg}")

def main():
    result = logs("小明登陆")
    print(result)

if __name__ == "__main__":
    main()

from random import random
import time
from functools import wraps


def retry(max_retires,base_delay,max_delay):
    def decorator(func):
        @wraps(func)
        def wrapper(*args,**kwargs):
            retires = 0
            try:
                return func(*args,**kwargs)
            except Exception as e:
                while retires < max_retires:
                    retires = retires + 1
                    delay = min(base_delay * (2 ** retires),max_delay)
                    print(f"正在进行{retires}次重试，请稍后再试。。。")
                    time.sleep(delay)
                raise Exception(f"尝试{retires}次后，仍然失败了")
        return wrapper
    return decorator

@retry(max_retires=3,base_delay=1,max_delay=8)
def main():
    if random.random()<0.9:
        return ValueError("任务失败")
    return "任务成功"

if __name__ == "__main__":
    try:
        result = main()
        print(result)
    except Exception as e:
        print(e)


import asyncio




async def task(name,sec):
    print(f"{name}开始")
    await asyncio.sleep(sec)
    print(f"{name}结束")
    return name

async def main():
    result = await asyncio.gather(
        task("a",2),
        task("b",3)

    )
    print(result)

asyncio.run(main())
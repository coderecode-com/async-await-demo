import asyncio


async def main(name):
    print('hello')
    await asyncio.sleep(1)
    print(name)


asyncio.run(main('upendra'))
# asyncio.run(main('world'))

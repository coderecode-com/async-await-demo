import asyncio


# coroutine
async def main(name):
    print('hello')
    await asyncio.sleep(1)
    print(name)

# main('Upendra')
print(main('Upendra'))


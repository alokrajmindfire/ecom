import asyncio
import aiohttp

async def greet():
    print("Hello...")
    await asyncio.sleep(1)
    print("World!")

asyncio.run(greet())

async def say_hello():
    print("Hello")
    await asyncio.sleep(1)

async def main():
    await say_hello()
    print("Done!")

asyncio.run(main())


async def task(name):
    print(f"Starting {name}")
    await asyncio.sleep(2)
    print(f"Finished {name}")

async def mainAsync():
    await asyncio.gather(task("A"), task("B"), task("C"))

asyncio.run(mainAsync())


def simple_coroutine():
    value = yield
    print("Received:", value)

coro = simple_coroutine()
next(coro)
coro.send("Hello Coroutine!")





async def fetch_data(session, url):
    async with session.get(url) as response:
        print(f"Fetching from {url}")
        data = await response.json()
        return data

async def mainApi():
    urls = [
        "https://jsonplaceholder.typicode.com/users",
        "https://jsonplaceholder.typicode.com/posts",
        "https://jsonplaceholder.typicode.com/comments"
    ]

    async with aiohttp.ClientSession() as session:
        tasks = [fetch_data(session, url) for url in urls]
        results = await asyncio.gather(*tasks)

    print("\nAll data fetched successfully!")
    for i, res in enumerate(results, start=1):
        print(f"🔹 Response {i}: {len(res)} items")

asyncio.run(mainApi())

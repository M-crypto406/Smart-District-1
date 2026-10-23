import asyncio
import os


async def source_one():
    await asyncio.sleep(1)
    return 100

async def source_two():
    await asyncio.sleep(1)
    return 200

async def source_three():
    await asyncio.sleep(1)
    return 300

async def main():
    results = await asyncio.gather(
        source_one(),
        source_two(),
        source_three(),
        return_exceptions=True
    )

    total = 0

    for result in results:
        if isinstance(result, Exception):
            print("Source failed:", result)
        else:
            total += result

    print("Environment:", os.getenv("APP_ENV", "development"))
    print("Source results:", results)
    print("Combined total:", total)

asyncio.run(main())
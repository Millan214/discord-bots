from bot import run_bot
from client import run_client
import asyncio
import os
import sys

sys.path.append(os.path.dirname(os.path.abspath(__file__)))


os.chdir(".")

async def main():
    await asyncio.gather(run_bot(), run_client())

asyncio.run(main())
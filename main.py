from project.bot import run_bot
from project.client import run_client
import asyncio
import os

os.chdir("./project")

async def main():
    await asyncio.gather(run_bot(), run_client())
 
asyncio.run(main())
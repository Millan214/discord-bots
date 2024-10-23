import discord
from discord.ext import commands
import os
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv('DISCORD_BOT_TOKEN')
VOICE_CHANNEL_ID = int(os.getenv('VOICE_CHANNEL_ID'))
TEXT_CHANNEL_ID = int(os.getenv('TEXT_CHANNEL_ID'))
JAMON_ROLE_ID = int(os.getenv('JAMON_ROLE_ID'))
COMMAND_PREFIX = os.getenv('COMMAND_PREFIX')

bot = commands.Bot(command_prefix=COMMAND_PREFIX, intents=discord.Intents.all())

# Basic bot event example
@bot.event
async def on_ready():
    print(f'Bot: {bot.user} is now online!')

async def load_commands():
    print("\nLoading bot commands ...\n")
    # Load Cogs (extensions) dynamically
    for filename in os.listdir('./commands'):
        if filename.endswith('.py'):
            try:
                await bot.load_extension(f'commands.{filename[:-3]}')
            except Exception as e:
                print(f'Failed to load extension {filename}: {e}')

async def run_bot():
    print("ola")
    await load_commands()
    await bot.start(TOKEN)

import discord
import os
import asyncio
import webserver
from dotenv import load_dotenv

load_dotenv()

intents = discord.Intents.default()
intents.members = True  # Ensure the bot can track member activities
intents.voice_states = True  # Track voice channel activity

client = discord.Client(intents=intents)

TOKEN = os.getenv('DISCORD_BOT_TOKEN')
VOICE_CHANNEL_ID = int(os.getenv('VOICE_CHANNEL_ID'))
TEXT_CHANNEL_ID = int(os.getenv('TEXT_CHANNEL_ID'))
JAMON_ROLE_ID = int(os.getenv('JAMON_ROLE_ID'))

@client.event
async def on_ready():
    print(f'Logged in as {client.user}')

@client.event
async def on_voice_state_update(member, before, after):
    # Check if the member joins the specific voice channel
    if after.channel and after.channel.id == VOICE_CHANNEL_ID:
        channel = client.get_channel(TEXT_CHANNEL_ID)
        voice_channel = client.get_channel(VOICE_CHANNEL_ID)
        voice_channel_num_members = len(voice_channel.members)
        if channel and voice_channel_num_members <= 1:
            await channel.send(f"<@&{JAMON_ROLE_ID}> > **{member.name}** está solo y necesita validación !")

# Run the bot with asyncio to prevent "Event loop is closed" error
def run_bot():
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    try:
        client.run(TOKEN)
    except Exception as e:
        print(f"Error running bot: {e}")

if __name__ == "__main__":
    #webserver.keep_alive()
    run_bot()

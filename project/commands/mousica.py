import discord
from discord.ext import commands
from discord.ui import Button, View
import os
from pathlib import Path

VOICE_CHANNEL_ID = int(os.getenv('VOICE_CHANNEL_ID'))

# Define sounds to play (in real implementation, these could map to sound files or actual playback)
sounds = {
    "Pelea de palos": "pelea-de-palos.mp3",
    "Sicko Mode": "sicko-mode.mp3",
    "🔥": "el-fuego-nos-dicta-la-verdad.mp3",
    "FUEGO": "FUEGO.mp3",
    "exploto": "exploto.mp3",
    "pal lobby": "pal-lobby.mp3",
    "pal lobby yo tambien": "pal-lobby-yo-tambien.mp3",
    "re manco el maxi": "re-manco-el-maxi.mp3",
    "im under the water": "im-under-the-water.mp3"
}

# Create a Button interaction for each sound
class SoundButton(Button):
    def __init__(self, label: str, sound: str):
        super().__init__(label=label, style=discord.ButtonStyle.primary)
        self.sound = sound

    async def callback(self, interaction: discord.Interaction):

        voice_channel = discord.utils.get(interaction.guild.voice_channels, id=VOICE_CHANNEL_ID)
        
        if interaction.user.voice is None:
            await interaction.response.send_message("You are not connected to a voice channel!", ephemeral=True)
            return

        # Si vc es None, es que no está conectado
        vc = interaction.guild.voice_client

        if vc is None:
            # Connect to the specific voice channel if not connected
            vc = await voice_channel.connect()
        else:
            # If connected to another channel, move to the specific one
            if vc.channel != voice_channel:
                await vc.move_to(voice_channel)

        # Stop any currently playing audio
        if vc.is_playing():
            vc.stop()

        current_path = Path("/app")
        audio_path = os.path.join( current_path, "audio", self.sound )
        audio_source = discord.FFmpegPCMAudio(audio_path)
        vc.play(audio_source, after=lambda e: print(f"Finished playing: {self.sound}"))

        await interaction.response.send_message(f"Playing {self.sound}", ephemeral=True)


# Create a View that holds multiple buttons
class SoundBoard(View):
    def __init__(self):
        super().__init__()
        for label, sound in sounds.items():
            self.add_item(SoundButton(label=label, sound=sound))

class Mousica(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='mousica')
    async def mousica(self, ctx):
        await ctx.send("Choose a sound to play:", view=SoundBoard())

# Use async setup function for adding the cog
async def setup(bot):
    await bot.add_cog(Mousica(bot))

from discord.ext import commands

class Ping(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='ping')
    async def ping(self, ctx):
        """Responds with 'Pong!' and latency."""
        latency = round(self.bot.latency * 1000)  # Latency in milliseconds
        await ctx.send(f'Pong! {latency}ms')

# Use async setup function for adding the cog
async def setup(bot):
    await bot.add_cog(Ping(bot))

import discord

from discord.ext import commands
from commands.weather_commands import Client


bot = commands.Bot(command_prefix="$", intents=discord.Intents.default())

@bot.event
async def on_ready():
    await bot.add_cog(Client(bot))
    await bot.tree.sync()
    print("Bot is now ready!")

bot.run('TOKEN')
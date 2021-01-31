import discord
from discord.ext import commands
import logging
import os

from management.greeter import Greeter

logging.basicConfig(level=logging.INFO)

token = os.environ.get('DISCORD_TOKEN')

intents = discord.Intents.default()
intents.members = True

bot = commands.Bot(command_prefix='$',intents=intents)

@bot.event
async def on_ready():
    print('tigerbot online')

bot.add_cog(Greeter(bot))

bot.run(token)

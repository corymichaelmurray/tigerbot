import discord
from discord.ext import commands
import logging
import os

from management.greeter import Greeter
from management.role_manater import RoleManager

logging.basicConfig(level=logging.INFO)

bot_token = os.environ.get('BOT_TOKEN')

intents = discord.Intents.default()
intents.members = True

bot = commands.Bot(command_prefix='$',intents=intents)

@bot.event
async def on_ready():
    print('tigerbot online')

bot.add_cog(Greeter(bot))
bot.add_cog(RoleManager(bot))

bot.run(bot_token)

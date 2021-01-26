import discord
from discord.ext import commands
import logging
import os

logging.basicConfig(level=logging.INFO)

token = os.environ.get('DISCORD_TOKEN')

client = discord.Client()
intents = discord.Intents.default()
intents.members = True

bot = commands.Bot(command_prefix='$',intents=intents)

@bot.command()
async def addrole(ctx, *args):
    await ctx.send('args: {}'.format(', '.join(args)))

@bot.event
async def on_raw_reaction_add(payload):
    print(payload.message_id)

@bot.event
async def on_member_join(member):
    await member.send(
        f'Hi {member.name}, welcome to the Hahnville Gaming Server! Please review the rules and react :thumbsup: to open the channels.'
    )

@bot.event
async def on_ready():
    print('tigerbot online')

bot.run(token)

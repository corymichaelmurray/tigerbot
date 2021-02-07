from discord.ext import commands
from discord.utils import get
import discord
import os

ENTRY_ROLE = os.environ.get('ENTRY_ROLE')

def build_greeting(user):
    return f"""
***Hi {user.name}, welcome to the Hahnville Gaming Server!***

Please review the rules and react :thumbsup: to open the channels.
If you have any questions, feel free to message one of the mods."""

# Greeter Class for Bot Cog
class Greeter(commands.Cog):


    def __init__(self, bot):
        self.bot = bot
        self._last_member = None

    @commands.Cog.listener()
    async def on_member_join(self, member):
        role = get(member.guild.roles, name=ENTRY_ROLE)
        await member.add_roles(role)
        await member.send(build_greeting(member))

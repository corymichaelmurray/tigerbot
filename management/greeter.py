from discord.ext import commands
from discord.utils import get
import discord

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
        role = get(member.guild.roles, name='noboots')
        await member.add_roles(role)
        await member.send(build_greeting(member))
    
    @commands.Cog.listener()
    async def on_raw_reaction_add(self, payload):
        community_terms_msg = 799141863533051926

        if payload.message_id == community_terms_msg:

            if payload.emoji.name == "👍":

                # The role names will hopefully be configurable in the future, but for now
                # they have to stay hard-coded. Below are just my silly Reno 911 references
                # for test roles.
                restricted_role = get(payload.member.guild.roles, name='noboots')
                guild = self.bot.get_guild(payload.guild_id)
                open_role = get(payload.member.guild.roles, name='newbootgoofin')
                member = get(guild.members, id=payload.user_id)

                await member.remove_roles(restricted_role)

                await member.add_roles(open_role)

        else:
            pass
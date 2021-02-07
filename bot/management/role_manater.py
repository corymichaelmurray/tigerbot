from discord.ext import commands
from discord.utils import get
import discord
import os

CG_MSG_ID = os.environ.get('CG_MSG_ID')
ENTRY_ROLE = os.environ.get('ENTRY_ROLE')
BASE_ROLE = os.environ.get('BASE_ROLE')

class RoleManager(commands.Cog):


    def __init__(self, bot):
        self.bot = bot
        self._last_member = None
    
    @commands.Cog.listener()
    async def on_member_join(self, member):
        role = get(member.guild.roles, name=ENTRY_ROLE)
        await member.add_roles(role)
        await member.send(build_greeting(member))
    
    @commands.Cog.listener()
    async def on_raw_reaction_add(self, payload):
        community_guidelines_msg_id = CG_MSG_ID

        if payload.message_id == community_guidelines_msg_id:

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
import discord
from discord.ext import commands
import asyncio

class status(commands.Cog):
    def __init__(self, Bot):
        self.Bot = Bot



    @commands.Cog.listener()
    async def on_ready(self):
        while True:
            await self.Bot.change_presence(activity=discord.Game(name='osu!'))
            await asyncio.sleep(10)
            await self.Bot.change_presence(activity=discord.Game(name='Type osu!help for help!'))
            await asyncio.sleep(10)
            await self.Bot.change_presence(activity=discord.Game(name='Welcome to osu!'))
            await asyncio.sleep(10)
            await self.Bot.change_presence(activity=discord.Game(name='why?!?!??!?!'))
            await asyncio.sleep(10)
            await self.Bot.change_presence(activity=discord.Game(name='Разрабы - insert worst nightmare#9035'))
            await asyncio.sleep(10)
            await self.Bot.change_presence(activity=discord.Game(name=(f'{len(self.Bot.guilds)} Серверов и {len(self.Bot.users)} Людей!')))
            await asyncio.sleep(10)
            await self.Bot.change_presence(activity=discord.Game(name='Hello world!'))
            await asyncio.sleep(10)



def setup(Bot):
    Bot.add_cog(status(Bot))
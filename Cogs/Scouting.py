import discord
from discord.ext import commands


class Scout(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print('Scout load. Not have functions!')


def setup(client):
    client.add_cog(Scout(client))
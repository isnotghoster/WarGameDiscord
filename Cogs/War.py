import discord
from SQLRequests import sqlreq
from discord.ext import commands


class WarGame(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def attack(self, ctx: commands.Context, member: discord.Member = None):
        if member is not None and member is not ctx.message.author and sqlreq.user(member.id):
            await ctx.send('True')


    # @commands.command()
    # async def test(self, ctx: commands.Context, member: discord.Member):
    #     await ctx.send(sqlreq.user(member_id=member.id))


def setup(client):
    client.add_cog(WarGame(client))
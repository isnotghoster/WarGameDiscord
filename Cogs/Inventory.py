import discord
from SQLRequests import sqlreq
from discord.ext import commands


class Inventory(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print('Inventory load.')

    @commands.command()
    async def inv(self, ctx: commands.Context):

        embed = discord.Embed(title='Ваш инвентарь:', color=discord.Color.dark_gold())

        for unit in sqlreq.unit_list(ctx.message.author):
            embed.add_field(name=unit[0],value=f'Количество юнитов: {unit[1]} \nУмение: {unit[2]} \nЭпоха: {unit[3]}')
        embed.set_footer(text="Atomic-Kartonen Union")

        await ctx.send(embed=embed)


def setup(client):
    client.add_cog(Inventory(client))
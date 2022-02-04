import discord
from Buttons import ShopNationUI
from SQLRequests import sqlreq
from discord.ext import commands


class Shop(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print('Shop load.')

    @commands.command()
    async def shop(self, ctx: commands.Context):
        embed_view = ShopNationUI(ctx)

        embed = discord.Embed(title="Магазин юнитов", description="Выберите нацию,чьих юнитов хотите купить.",
                              color=0xff0000)
        embed.add_field(name="USA", value="ПМВ - Современность", inline=True)
        embed.add_field(name="USSR", value="ПМВ - Современность", inline=True)
        embed.add_field(name="Germany", value="ПМВ - Современность", inline=True)
        embed.add_field(name="France", value="ПМВ - Современность", inline=True)
        embed.add_field(name="Britain", value="ПМВ - Современность", inline=True)
        embed.add_field(name="Italy", value="ПМВ - Современность", inline=True)
        embed.add_field(name="Sweden", value="ПМВ - Современность", inline=True)
        embed.set_footer(text="Atomic-Kartonen Union")

        shop_message = await ctx.send(embed=embed, view=embed_view)

        embed_view.nation_shop = shop_message

    @commands.command()
    async def buy(self, ctx: commands.Context, unit_id: int = None):
        if sqlreq.unit_list(unit_id=unit_id) is not None:
            pass
        else:
            await ctx.send(embed=discord.Embed(title='Err'))

    @commands.command()
    async def check(self, ctx: commands.Context, id: int = None):
        print(sqlreq.unit_list(unit_id=id))


def setup(client):
    client.add_cog(Shop(client))
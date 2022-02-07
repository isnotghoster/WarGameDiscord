import discord
from Buttons import ShopNationUI
from SQLRequests import sqlreq
from SQLRequests import NotEnoughMoney
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
            try:
                unit = sqlreq.hiring(unit_id=unit_id, user=ctx.message.author)
                await ctx.send(embed=discord.Embed(title=f'New unit \"{unit}\" hired'))

            except NotEnoughMoney as exc:
                await ctx.send(embed=discord.Embed(title=exc))

        else:
            await ctx.send(embed=discord.Embed(title='Err'))

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def award(self, ctx: commands.Context, member: discord.Member = None, amount: int = None):
        pass

    @commands.command(aliases=['bank', "credits"])
    async def credit(self, ctx: commands.Context):
        await ctx.reply(embed=discord.Embed(
            title="СпёрБанк",
            colour=0xffa500,
            description=f"""Ваш баланс состовляет: {sqlreq.balance(ctx.message.author.id)}"""))


def setup(client):
    client.add_cog(Shop(client))
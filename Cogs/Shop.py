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
        # Example: embed.add_field(name="Imperium", value="41 тысячелетие", inline=True)
        embed.add_field(name="USA", value="ПМВ - Современность", inline=True)
        embed.add_field(name="USSR", value="ПМВ - Современность", inline=True)
        embed.add_field(name="Germany", value="ПМВ - Современность", inline=True)
        embed.add_field(name="France", value="ПМВ - Современность", inline=True)
        embed.add_field(name="Britain", value="ПМВ - Современность", inline=True)
        embed.add_field(name="Italy", value="ПМВ - Современность", inline=True)
        embed.add_field(name="Sweden", value="ПМВ - Современность", inline=True)
        embed.add_field(name="Special", value="Без времени", inline=True)
        embed.add_field(name="Savages", value="До н.э.", inline=True)
        embed.set_footer(text="Atomic-Kartonen Union")

        shop_message = await ctx.send(embed=embed, view=embed_view)

        embed_view.nation_shop = shop_message

    @commands.command()
    async def buy(self, ctx: commands.Context, unit_id: int = None, count: int = 1):
        if sqlreq.unit_list(unit_id=unit_id) is not None:
            try:
                unit = sqlreq.hiring(unit_id=unit_id, user=ctx.message.author, count=count)
                await ctx.send(embed=discord.Embed(title=f"A new unit \"{unit}\" was hired, in the amount: {count}.\
                \nYou have units: {sqlreq.unit_amount(user_id=ctx.message.author.id, unit=unit_id)}"))

            except NotEnoughMoney as exc:
                await ctx.send(embed=discord.Embed(title=exc))

        else:
            await ctx.send(embed=discord.Embed(title='Err'))

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def award(self, ctx: commands.Context, member: discord.Member = None, amount: int = None):
        sqlreq.awarding(user_id=member.id, amount=amount)
        await ctx.reply(embed=discord.Embed(title=f'Награжден: {member.name}',
                                            colour=discord.Colour.teal(),
                                            description=f"Награждается {member.name},на сумму: {amount} :credit_card:!"))

    @commands.command(aliases=['bank', "credits"])
    async def credit(self, ctx: commands.Context):
        await ctx.reply(embed=discord.Embed(
            title="СпёрБанк",
            colour=0xffa500,
            description=f"""Ваш баланс состовляет: {sqlreq.balance(ctx.message.author.id)}"""))


def setup(client):
    client.add_cog(Shop(client))
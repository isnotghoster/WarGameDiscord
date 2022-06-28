import discord.ui
import discord
from SQLRequests.SQLR import sqlreq


class ShopNationUI(discord.ui.View):
    def __init__(self, ctx):
        super().__init__()
        self.ctx = ctx
        self.nation_shop = None

    async def units_table(self, button_label):
        embed_view = ShopPaginationUI(self.ctx,
                                      nation_tuple=sqlreq.unit_list(nation=button_label.lower()),
                                      nation_name=button_label.lower())
        embed = embed_view.get_page_embed(button_label)
        embed_view.edit_message = await self.nation_shop.edit(embed=embed, view=embed_view)

    # Example:
    # @discord.ui.button(label='Imperium', style=discord.ButtonStyle.blurple)
    # async def imperium(self, button: discord.ui.Button, interaction: discord.Interaction):
    #     if interaction.user == self.ctx.author: await self.units_table(button_label=button.label)

    @discord.ui.button(label="USA", style=discord.ButtonStyle.blurple)
    async def usa(self, button: discord.ui.Button, interaction: discord.Interaction):
        if interaction.user == self.ctx.author: await self.units_table(button_label=button.label)

    @discord.ui.button(label='USSR', style=discord.ButtonStyle.blurple)
    async def ussr(self, button: discord.ui.Button, interaction: discord.Interaction):
        if interaction.user == self.ctx.author: await self.units_table(button_label=button.label)

    @discord.ui.button(label='Germany', style=discord.ButtonStyle.blurple)
    async def germany(self, button: discord.ui.Button, interaction: discord.Interaction):
        if interaction.user == self.ctx.author: await self.units_table(button_label=button.label)

    @discord.ui.button(label='France', style=discord.ButtonStyle.blurple)
    async def france(self, button: discord.ui.Button, interaction: discord.Interaction):
        if interaction.user == self.ctx.author: await self.units_table(button_label=button.label)

    @discord.ui.button(label='Britain', style=discord.ButtonStyle.blurple)
    async def britain(self, button: discord.ui.Button, interaction: discord.Interaction):
        if interaction.user == self.ctx.author: await self.units_table(button_label=button.label)

    @discord.ui.button(label='Italy', style=discord.ButtonStyle.blurple)
    async def italy(self, button: discord.ui.Button, interaction: discord.Interaction):
        if interaction.user == self.ctx.author: await self.units_table(button_label=button.label)

    @discord.ui.button(label='Sweden', style=discord.ButtonStyle.blurple)
    async def swedan(self, button: discord.ui.Button, interaction: discord.Interaction):
        if interaction.user == self.ctx.author: await self.units_table(button_label=button.label)

    @discord.ui.button(label='Special', style=discord.ButtonStyle.blurple)
    async def special(self, button: discord.ui.Button, interaction: discord.Interaction):
        if interaction.user == self.ctx.author: await self.units_table(button_label=button.label)

    @discord.ui.button(label='Savages', style=discord.ButtonStyle.blurple)
    async def savages(self, button: discord.ui.Button, interaction: discord.Interaction):
        if interaction.user == self.ctx.author: await self.units_table(button_label=button.label)


class ShopPaginationUI(discord.ui.View):
    def __init__(self, ctx, nation_tuple, nation_name):
        super().__init__()
        self.ctx = ctx
        self.nation = nation_tuple
        self.page = 0
        self.page_length = 10
        self.edit_message = None
        self.nation_name = nation_name

    def get_page_embed(self, nation):
        embed = discord.Embed(title=f'Units of {nation}.',
                              description=f'Страница: {self.page + 1}/{self.get_max_page()}',
                              color=discord.Color.teal())

        iterator = self.page_length * self.page

        while iterator < self.page_length * self.page + self.page_length and iterator < len(self.nation):
            embed.add_field(name=self.nation[iterator][1], value=f'id:{self.nation[iterator][0]}', inline=False)

            iterator += 1

        embed.set_footer(text='Atomic-Kartonen Union')

        return embed

    def get_max_page(self):
        return math.ceil(len(self.nation) / self.page_length)

    def set_page(self, page):
        if 0 <= page < self.get_max_page():
            self.page = page

    @discord.ui.button(label='Cлед. стр.', style=discord.ButtonStyle.red)
    async def next_page(self, button: discord.ui.Button, interaction: discord.Interaction):
        if interaction.user == self.ctx.author:
            self.set_page(self.page + 1)
            await self.edit_message.edit(embed=self.get_page_embed(self.nation_name))

    @discord.ui.button(label='Пред. стр.', style=discord.ButtonStyle.red)
    async def previous_page(self, button: discord.ui.Button, interaction: discord.Interaction):
        if interaction.user == self.ctx.author:
            self.set_page(self.page - 1)
            await self.edit_message.edit(embed=self.get_page_embed(self.nation_name))

    @discord.ui.button(label="Обратно.", style=discord.ButtonStyle.danger)
    async def back(self, button: discord.ui.Button, interaction: discord.Interaction):
        if interaction.user == self.ctx.author:
            embed_view = ShopNationUI(self.ctx)

            embed = discord.Embed(title="Магазин юнитов", description="Выберите нацию,чьих юнитов хотите купить.",
                                  color=0xff0000)
            embed.add_field(name="USA", value="ПМВ - Современность", inline=True)
            embed.add_field(name="USSR", value="ПМВ - Современность", inline=True)
            embed.add_field(name="Germany", value="ПМВ - Современность", inline=True)
            embed.add_field(name="France", value="ПМВ - Современность", inline=True)
            embed.add_field(name="Britain", value="ПМВ - Современность", inline=True)
            embed.add_field(name="Italy", value="ПМВ - Современность", inline=True)
            embed.add_field(name="Sweden", value="ПМВ - Современность", inline=True)
            embed.add_field(name='Special', value="Без времени", inline=True)
            embed.set_footer(text="Atomic-Kartonen Union")

            await self.edit_message.edit(embed=embed, view=embed_view)

            embed_view.nation_shop = self.edit_message

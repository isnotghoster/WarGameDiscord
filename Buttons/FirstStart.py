import discord.ui
import discord
from SQLRequests import sqlreq


class FirstStartUI(discord.ui.View):
    def __init__(self, ctx, ):
        super().__init__()
        self.ctx = ctx

    @discord.ui.button(label="Продолжить", style=discord.ButtonStyle.green)
    async def confirm(self, button: discord.ui.Button, interaction: discord.Interaction):
        embed = discord.Embed(title='Аккаунт', description='Ваш аккаунт был добавлен.')
        embed.add_field(name="Войска", value="Вам был выдан стартовый набор", inline=False)
        embed.add_field(name='Саперов ПВМ 0 ранга', value="160", inline=True)
        embed.add_field(name='Кавалеристов ПВМ 0 ранга', value="40", inline=True)
        embed.set_footer(text='Atomic-Kartonen Union')
        if interaction.user == self.ctx.author:
            if sqlreq.new_player(self.ctx.author):
                await interaction.response.send_message(ephemeral=True, embed=embed)
                self.stop()
            else:
                await interaction.response.send_message('Вас уже зарегистрированы.', ephemeral=True)
                self.stop()
        else:
            pass

    @discord.ui.button(label='Отмена', style=discord.ButtonStyle.blurple)
    async def cancel(self, button: discord.ui.Button, interaction: discord.Interaction):
        if interaction.user == self.ctx.author:
            await interaction.response.send_message('Принято', ephemeral=True)
            self.stop()
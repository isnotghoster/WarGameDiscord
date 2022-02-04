import discord
from Buttons import FirstStartUI
from discord.ext import commands


class StartGame(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print('StartGame load.')

    @commands.command()
    async def enter(self, ctx: commands.Context):
        embed_view = FirstStartUI(ctx)

        embed = discord.Embed(title="Storm War Games", description="Amator 2.0 server", color=0x4900d1)
        embed.add_field(name="Описание", value="Подозрительные шашечки", inline=True)
        embed.add_field(name="Предупреждение",
                        value="После создания записи в игре,на вас могу нападать другие игроки без вашей ведомости",
                        inline=False)
        embed.set_footer(text="Atomic-Kartonen Union")

        await ctx.send(embed=embed, view=embed_view, file=discord.File("I_found_Karton.png"))

        await embed_view.wait()

    @commands.command()
    async def help(self, ctx: commands.Context):
        # Выводит подсказку по игре
        # Стр. 1 = Краткая подсказка по игре
        # Стр. 2-10 = Подсказка по типам юнитов
        #
        await ctx.send('Er404. Мы где-то проебали это')


def setup(client):
    client.add_cog(StartGame(client))
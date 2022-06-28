import os
from discord.ext import commands
from settings import TOKEN


class Client(commands.Bot):
    def __init__(self):
        super().__init__(command_prefix=commands.when_mentioned_or(">>"), intents=discord.Intents.all())

    async def on_ready(self):
        print(f"Logged in as {self.user} (ID: {self.user.id})")
        print("------")


client = Client()
client.remove_command('help')

for filename in os.listdir("./Cogs"):
    if filename.endswith('.py'):
        client.load_extension(f"Cogs.{filename[:-3]}")

client.run(TOKEN)
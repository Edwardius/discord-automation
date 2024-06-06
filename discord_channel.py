import discord
from discord.ext import commands

# Replace with your bot's token
TOKEN = 

intents = discord.Intents.default()
intents.guilds = True
intents.members = True

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'Bot connected as {bot.user}')
    await sync_channel_permissions()

async def sync_channel_permissions():
    for guild in bot.guilds:
        for category in guild.categories:
            overwrites = category.overwrites
            for channel in category.channels:
                await channel.edit(overwrites=overwrites)
                print(f'Synced permissions for channel: {channel.name} with category: {category.name}')

bot.run(TOKEN)

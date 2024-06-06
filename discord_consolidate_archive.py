import discord
from discord.ext import commands

# Replace with your bot's token
TOKEN = 
# Name of the consolidated archive category
ARCHIVE_CATEGORY_NAME = ''

intents = discord.Intents.default()
intents.guilds = True
intents.members = True

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'Bot connected as {bot.user}')
    await consolidate_archive_categories()

async def consolidate_archive_categories():
    for guild in bot.guilds:
        archive_category = None

        # Find or create the main archive category
        for category in guild.categories:
            if category.name.lower() == ARCHIVE_CATEGORY_NAME.lower():
                archive_category = category
                break

        if not archive_category:
            archive_category = await guild.create_category(ARCHIVE_CATEGORY_NAME)
            print(f'Created archive category: {archive_category.name}')

        # Move channels from other archive categories to the main archive category
        for category in guild.categories:
            if category.name.lower().endswith('archive') and category != archive_category:
                for channel in category.channels:
                    await channel.edit(category=archive_category)
                    print(f'Moved channel: {channel.name} to category: {archive_category.name}')
                await category.delete()
                print(f'Deleted empty archive category: {category.name}')

bot.run(TOKEN)

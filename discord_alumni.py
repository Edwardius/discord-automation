import discord
from discord.ext import commands
from datetime import datetime, timezone

# Replace with your bot's token
TOKEN = ''
# Replace with your server's ID
GUILD_ID = 
# Replace with your Alumni role's ID
ALUMNI_ROLE_ID =
# Set the cutoff date for Alumni status
CUTOFF_DATE = datetime(2022, 7, 30, tzinfo=timezone.utc)  # Example date

intents = discord.Intents.default()
intents.members = True  # Enable the members intent

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'Bot connected as {bot.user}')
    guild = bot.get_guild(GUILD_ID)
    if guild:
        alumni_role = guild.get_role(ALUMNI_ROLE_ID)
        if alumni_role:
            for member in guild.members:
                if member.joined_at and member.joined_at.replace(tzinfo=timezone.utc) < CUTOFF_DATE:
                    if alumni_role not in member.roles:
                        await member.add_roles(alumni_role)
                        print(f'Assigned Alumni role to {member.name}')

    print('Finished assigning roles')

bot.run(TOKEN)

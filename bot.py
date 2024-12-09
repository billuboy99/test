import discord
from discord.ext import commands
from discord import app_commands

intents = discord.Intents.all()
intents.messages = True
intents.dm_messages = True

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}')
    await bot.change_presence(activity=discord.Streaming(name="Pure GFX!!!", url="http://twitch.tv/streamer"))
    try:
        synced = await bot.tree.sync()
        print(f"Synced {len(synced)} command(s)")
    except Exception as e:
        print(f"Failed to sync commands: {e}")

@bot.tree.command(name="dm")
async def dm(interaction: discord.Interaction, user: discord.User, message: str):
    try:
        await user.send(message)
        await interaction.response.send_message(f"Message sent to {user.name}", ephemeral=True)

    except discord.Forbidden:
        await interaction.response.send_message("I cannot send a DM to this user.", ephemeral=True)

bot.run('')

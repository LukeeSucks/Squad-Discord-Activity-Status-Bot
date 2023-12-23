import discord
from discord.ext import commands, tasks
import APIScript
import itertools

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='>', intents=intents)
bot.remove_command('help')

# Global cycle variable, initialized with dummy values
status_cycle = itertools.cycle(["", ""])

@bot.event
async def on_ready():
    print("Bot is online!")
    APIScript.update_server_info()
    global status_cycle
    latest_map = APIScript.get_latest_map()
    latest_player_count = APIScript.get_latest_player_count()
    status_cycle = itertools.cycle([latest_map, latest_player_count])
    change_status.start()

@tasks.loop(seconds=30) # If changing made more frequent, could lead to being rate limited
async def change_status():
    global status_cycle

    # Update server information
    APIScript.update_server_info()

    # Check the server status
    latest_status = APIScript.get_latest_status()
    if latest_status == "offline":
        # If the server is offline, set the bots status to idle
        await bot.change_presence(activity=discord.Game(name="Server Offline :("), status=discord.Status.idle)
    else:
        status = next(status_cycle)
        await bot.change_presence(activity=discord.Game(name=status), status=discord.Status.online)

bot.run('bot_token')
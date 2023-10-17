import asyncio
import os
import discord
from discord.ext import commands
import traceback, sys

client = commands.Bot(command_prefix="a!", intents=discord.Intents().all(), case_insensitive=True)
client.remove_command("help")
   
async def setup(extensions: list[str], client: discord.Client) -> None:
    async with client:
        for extension in extensions:
            try:
                await client.load_extension(extension)
            except Exception as e:
                print(f'Failed to load extension {extension}.', file=sys.stderr)
                traceback.print_exc()
        await client.start(os.getenv("API_TOKEN"), reconnect=True)

if __name__ == '__main__':
    try:
        asyncio.run(setup(extensions=['cogs.listeners'], client=client))
    except Exception as e:
        print(f"Error when logging in: {e}")
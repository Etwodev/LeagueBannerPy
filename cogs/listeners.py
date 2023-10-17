import discord, asyncio, ast
from discord import message
from discord.ext import commands, tasks

class listeners(commands.Cog):
    def __init__(self, client):
        self.client = client
        

    @tasks.loop(minutes=5)
    async def status_task(self):
        await self.client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=f"users | {len(self.client.guilds)} servers"))
            

    @commands.Cog.listener()
    async def on_ready(self):
        if not self.status_task.is_running():
            self.status_task.start()
            
    @commands.Cog.listener()
    async def on_message(self, ctx):
        for activity in ctx.author.activities:
            if type(activity) == discord.activity.Game:
                if activity.name == "League of Legends":
                    ctx.author.ban("You Play League...")
                    ctx.send(f"{ctx.author.name} has been banned for playing League!")
            
async def setup(client):
    await client.add_cog(listeners(client))
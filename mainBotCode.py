from typing import Final
from discord import Intents,Client,Message
from discord.ext import tasks, commands
from dotenv import load_dotenv
import asyncio
import os
import requests
import math
import discord
from questionInfo import *

load_dotenv()
TOKEN: Final[str] = os.getenv('TOKEN')

intents: Intents = Intents.default()
intents.message_content = True
client: Client = Client(intents=intents)


def difficultychecker(difficulty):
    if difficulty == "Hard":
        return 0xff0000  
    elif difficulty == "Medium":
        return 0xFFFF00
    elif difficulty == "Easy":
        return 0x008000
    
async def returnInfo(channel):
    daily_problem = fetch_daily_leetcode_problem()

    embed = discord.Embed(
            title="Today's LeetCode Problem",
            description="",
            color= difficultychecker(daily_problem['difficulty']))
    
    if daily_problem:
        embed.add_field(name="Problem", value=f"`{daily_problem['title']}`", inline=False)
        embed.add_field(name="Difficulty", value=f"`{daily_problem['difficulty']}`", inline=False)
        embed.add_field(name="Link", value=f"[Click here to solve the problem]({daily_problem['link']})", inline=False)
        embed.add_field(name="Description", value=f"```python\n{daily_problem['description']}\n```", inline=False)
    else:
        embed.description = "Big yikers! An error has occurred."

    await channel.send(embed=embed)

@tasks.loop(minutes=1)
async def api_request_task():
    channel = client.get_channel(1273205099589533741)  # This needs to be put to 0 when we fully upload to github. Dont want random things sent in our channel by other people.
    if channel is not None:
        await returnInfo(channel)  
        print("Daily problem message sent to channel!")
    else:
        print("Channel not found!")

@client.event
async def on_ready():
    print(f'{client.user} is now running!')
    api_request_task.start()

async def main():
    await client.start(TOKEN)

asyncio.run(main())
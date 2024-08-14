from typing import Final
from discord import Intents,Client,Message
from discord.ext import tasks, commands
from dotenv import load_dotenv
import asyncio
import os
import requests
import math
import discord

load_dotenv()
TOKEN: Final[str] = os.getenv('TOKEN')

intents: Intents = Intents.default()
intents.message_content = True
client: Client = Client(intents=intents)
        
async def send_message(message : Message, user_message:str) -> None:
    if not user_message:
        print("Message was empty because intents were not enable properly.")
    
    if is_private := user_message[0] == '?':
        user_message = user_message[1:]
        
    try:
        response: str = get_response(user_message)
        await message.author.send(response) if is_private else await message.channel.send(response)
    except Exception as e:
        print(e)

''' Going to use this for choosing the different languages:

def get_response(user_input: str) -> str:
    if user_input.strip().lower() == "#kills":
        leaderboard = create_leaderboard(puuidPairs, "Kills")
        return display_leaderboard(leaderboard, "Kills")
    elif user_input.strip().lower() == "#assists":
        leaderboard = create_leaderboard(puuidPairs, "Assists")
        return display_leaderboard(leaderboard, "Assists")
    elif user_input.strip().lower() == "#deaths":
        leaderboard = create_leaderboard(puuidPairs,"Deaths")
        return display_leaderboard(leaderboard, "Deaths")
    elif user_input.strip().lower().startswith("#mastery"):
        output = ""
        parts = user_input.strip().split()
        if len(parts) >= 3 and parts[0].lower() == "#mastery":
            player_name = " ".join(parts[1:-1])
            count = int(parts[-1])
            for name, info in puuidPairs.items():
                if info[0] == player_name:
                    name = info[0]
                    puuid = info[2]
                    output = print_top_masteries(name, puuid, count)
                    break

            else:
                print("Invalid command format. Please use '#mastery PlayerName Count'.")
        return output
'''  
'''  
@client.event
async def on_message(message: Message) -> None:
    if message.author == client.user:
        return

    username: str = str(message.author)
    user_message: str = message.content
    channel: str = str(message.channel)

    if user_message.startswith("#kills"):
        response = get_response(user_message)
        await message.channel.send(response)
    if user_message.startswith("#assists"):
        response = get_response(user_message)
        await message.channel.send(response)
    if user_message.startswith("#deaths"):
        response = get_response(user_message)
        await message.channel.send(response)
    if user_message.startswith("#mastery"):
        response = get_response(user_message)
        await message.channel.send(response)
        
    else:
        # Handle other messages if needed
        pass
    
    print(f'[{channel}] {username}: "{user_message}"')
    
#----------------------------------------------------------------------------
'''  

@tasks.loop(minutes=1)
async def api_request_task(message: Message) -> None:
    channel = client.get_channel(1273205099589533741) # Put your dicord channel number here inside the ()!!
    response = get_response(user_message)
    await message.channel.send(response)
    #await APIrequest()  

        
@client.event
async def on_ready():
    print(f'{client.user} is now running!')
    api_request_task.start()

async def main():
    await client.start(TOKEN)
    
asyncio.run(main())
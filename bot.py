"""
___DISCORD BOT FOR THE LG1 SERVER:___
    - This bot is designed to be used on the LG1 Discord server.
    - It can be used and modified for other servers, but it is not guaranteed to work.
    - 

"""
import os
import discord as dc
import asyncio
#imported a self written .py module which works as the Enviroment variable storage for the bot.
#This is to avoid leaking my bot token to the public.
#If you want to recreate this, you can do so by creating your own module and defining Funktions that return your secrets.
import envkeys as key

#create a new client object.
client = dc.Client()

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')
client.run(key.TOKEN())
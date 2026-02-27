import discord
import random
from deneme1 import gen_pass2

from deneme import gen_pass
intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'{client.user} olarak giriş yaptık.')
Messagett = True
@client.event
async def on_message(message):

    
    
    
    
    if message.content.startswith("help about server"):
        message.channel.send("you can use help to help about some code ex:help print")
        message.channel.send("sss makes you a password")
        
    if message.content.startswith('help1'):
        gr = str(message.content[5:])
        await message.channel.send(gen_pass2(gr))
    if message.content.startswith('sss'):
        
        xer = int(message.content[3:])
        await message.channel.send("password is going to make")# Extract the number after '1'
        try:
            gen_pass(xer)
        except:
            message.channel.send("please enter a number")
    
        await message.channel.send(gen_pass(xer))
    if message.author == client.user:
        return
    if message.content.startswith('merhaba'):
        await message.channel.send("Merhaba!")
    
    elif message.content.startswith('sybau'):
        await message.channel.send("😭🥀")
    


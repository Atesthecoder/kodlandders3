import discord
import random
import builtins

def gen_pass2(p):
    x = getattr(builtins,p)
    gt = str(help(x))
    return gt.__doc__#yapay zeka ile sadece
    
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
        await message.channel.send("şifre oluştrulacak!sayı girdiniz değilmi???")# Extract the number after '1'
        try:
            gen_pass(xer)
        except:
            message.channel.send("Lütfen bir sayı girin!")
    
        await message.channel.send(gen_pass(xer))
    if message.author == client.user:
        return
    if message.content.startswith('merhaba'):
        await message.channel.send("Merhaba!")
    
    elif message.content.startswith('sybau'):
        await message.channel.send("😭🥀")
    

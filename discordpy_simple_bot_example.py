import discord
from discord.ext import commands 
import asyncio

description = 'oui'
intents= discord.Intents().all()
bot = commands.Bot(command_prefix="", description=description, intents=intents)

#écrit dans la console "carre" quand le bot est fonctionnel/ print "carre" in the cmd prompt when the bot is working
@bot.event
async def on_ready():
    print("carre")
    await bot.change_presence(activity=discord.Game(name='vec ta daronne'))#put the name of the game in name=""

#déplace l'utilisateur mentionné toute les 1.5sec pour un total de 11 fois/ move the pinged user every 1.5sec for a total of 11 times  
@bot.command()
async def ms(ctx, member: discord.Member):
    ChannelA= bot.get_channel()#insert the id of the voice channel  within the parenthesis
    ChannelB= bot.get_channel()
    if ctx.message.author.guild_permissions.move_members==True:
        for i in range(5):
            await member.move_to(ChannelA, reason='ferme ta gueule')
            await asyncio.sleep(1.5) #wait 1.5sec before executing the next line
            await member.move_to(ChannelB, reason='ferme ta gueule')
            await asyncio.sleep(1.5)
        await member.move_to(ctx.author.voice.channel,reason='ferme ta gueule')

#déplace l'utilisateur mentionné toute les 1.5sec pour un total de 101 fois/ move the pinged user every 1.5sec for a total of 101 times   
@bot.command()
async def mss(ctx, member: discord.Member):
    ChannelA= bot.get_channel()#insert the id of the voice channel  within the parenthesis
    ChannelB= bot.get_channel()
    if ctx.message.author.guild_permissions.move_members==True:
        for i in range(50):
            await member.move_to(ChannelA, reason='ferme ta gueule')
            await asyncio.sleep(1.5)#wait 1.5sec before executing the next line
            await member.move_to(ChannelB, reason='ferme ta gueule')
            await asyncio.sleep(1.5)
        await member.move_to(ctx.author.voice.channel,reason='ferme ta gueule')

#déconnecte l'utilisateur mentionné 1 fois par 1.5seconde 100 fois/ disconnect the mentionned user once every 1.5second 100 times 
@bot.command()
async def ds(ctx, member: discord.Member):
    if ctx.message.author.guild_permissions.move_members==True:
        for i in range(100):
            await member.move_to(None, reason='ferme ta gueule') #disconnect the user when the channel setting is passed as None
            await asyncio.sleep(1.5)#wait 1.5sec before executing the next line
 

#metionne 25 fois l'utilisateur mentionné / ping 25 times the mentionned user
@bot.command()
async def ps(ctx, member:discord.Member):
    if ctx.message.author.guild_permissions.administrator==True:
        for i in range(25):
            await ctx.send(member.mention)
            await asyncio.sleep(.5)#wait 0.5sec before executing the next line

#envoi un message privé aux utilisateurs joignant le serveur/send a direct message to poeple who join the guild
@bot.event
async def on_member_join(member):
    await member.send(f'va bien te faire foutre {member.name} !')

#concatène deux chaines de caractères(str)(1+5=15) changer à "int" pour faire additonner les nombres/ concatenates the two string(str)(1+1=15) change to "int" in order to do the sum of the two numbers
@bot.command()
async def somme(ctx, numUn: str, numDeux: str):
    await ctx.send(numUn + numDeux)

#répond"chong" quand l'utilisateur commence son message par ching/ reply "chong" when the sentence of the user starts with "ching"
@bot.command()
async def ching(ctx):
    await ctx.reply('chong')

bot.run('token')


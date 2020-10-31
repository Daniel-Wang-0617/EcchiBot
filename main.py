import os
import requests
import random
import discord
import asyncio
from discord.ext import commands

bot = commands.Bot(command_prefix="e.")

client = discord.Client()

TOKEN = ""

@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected to Discord!')
 
@bot.event
async def on_member_join(member):
    await member.create_dm()
    await member.dm_channel.send(
        f'Hi {member.name}, welcome to the WHS Anime Server!'
    )

@bot.event
async def on_command_error(ctx, error):
  if isinstance(error, commands.MissingRequiredArgument):
    await ctx.send("Please input the required argument")
  elif isinstance(error, commands.CommandNotFound):
    await ctx.send("Command not found")
  elif isinstance(error, commands.CommandOnCooldown):
    await ctx.send("Please wait for cooldown to end")
  else:
    pass

@bot.event
async def on_member_remove(member):
  print(f'(member) has left server :cri:')


@bot.command(name="pic", help="gives a nice ecchi pic")
async def random_anime_quote(ctx):
    links = [
    "https://external-preview.redd.it/JFE4Jek_WZNlBLyJtvw_moBgMfU6jjCeXBkTcBtzOwU.jpg?width=640&crop=smart&auto=webp&s=ca8cff352d7ef60ecd68e19679e7d488b7099509",
    "https://preview.redd.it/g6894skzkom41.png?width=640&crop=smart&auto=webp&s=e36ddbe2fe2e2fe9a972cd0069e8ce3a463dcb5c",
    "https://preview.redd.it/unylvn8av6841.jpg?width=640&crop=smart&auto=webp&s=8a5491b7373715e3df9b118855269a92a659ab88",
    "https://preview.redd.it/fhqp4rfqsqk51.jpg?width=640&crop=smart&auto=webp&s=93d10f754a091d1bda7c86846d76af4558ae29ca",
    "https://media.discordapp.net/attachments/753771988035829771/772168084726611988/image0.jpg?width=260&height=382",
    ]
    response = random.choice(links)
    await ctx.send(response)

@bot.command(name="sauce", help="gives sauce :smirk:")
async def random_anime_quote(ctx):
    sauce = (("https://imgur.com/a/x4qYloJ#keyug9l", 279963),("https://imgur.com/a/XIYB71N", 286444))
    response = random.choice(sauce)
    await ctx.send(response[0])
    await ctx.send("Sauce: " + str(response[1]))



bot.run(TOKEN)

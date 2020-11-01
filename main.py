import os
import requests
import random
import discord
import asyncio
from discord.ext import commands

bot = commands.Bot(command_prefix="e.")

TOKEN = "NzcxOTM3OTI0NjkwMjE0OTIz.X5zZNw.wszYqlaNpLV057poJWM-MxsAUmk"

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

@bot.event
async def on_message(message):
    await bot.process_commands(message)
    if message.author == bot.user:
        return
    if "im" in message.content:
        responseIndex = message.content.find("im")
        await message.channel.send("Hi " + message.content[responseIndex:] + ", I'm Jack")

@bot.command(name="pic", help="gives a nice ecchi pic")
async def pic(ctx):
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
async def sauce(ctx):
    sauce = [
    ("https://imgur.com/a/x4qYloJ#keyug9l", 279963),
    ("https://imgur.com/a/XIYB71N", 286444),
    ]
    response = random.choice(sauce)
    await ctx.send(response[0])
    await ctx.send("Sauce: " + str(response[1]))

@bot.command(name="hentai", help="gives sauce in a video format")
async def sauce(ctx):
    hentai = [
    ("https://hanime.tv/videos/hentai/aku-no-onna-kanbu-full-moon-night-r-1", "Aku no Onna Kanbu: Full Moon Night R 1"),
    ("https://hanime.tv/videos/hentai/isekai-harem-monogatari-2", "Isekai Harem Monogatari 2")
    ]
    response = random.choice(hentai)
    await ctx.send(response[0])
    await ctx.send("Sauce: " + response[1])





bot.run(TOKEN)

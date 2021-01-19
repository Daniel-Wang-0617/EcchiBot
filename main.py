import os
import requests
import random
import discord
import asyncio
import time
import praw
from discord.ext import commands
from reactions import *
from nhentai import *

bot = commands.Bot(command_prefix="e.")

TOKEN = "NzcxOTM3OTI0NjkwMjE0OTIz.X5zZNw.kj0G8Zjz8L11CqV-yaJ7H0TbZyg"

reddit = praw.Reddit(client_id = 'C0EVE0NpVGV8PQ', client_secret = 'pMwTwwG96WWCwSvt5Qjajmd3BI4s7A', username = 'EcchiBot', password = 'ecchibot', user_agent = 'EcchiBot')

subreddit_ecchi = reddit.subreddit('ecchi')
subreddit_thighdeology = reddit.subreddit('thighdeology')
subreddit_so = reddit.subreddit('SaraOrrego')
subreddit_tits = reddit.subreddit('BigAnimeTiddies')



@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.playing, name="with my dxe"))
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
  print(f'{member} has left server :cri:')


@bot.event
async def on_message(message):
    await bot.process_commands(message)
    content = message.content
    if(message.author == bot.user):
        return
    if(message.author in mutedList):
        await message.delete()
    if("dick" in content.lower()):
        await react_eggplant(message)
        await message.channel.send("Suck my dick m")
        return
    
piclinks =[]
hotlinks = []
hotthighlinks = []
topthighlinks = []
solinks = []
titlinks = []

mutedList = []

for item in reddit.user.me().saved(limit=None):
    piclinks.append(item)


@bot.command(name="sauceme", help="Get random sauce")
async def sauceme(ctx):
    await random_sauce(ctx)

@bot.command(name="mute", help="mute yourself")
async def mute(ctx):
    mutedList.append(ctx.author)
    await ctx.send("You are now muted")

@bot.command(name="unmute", help= "Unmute yourself")
async def unmute(ctx):
    if(ctx.author in mutedList):
        mutedList.remove(ctx.author)
        await ctx.send("You are now unmuted")
    else:
        await ctx.send("You are not muted")

@bot.command(name="hotpic", help="gives a nice ecchi pic")
async def pic(ctx):
    hot_ecchi = subreddit_ecchi.hot(limit=50)
    for item in hot_ecchi:
        hotlinks.append(item)
    response = random.choice(hotlinks)
    await ctx.send(response.url)

@bot.command(name="pic", help="gives a nice ecchi pic")
async def pic(ctx):
    response = random.choice(piclinks)
    await ctx.send(response.url)

@bot.command(name="hotthigh", help="gives a nice thigh pic")
async def pic(ctx):
    hot_thigh = subreddit_thighdeology.hot(limit=50)
    for item in hot_thigh:
        hotthighlinks.append(item)
    response = random.choice(hotthighlinks)
    await ctx.send(response.url)

@bot.command(name="thigh", help="gives a top thigh pic")
async def pic(ctx):
    hot_thigh = subreddit_thighdeology.top(limit=100)
    for item in hot_thigh:
        topthighlinks.append(item)
    response = random.choice(topthighlinks)
    await ctx.send(response.url)

@bot.command(name="so", help="Sara Orrego pic")
async def pic(ctx):
    hot_sara = subreddit_so.top(limit=100)
    for item in hot_sara:
        solinks.append(item)
    response = random.choice(solinks)
    await ctx.send(response.url)

@bot.command(name="tits", help="Big Anime Tits")
async def pic(ctx):
    top_tits = subreddit_tits.top(limit = 100)
    for item in top_tits:
        titlinks.append(item)
    response = random.choice(titlinks)
    usedLinks.append(response)
    await ctx.send(response.url)

@bot.command(name="sauce", help="gives sauce :smirk:")
async def sauce(ctx):
    sauce = [
    ("https://imgur.com/a/x4qYloJ#keyug9l", 279963, "After Relentlessly Cumming Inside a Runaway Gyaru, We Started Living Together as Fuck Buddies"),
    ("https://imgur.com/a/XIYB71N", 286444, "Muramata-san's secret"),
    ("https://imgur.com/a/Hl36PeL", 313039, "Welcome to the Residence with Glory Holes"),
    ("https://imgur.com/a/eQR65xz", 324278, "I Am the Only Boy in Our Class"),
    ("https://imgur.com/a/5mnTM03", 285588, "5th Year After School"),
    ("https://imgur.com/a/3N8lh6J", "No sauce :pensive:", "Fucking the Gals Who Nonchalantly Came into My Room"),
    ("https://imgur.com/a/UITDW", 285330, "My Classmate's Young Mom"),
    ("https://imgur.com/a/VU2WX6v", 321889, "A Certain Day when a College Student was the Laziest"),
    ("https://imgur.com/a/VJAXy7c", 298547, "Half Seduction"),
    ("https://imgur.com/a/rE3hcVs", 318224, "It's So Hot That My Girlfriend Has To Blow Me Down"),
    ]
    response = random.choice(sauce)
    await ctx.send(response[0])
    await ctx.send("Sauce: " + str(response[1]))
    await ctx.send("Title: " + response[2])

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

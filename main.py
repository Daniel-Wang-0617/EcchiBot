import os
import requests
import random
import discord
import asyncio
import time
import praw
from discord.ext import commands

bot = commands.Bot(command_prefix="e.")

#client = discord.Client()

TOKEN = ""

reddit = praw.Reddit(client_id = 'C0EVE0NpVGV8PQ', client_secret = 'pMwTwwG96WWCwSvt5Qjajmd3BI4s7A', username = 'EcchiBot', password = 'ecchibot', user_agent = 'EcchiBot')

subreddit_ecchi = reddit.subreddit('ecchi')
subreddit_thighdeology = reddit.subreddit('thighdeology')
subreddit_so = reddit.subreddit('SaraOrrego')
subreddit_tits = reddit.subreddit('BigAnimeTiddies')



@bot.event
async def on_ready():
    numPeople = 0
    for server in bot.guilds:
        numPeople +=len(server.members)
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="{} people fail NNN".format(numPeople)))
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
    # sent = False
    # if(sent==False):
    #     await message.channel.send("Hi. How are you?")
    #     sent = True
    # if message.author == bot.user:
    #     return
    # if "shitij" in message.content.lower():
    #     print(message.content)
    # if "bot" in message.content.lower():
    #     print(message.content)
    # if "e." in message.content.lower():
    #     print(message.content)
    # print(message.content)

usedLinks = []
usedSauce = []
piclinks =[]
hotlinks = []
hotthighlinks = []
topthighlinks = []
solinks = []
titlinks = []

for item in reddit.user.me().saved(limit=None):
    piclinks.append(item)


@bot.command(name="hotpic", help="gives a nice ecchi pic")
async def pic(ctx):
    hot_ecchi = subreddit_ecchi.hot(limit=50)
    for item in hot_ecchi:
        hotlinks.append(item)
    if(len(usedLinks)>15):
        usedLinks.pop(0)
    response = random.choice(hotlinks)
    while(response in usedLinks):
        response = random.choice(hotlinks)
    usedLinks.append(response)
    print(response.url)
    await ctx.send(response.url)

@bot.command(name="pic", help="gives a nice ecchi pic")
async def pic(ctx):
    if(len(usedLinks)>15):
        usedLinks.pop(0)
    response = random.choice(piclinks)
    while(response in usedLinks):
        response = random.choice(piclinks)
    usedLinks.append(response)
    print(response.url)
    await ctx.send(response.url)

@bot.command(name="hotthigh", help="gives a nice thigh pic")
async def pic(ctx):
    hot_thigh = subreddit_thighdeology.hot(limit=50)
    for item in hot_thigh:
        hotthighlinks.append(item)
    if(len(usedLinks)>15):
        usedLinks.pop(0)
    response = random.choice(hotthighlinks)
    while(response in usedLinks):
        response = random.choice(hotthighlinks)
    usedLinks.append(response)
    await ctx.send(response.url)

@bot.command(name="thigh", help="gives a top thigh pic")
async def pic(ctx):
    hot_thigh = subreddit_thighdeology.top(limit=100)
    for item in hot_thigh:
        topthighlinks.append(item)
    if(len(usedLinks)>15):
        usedLinks.pop(0)
    response = random.choice(topthighlinks)
    while(response in usedLinks):
        response = random.choice(topthighlinks)
    usedLinks.append(response)
    await ctx.send(response.url)

@bot.command(name="so", help="Sara Orrego pic")
async def pic(ctx):
    hot_sara = subreddit_so.top(limit=100)
    for item in hot_sara:
        solinks.append(item)
    if(len(usedLinks)>15):
        usedLinks.pop(0)
    response = random.choice(solinks)
    while(response in usedLinks):
        response = random.choice(hotgiflinks)
    usedLinks.append(response)
    await ctx.send(response.url)

@bot.command(name="tits", help="Big Anime Tits")
async def pic(ctx):
    top_tits = subreddit_tits.top(limit = 100)
    for item in top_tits:
        titlinks.append(item)
    if(len(usedLinks)>15):
        usedLinks.pop(0)
    response = random.choice(titlinks)
    while(response in usedLinks):
        response = random.choice(titlinks)
    usedLinks.append(response)
    await ctx.send(response.url)

@bot.command(name="sauce", help="gives sauce :smirk:")
async def sauce(ctx):
    if(len(usedSauce)>5):
        usedSauce.pop(0)
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
    while(response in usedSauce):
        response = random.choice(sauce)
    usedSauce.append(response)
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

import os
import requests
import random
import discord
import asyncio
import time
import praw
from discord.ext import commands

bot = commands.Bot(command_prefix="e.")

TOKEN = ""

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

@bot.command(name="schedule", help="prints the titles of anime that are airing on a given day at JST time")
async def schedule(ctx, day):
  url = f"https://jikan1.p.rapidapi.com/schedule/{day}"

  params = {"format": "json"}

  headers = {
    'x-rapidapi-host': "jikan1.p.rapidapi.com",
      'x-rapidapi-key': "e70f6faedemsh1bf61b13a1ec429p1da9d3jsn73fc3e3b1f9f"
  }

  response = requests.request("GET", url, headers=headers, params=params).json()

  response_list = response[str(day)]

  title_list = []

  for n in range(0, len(response_list)):
    title_list.append(response_list[n]["title"])

  await ctx.send(title_list)

@bot.command(name="search", help="searches info of medium given. to make search more accurate, don\'t include spaces.")
async def search(ctx, medium, title):
  url = f"https://jikan1.p.rapidapi.com/search/{medium}"

  params = {"q": str(title), "format": "json"}

  headers = {
    'x-rapidapi-host': "jikan1.p.rapidapi.com",
      'x-rapidapi-key': "e70f6faedemsh1bf61b13a1ec429p1da9d3jsn73fc3e3b1f9f"
  }

  response = requests.request("GET", url, headers=headers, params=params).json()

  response_list = response["results"][0]

  await ctx.send(response_list)


bot.run(TOKEN)

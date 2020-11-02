import os
import requests
import random
import discord
import asyncio
from discord.ext import commands

bot = commands.Bot(command_prefix="e.")

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

@bot.event
async def on_message(message):
    await bot.process_commands(message)
    if message.author == bot.user:
        return
    if "shitij" in message.content.lower():
        print(message.content)

usedLinks = []
usedSauce = []

@bot.command(name="pic", help="gives a nice ecchi pic")
async def pic(ctx):
    if(len(usedLinks)>5):
        usedLinks.pop(0)
    links = [
    ("https://external-preview.redd.it/JFE4Jek_WZNlBLyJtvw_moBgMfU6jjCeXBkTcBtzOwU.jpg?width=640&crop=smart&auto=webp&s=ca8cff352d7ef60ecd68e19679e7d488b7099509","Pretty nice"),
    ("https://preview.redd.it/unylvn8av6841.jpg?width=640&crop=smart&auto=webp&s=8a5491b7373715e3df9b118855269a92a659ab88","Hey, stop doing that"),
    ("https://preview.redd.it/fhqp4rfqsqk51.jpg?width=640&crop=smart&auto=webp&s=93d10f754a091d1bda7c86846d76af4558ae29ca","Perfection"),
    ("https://media.discordapp.net/attachments/753771988035829771/772168084726611988/image0.jpg?width=260&height=382","Succubi aren't bad once in a while"),
    ("https://external-preview.redd.it/LZ-oHsJQ-OB1bxgxrpi1I3iE_OoqgSUWvMCM3A4A4SA.jpg?width=640&crop=smart&auto=webp&s=ff353c5398b2f051ada3acc4e05585081dccb2d9","Heaven"),
    ("https://external-preview.redd.it/gZpTIdVvnbLR2MKEP_fzGbAPl3kHF_ew4MjFPQPH6Uw.jpg?width=640&crop=smart&auto=webp&s=5d10aeecad9b6f64a2ea1f7dad7f1208e0abe6ae","Morning mood"),
    ("https://preview.redd.it/e2sznt2j6cs41.jpg?width=640&crop=smart&auto=webp&s=4dee9375ad1318f0e2822f6884895fe0c5779d08","Perfectly size"),
    ("https://preview.redd.it/s7ywboahs6l51.jpg?width=640&crop=smart&auto=webp&s=b54e8cc5f424a6e78b36bc2e4341a6f445198b28","Yummy cake"),
    ("https://preview.redd.it/r34egybf63951.jpg?width=640&crop=smart&auto=webp&s=262b760fb6f37900a311cf6dc1d5aa8b5b7e13dc","Shhhhh, don't make any noise"),
    ("https://preview.redd.it/4wiuzkrpoj251.jpg?width=640&crop=smart&auto=webp&s=4eb33f26eb2b802fe6213517c0efdcf9b5d9cfa2","Ready for some action?"),
    ("https://preview.redd.it/m9zjecmixlg51.jpg?width=640&crop=smart&auto=webp&s=4a28d7d3d36ecf8c871928928500f2789cba7f6e","Just plain hot"),
    ("https://preview.redd.it/xvma95gd0ky41.jpg?width=640&crop=smart&auto=webp&s=12f54393097b542b8ad808a20503fa8cbca617de","B-b-baka don't look at me like that"),
    ("https://external-preview.redd.it/_z6uqLe95Auuo0a0nfzwXoHtqBsTCC-m8dphKvgM76A.jpg?width=640&crop=smart&auto=webp&s=9c9654fd58b8525fb498407721ba16af32bd7100","Everything cultured in one picture"),
    ("https://preview.redd.it/j40nm267p1u51.jpg?width=640&crop=smart&auto=webp&s=912939b23571e128e4ae8f34736609c6f475395b","Amber has a side quest for you"),
    ("https://external-preview.redd.it/8HI3IdwlyqAesZKEsYT66qUON8vnR7CzHgS-yPduBQQ.jpg?width=640&crop=smart&auto=webp&s=7cacc990d21e007b6cb09e587eb2e052578fa81b","Nice ass"),
    ("https://preview.redd.it/yyn43dqbfnu51.jpg?width=640&crop=smart&auto=webp&s=e71763279d69a79529e019ea6e7e047db94b769e", "Maybe we can untie it after school :smirk:"),
    ("https://external-preview.redd.it/bHC1nlxD8GCDgM4hgb9WQxEQLUx9ojnIp-HTKzzg5bs.png?width=640&crop=smart&auto=webp&s=4996ac3951fb4bc0bdcf2e65fe16b37a0619cffe", "Never can go wrong with guns and girls"),
    ]
    response = random.choice(links)
    while(response in usedLinks):
        response = random.choice(links)
    usedLinks.append(response)
    await ctx.send(response[0])
    await ctx.send(response[1])

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

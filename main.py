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

subreddit = reddit.subreddit('ecchi')

hot_ecchi = subreddit.hot()

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
    

usedLinks = []
usedSauce = []
links =[]

for submission in hot_ecchi:
    links.append(submission)

@bot.command(name="pic", help="gives a nice ecchi pic")
async def pic(ctx):
    count =0
    if(len(usedLinks)>15):
        usedLinks.pop(0)
    # links = [
    # ("https://external-preview.redd.it/JFE4Jek_WZNlBLyJtvw_moBgMfU6jjCeXBkTcBtzOwU.jpg?width=640&crop=smart&auto=webp&s=ca8cff352d7ef60ecd68e19679e7d488b7099509","Pretty nice"),
    # ("https://preview.redd.it/unylvn8av6841.jpg?width=640&crop=smart&auto=webp&s=8a5491b7373715e3df9b118855269a92a659ab88","Hey, stop doing that"),
    # ("https://preview.redd.it/fhqp4rfqsqk51.jpg?width=640&crop=smart&auto=webp&s=93d10f754a091d1bda7c86846d76af4558ae29ca","Perfection"),
    # ("https://media.discordapp.net/attachments/753771988035829771/772168084726611988/image0.jpg?width=260&height=382","Succubi aren't bad once in a while"),
    # ("https://external-preview.redd.it/LZ-oHsJQ-OB1bxgxrpi1I3iE_OoqgSUWvMCM3A4A4SA.jpg?width=640&crop=smart&auto=webp&s=ff353c5398b2f051ada3acc4e05585081dccb2d9","Heaven"),
    # ("https://external-preview.redd.it/gZpTIdVvnbLR2MKEP_fzGbAPl3kHF_ew4MjFPQPH6Uw.jpg?width=640&crop=smart&auto=webp&s=5d10aeecad9b6f64a2ea1f7dad7f1208e0abe6ae","Morning mood"),
    # ("https://preview.redd.it/e2sznt2j6cs41.jpg?width=640&crop=smart&auto=webp&s=4dee9375ad1318f0e2822f6884895fe0c5779d08","Perfectly size"),
    # ("https://preview.redd.it/s7ywboahs6l51.jpg?width=640&crop=smart&auto=webp&s=b54e8cc5f424a6e78b36bc2e4341a6f445198b28","Yummy cake"),
    # ("https://preview.redd.it/r34egybf63951.jpg?width=640&crop=smart&auto=webp&s=262b760fb6f37900a311cf6dc1d5aa8b5b7e13dc","Shhhhh, don't make any noise"),
    # ("https://preview.redd.it/4wiuzkrpoj251.jpg?width=640&crop=smart&auto=webp&s=4eb33f26eb2b802fe6213517c0efdcf9b5d9cfa2","Ready for some action?"),
    # ("https://preview.redd.it/m9zjecmixlg51.jpg?width=640&crop=smart&auto=webp&s=4a28d7d3d36ecf8c871928928500f2789cba7f6e","Just plain hot"),
    # ("https://preview.redd.it/xvma95gd0ky41.jpg?width=640&crop=smart&auto=webp&s=12f54393097b542b8ad808a20503fa8cbca617de","B-b-baka don't look at me like that"),
    # ("https://external-preview.redd.it/_z6uqLe95Auuo0a0nfzwXoHtqBsTCC-m8dphKvgM76A.jpg?width=640&crop=smart&auto=webp&s=9c9654fd58b8525fb498407721ba16af32bd7100","Everything cultured in one picture"),
    # ("https://preview.redd.it/j40nm267p1u51.jpg?width=640&crop=smart&auto=webp&s=912939b23571e128e4ae8f34736609c6f475395b","Amber has a side quest for you"),
    # ("https://external-preview.redd.it/8HI3IdwlyqAesZKEsYT66qUON8vnR7CzHgS-yPduBQQ.jpg?width=640&crop=smart&auto=webp&s=7cacc990d21e007b6cb09e587eb2e052578fa81b","Nice ass"),
    # ("https://preview.redd.it/yyn43dqbfnu51.jpg?width=640&crop=smart&auto=webp&s=e71763279d69a79529e019ea6e7e047db94b769e", "Maybe we can untie it after school :smirk:"),
    # ("https://external-preview.redd.it/bHC1nlxD8GCDgM4hgb9WQxEQLUx9ojnIp-HTKzzg5bs.png?width=640&crop=smart&auto=webp&s=4996ac3951fb4bc0bdcf2e65fe16b37a0619cffe", "Never can go wrong with guns and girls"),
    # ("https://preview.redd.it/40wgml69wfw51.jpg?width=640&crop=smart&auto=webp&s=aad731ee264db6091d3fcfa07ac58360ff5b68cf", "Do you want to join us? :smirk:"),
    # ("https://i.redd.it/rijra7j20yk51.png", "Hayasaka best girl"),
    # ("https://preview.redd.it/orcjhvaearq51.png?width=640&crop=smart&auto=webp&s=354d80bda072cef8aa4edd9658e7803b62c7ed4a", "Megumin's Megumins and Yunyun's Yunyuns"),
    # ("https://external-preview.redd.it/-ya8ijmoZw5QyhAcSO2DvqrcIJbEPpsCms37iLJIXgk.jpg?width=640&crop=smart&auto=webp&s=5fda45c15462b9a0ebe1c6952889a8ece209a36f", "Shirt lift"),
    # ("https://preview.redd.it/c340lmpl4gu51.jpg?width=640&crop=smart&auto=webp&s=c1a879a23b7f6ff99c172fe509d0b9913a9e1249", "Senpai, we have a little bit of time before class"),
    # ("https://preview.redd.it/gusd6cl30tw51.jpg?width=640&crop=smart&auto=webp&s=59fedf4f70e6bba74eed185ee0b106f848a37249", "Mona's thicc ass"),
    # ("https://external-preview.redd.it/7jufJCbh2l9h98fwqn4T4ynYYbqG2XhroAEC7EKYB3I.png?width=640&crop=smart&auto=webp&s=bcceb2087672ff3ea51b3e63be2da94f8a3744ce", "God bless this trend"),
    # ("https://preview.redd.it/9eiedvw8hls51.jpg?width=640&crop=smart&auto=webp&s=e9c3e288b849de492ed2035a038f915217886b4e", "Restaurant Girls"),
    # ("https://preview.redd.it/nhhy4xmoy6u31.png?width=640&crop=smart&auto=webp&s=48bd9c08bccd1bc57238a3e49cc4d8aecb7c5725", "Perfection in an image"),
    # ("https://preview.redd.it/t68jy54ip9f31.jpg?width=640&crop=smart&auto=webp&s=d58d8ba43dec5c8ba036b36179c5a577dbc0b6e5", "Cat girls are meowwwstanding"),
    # ("https://preview.redd.it/8oz8w8p79dm51.png?width=640&crop=smart&auto=webp&s=da2013d83ca080e357e17837f4a269db70fcd020", "Ass? Anyone?"),
    # ("https://preview.redd.it/xrn3yxhwaro51.jpg?width=640&crop=smart&auto=webp&s=6a9d35e3c7edbefda74b77e117699659051f2c27", "Waking up is hard"),
    # ("https://external-preview.redd.it/3u3ciWfYKzJbyV9i9ZKnGLMtnoog9lG0A5y9-ydhIIE.jpg?width=640&crop=smart&auto=webp&s=90e35e69aa931919cd0f658294ece922e6f3fd07", "They're showing off"),
    # ("https://preview.redd.it/ef9pf937vab41.jpg?width=640&crop=smart&auto=webp&s=08e8e1e73444db411af9123f47c64edacde147ce", "watching lewd stuff together"),
    # ("https://preview.redd.it/qk1yj1fcniv51.jpg?width=640&crop=smart&auto=webp&s=8e5025bbdf325ca6a1a0eec731ae6c6d945608c5","Ohaiyoo"),
    # ("https://preview.redd.it/ri7kvwyfjfd51.jpg?width=640&crop=smart&auto=webp&s=70de2cdc286e2dd84ecf8633b2c46f10a445b139","Cue ara ara noises"),
    # ("https://preview.redd.it/y7pvryl1qrt51.jpg?width=640&crop=smart&auto=webp&s=030b65864b191d25decd6272b1d03c2045328d72","The best view"),
    # ("https://preview.redd.it/57lt629uocj51.jpg?width=640&crop=smart&auto=webp&s=73a9523cf3c9426a25be3b4f09c6f2aa0c35b325", "Do you like it"),
    # ("https://preview.redd.it/rwell1gl5mm51.jpg?width=640&crop=smart&auto=webp&s=c5d9cf8f55fedf8aacd762f9f64b50daf2bc0562", "A little shy"),
    # ("https://external-preview.redd.it/DpjopH_8hIBiD_fCdY1KoRHcA2uQzI8nW8JoDnEun6w.png?width=640&crop=smart&auto=webp&s=d00eb9d1b93b4b302d48ad152725d9b055e721e7", "Yuudachi lookin like a snacc"),
    # ("https://i.redd.it/lyos68fsxss51.jpg", "Perfectly balanced, as all things should be"),
    # ("https://preview.redd.it/0gqxj0v9lhw31.jpg?width=640&crop=smart&auto=webp&s=08dbe02b7d3b96c67d6d40873b42e62271ce5b04", "Some nice curves"),
    # ("https://external-preview.redd.it/Ce_aHOPJqUnJRooUqU1RHn67jt8tyvW_s1XYfwtTtgc.jpg?width=640&crop=smart&auto=webp&s=37a95109a7a6fd1a018427877ac6309b077aa818","A nice beach episode"),
    # ("https://preview.redd.it/5plndzp7zhq51.jpg?width=640&crop=smart&auto=webp&s=17432d792bc4dba9f891d3d931ee333decc085ec", "Can't go wrong with dark-skinned elves"),
    # ("https://preview.redd.it/kfloqaimtpp51.jpg?width=640&crop=smart&auto=webp&s=17dffc4127d0d7d25345988247b486dee0fa51f3", "Enough to excite someone"),
    # ("https://preview.redd.it/yv4ujwds8xh41.jpg?width=640&crop=smart&auto=webp&s=6c39a79d3edca0de09d5f4f9e7db1f413f6e110b", "Hey, don't look at me like that"),
    # ("https://preview.redd.it/vsujzna1egr51.jpg?width=640&crop=smart&auto=webp&s=3385128bb5befb471c254220a58168dc0b63ef73", "Sharing with the class"),
    # ("https://preview.redd.it/0uv6a982q1v51.jpg?width=640&crop=smart&auto=webp&s=ca2b822589f0bd404004db71435218491bbbc87f", "Thicc thigh senpai"),
    # ("https://preview.redd.it/7ltp1rdcnmo41.jpg?width=640&crop=smart&auto=webp&s=02ff262dbf0398c42a08e190af7e556eb3d996c2", "Goddess"),
    # ("https://preview.redd.it/vlb3xob1zrw41.jpg?width=640&crop=smart&auto=webp&s=3308bc684ef81b8b2f020d234500e515f2b20556", "How does it look back there"),
    # ("https://preview.redd.it/y4lpt8jzpmi51.jpg?width=640&crop=smart&auto=webp&s=2d0225422c0801d168844f403576dca706718282", "Ready to get the job done"),
    # ("https://preview.redd.it/maf4zf5nv4h41.jpg?width=640&crop=smart&auto=webp&s=1b353530a70c965df1e7beda72fe21a6c6b2a7e9", "These eyes :eyes:"),
    # ("https://preview.redd.it/2097u246yph51.png?width=640&crop=smart&auto=webp&s=17a849b6cf50f0ec8c6a93070c77a10694ba3bff", "Realistic thighs"),
    # ("https://external-preview.redd.it/wZU2LWXgpfydkbNf08QkgKqeM90VEc1nJJtzojovoxI.jpg?width=640&crop=smart&auto=webp&s=fcabbb0d2a8b250187e3718ad3d4a480f1874cb9", "Sometimes the right amount of clothes is hotter than no clothes"),
    # ("https://i.redd.it/2kj3kdap9uj41.jpg", "Is the Violet Evergarden??"),
    # ("https://preview.redd.it/th7fe9ixt4o51.jpg?width=640&crop=smart&auto=webp&s=4dcdb371552befbef0233572ce81cfffe13beebe", "Echidna wearing her socks"),
    # ("https://preview.redd.it/a0bol5rtb8551.jpg?width=640&crop=smart&auto=webp&s=9352bad3c508712d64883049b85e8fcc8540b8b3", "Licking a phallus"),
    # ("https://preview.redd.it/9g9nqhmq83q51.jpg?width=640&crop=smart&auto=webp&s=43c51b013616b8515e89ce4de6c2660a17099b2c", "She's a little shy"),
    # ("https://preview.redd.it/8k2iquu9m6m51.png?width=640&crop=smart&auto=webp&s=b4d2e0ad280045636a474beeb90c38eabe2f3f48", "White lingerie"),
    # ("https://preview.redd.it/fnokajtwk0o51.jpg?width=640&crop=smart&auto=webp&s=f4e17c43114ca19feb8082d506fbdeb84ee47f92", "Kawaii"),
    # ("https://preview.redd.it/b83eshq6u4n51.png?width=640&crop=smart&auto=webp&s=1a50022a30727078a41a955c2b08d88af77934c7", "Quintuplets"),
    # ("https://preview.redd.it/3q4q5lgi2de51.jpg?width=640&crop=smart&auto=webp&s=ba1d8b39290775fbb2cc131a9aa93feb15339279", "For ashmit"),
    # ("https://i.redd.it/1y7ifnadqnr51.jpg", "View after a sweaty workout"),
    # ("https://external-preview.redd.it/63fcNFQFZqKxxHfWjxzzY3XsxwrE_1dOw84LM5V_wlQ.png?auto=webp&s=a8eb7a9a5f12e47cfbf180cf4c7945b974907d7a", "Bathing"),
    # ("https://external-preview.redd.it/_af22E0EsTsnp8RA5tk0GjsakNH1SlqeX-Q9c2hjIUQ.jpg?width=640&crop=smart&auto=webp&s=8b36b09f25bdbd2f4d6a5dce1fc518ac96b0b61c","Girls' locker room"),
    # ("https://preview.redd.it/2ly38wrmzst41.jpg?width=640&crop=smart&auto=webp&s=3f0716111c1a4834db4990a690966e4c2b3c02de", "Nice swimsuit"),
    # ("https://external-preview.redd.it/Uz_RYesqBvNCtVwsUYxoQUTkOPUVp-UfqqeLsI_QnIw.png?width=640&crop=smart&auto=webp&s=b6ec8bf6895be32e1cf0f915bb851a10cf642741", "Well endowed blond women"),
    # ("https://preview.redd.it/7zbefpv29ty41.jpg?width=640&crop=smart&auto=webp&s=b2dbee6c3614bb0cf5bc2bef834e7e1ba1fef9ef", "More tits for ashmit"),
    # ("https://preview.redd.it/bwkq5csvrlb21.png?width=640&crop=smart&auto=webp&s=54b7341dd0ab19ad528ec5be1213ec0603f1f3b8", "Just monika"),
    # ("https://external-preview.redd.it/gHET1Si_ZQ5TLN6kxLuQL9EsPiKWk0_bfZZo6iyRamI.jpg?width=640&crop=smart&auto=webp&s=5ad5a74f13525303fe0b90f95068de2782327ab3", "Ark Royal"),
    # ("https://preview.redd.it/gohi3kibfhl51.jpg?width=640&crop=smart&auto=webp&s=fdd672eadc51e29b5e9f296c9189a73d9797da55", "For ashmit as well"),
    # ("https://preview.redd.it/0h1e7egyluu51.jpg?width=640&crop=smart&auto=webp&s=3eb5cfdaccaf24b03cd48ee1182e9e136065e454", "Senpai you're taking too long. Choose quickly"),
    #
    # ]

    #s = r.user.get_saved(params = {'sr':'ecchi'})
    #print(s)

    response = random.choice(links)
    while(response in usedLinks):
        response = random.choice(links)
    usedLinks.append(response)
    print(response.url)
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

from NHentai import NHentai
import discord

nhentai = NHentai()
blacklist = ["double penetration", "anal", "yaoi", "lolicon", "rape", "ugly bastard"]

async def create_embed(title, url, description, thumbnail, tags, pages, ctx):
    embed = discord.Embed(title=title, url=url, description= description)
    embed.set_thumbnail(url=thumbnail)
    embed.add_field(name="Tags", value = tags)
    embed.set_footer(text = "Total pages {}".format(pages))
    await ctx.send(embed = embed)


async def random_sauce(ctx):
    found_doujin = False
    while(not found_doujin):
        random_doujin: Doujin = nhentai.get_random()
        # Get a good english doujin without no-no things
        if("english" in random_doujin.languages and not any(item in blacklist for item in random_doujin.tags)):
            print(dir(random_doujin))
            # Generate tags m
            tags =""
            for cat in random_doujin.tags:
                tags+=cat
                tags+=", "
            title = random_doujin.title
            url = "https://nhentai.net/g/{}".format(random_doujin.id)
            thumbnail = random_doujin.images[0]
            description = random_doujin.secondary_title
            total_pages = random_doujin.total_pages
            await create_embed(title, url, description, thumbnail, tags, total_pages, ctx)
            found_doujin = True
            break
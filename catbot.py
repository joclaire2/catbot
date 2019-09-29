# Work with Python 3.6 only

import os
import discord
#import unsplash

from dotenv import load_dotenv

load_dotenv()
token = os.getenv('DISCORD_TOKEN')

client = discord.Client()

# -------------------------------------------------------

@client.event
async def on_message(message):
    # we do not want the bot to reply to itself
    if message.author == client.user:
        return

    if (message.content.startswith('hello') or message.content.startswith('hey') or  message.content.startswith('hi')):
        print(f"Saying hi to {message.author.name}")
        msg = 'Hello! {0.author.mention}'.format(message)
        print(msg)
        await client.send_message(message.channel, msg)

    if (message.content.startswith('c.pic') or message.content.startswith('c.picture')):
        print(f"Sending {message.author.name} a cat pic")
        msg = 'Here is a cute cat for you~! {0.author.mention}'.format(message)
        print(msg)
        await client.send_message(message.channel, msg)
        with open('images/ragdoll.jpg', 'rb') as picture:
            await client.send_file(message.channel, picture)

    if (message.content.startswith('c.info') or message.content.startswith('c.botinfo')):
        print(f"telling {message.author.name} info about catbot")
        embed = discord.Embed(title="catbot", description="catbot is a basic bot with cute mini games where you can collect cats (=ᵔ ﻌ ᵔ=)ﾉ", color=0x4c8cd6)
        embed.add_field(name="Authors", value="@joclaire2#5534 (bot design) and @ribman#7979 (bot coding)")
        embed.add_field(name="Invite link", value="[Click here to invite catbot to your server!](<https://discordapp.com/api/oauth2/authorize?client_id=625644432741629992&permissions=388160&scope=bot>)")
        embed.add_field(name="Official catbot support server", value="[Click here to join our server!](<https://discord.gg/G6A4VEa>)")
        print(embed)
        await client.send_message(message.channel, embed=embed)

    if message.content.startswith('c.api'):
        print(f"Sending {message.author.name} a cat pic from unsplash")
        game = message.content[6:]
        gres = requests.get('https://api.steampowered.com/ISteamApps/GetAppList/v2/')
        gdata = gres.json()
        print (gdata)
        for i in gdata["applist"]["apps"]:
            if (i["name"] == game):
                app = (i["appid"])
                priceres = requests.get(f"https://store.steampowered.com/api/appdetails/?appids={app}")
                priced = priceres.json()
                price = (priced[f"{app}"]["data"]["price_overview"].get("final"))

    if message.content.startswith('!api'):
        game = message.content[5:]
        print(f"the words after 'api' were: {game}")
        gres = requests.get('https://api.steampowered.com/ISteamApps/GetAppList/v2/')
        gdata = gres.json()
        for i in gdata["applist"]["apps"]:
            if (i["name"] == game):
                app = (i["appid"])
                priceres = requests.get(f"https://store.steampowered.com/api/appdetails/?appids={app}")
                priced = priceres.json()
                price = (priced[f"{app}"]["data"]["price_overview"].get("final"))
                msg = f"{game} is currently{price}".format(message)
                await client.send_message(message.channel, msg)

# -------------------------------------------------------
@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

client.run(token)

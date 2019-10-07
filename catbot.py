# catbot runner
# version 0.2.0+
# =======================================================
import os
from dotenv import load_dotenv
load_dotenv('../.secure/.env')
token = os.getenv('DISCORD_TOKEN')
# =======================================================
import discord
from discord.ext import commands
# =======================================================
# Create the bot
client = discord.Client()
# =======================================================
@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

# =======================================================
@client.event
async def on_message(message):
    msgAuthor = message.author
    # we do not want the bot to reply to itself
    if msgAuthor == client.user:
        return
        
    # setup shared common settings
    msgText = message.content.lower()
    msgrName = msgAuthor.name
    msgChannel = message.channel

# -------------------------------------------------------
    if (msgText.startswith('hello') or msgText.startswith('hey') or  msgText.startswith('hi')):
        print(f"Saying hi to {msgrName}")
        msg = f"Hello! {msgAuthor.mention}"
        embed = discord.Embed(title="(✿◕‿◠)~★", description=msg, color=0x4c8cd6)
        print(embed)
        await msgChannel.send(embed=embed)

# -------------------------------------------------------
    if (msgText.startswith('c.pic') or msgText.startswith('c.picture')):
        print(f"Sending {msgrName} a cat pic")
        embed = discord.Embed(title="(づ｡◕‿‿◕｡)づ", description="Here is a cute cat for you~!", color=0x4c8cd6)
        embed.set_image(url="https://images.unsplash.com/photo-1532386236358-a33d8a9434e3?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=500&q=60")
        embed.add_field(name="Credit", value="Photo by Raul Varzar https://unsplash.com/@calypso999 on Unsplash https://unsplash.com/")
        print(embed)
        await msgChannel.send(embed=embed)

# -------------------------------------------------------
    if (msgText.startswith('c.info') or msgText.startswith('c.botinfo')):
        print(f"telling {msgrName} info about catbot")
        embed = discord.Embed(title="(✿◕‿◠)~★", description="catbot is a basic bot with cute mini games where you can collect cats (=ᵔ ﻌ ᵔ=)ﾉ", color=0x4c8cd6)
        embed.add_field(name="Authors", value="@joclaire2#5534 (bot design) and @ribman#7979 (bot coding)")
        embed.add_field(name="Invite link", value="[Click here to invite catbot to your server!](<https://discordapp.com/api/oauth2/authorize?client_id=625644432741629992&permissions=388160&scope=bot>)")
        embed.add_field(name="Official catbot support server", value="[Click here to join our server!](<https://discord.gg/G6A4VEa>)")
        print(embed)
        await msgChannel.send(embed=embed)

# =======================================================
# Create the bot
client.run(token)
# =======================================================

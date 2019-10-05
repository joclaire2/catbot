# catbot runner
# version 0.2.0+
# =======================================================
import os
from dotenv import load_dotenv
load_dotenv()
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
    # we do not want the bot to reply to itself
    if message.author == client.user:
        return

# -------------------------------------------------------
    if (message.content.lower().startswith('hello') or message.content.lower().startswith('hey') or  message.content.lower().startswith('hi')):
        print(f"Saying hi to {message.author.name}")
        msg = f"Hello! {message.author.mention}"
        #msg = 'Hello! {0.author.mention}'.format(message)
        embed = discord.Embed(title="(✿◕‿◠)~★", description=msg, color=0x4c8cd6)
        print(embed)
        await client.send_message(message.channel, embed=embed)

# -------------------------------------------------------
    if (message.content.lower().startswith('c.pic') or message.content.lower().startswith('c.picture')):
        print(f"Sending {message.author.name} a cat pic")
        embed = discord.Embed(title="(✿◕‿◠)~★", description="Here is a cute cat for you~!", color=0x4c8cd6)
        embed.set_image(url="https://images.unsplash.com/photo-1532386236358-a33d8a9434e3?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=500&q=60")
        embed.add_field(name="Credit", value="Photo by Raul Varzar https://unsplash.com/@calypso999 on Unsplash https://unsplash.com/")
        print(embed)
        await client.send_message(message.channel, embed=embed)

# -------------------------------------------------------
    if (message.content.lower().startswith('c.info') or message.content.lower().startswith('c.botinfo')):
        print(f"telling {message.author.name} info about catbot")
        embed = discord.Embed(title="(✿◕‿◠)~★", description="catbot is a basic bot with cute mini games where you can collect cats (=ᵔ ﻌ ᵔ=)ﾉ", color=0x4c8cd6)
        embed.add_field(name="Authors", value="@joclaire2#5534 (bot design) and @ribman#7979 (bot coding)")
        embed.add_field(name="Invite link", value="[Click here to invite catbot to your server!](<https://discordapp.com/api/oauth2/authorize?client_id=625644432741629992&permissions=388160&scope=bot>)")
        embed.add_field(name="Official catbot support server", value="[Click here to join our server!](<https://discord.gg/G6A4VEa>)")
        print(embed)
        await client.send_message(message.channel, embed=embed)

# =======================================================
# Create the bot
client.run(token)
# =======================================================

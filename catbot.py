# catbot.py
# version 0.2.0

import discord
from discord.ext import commands

class Catbot():
def __init__(self, bot):
    self.bot = bot

@commands.command(pass_context=True)
async def hello2(ctx):
    msg = 'Hello there {0.author.mention}'.format(ctx.message)
    await bot.say(msg)

def setup(bot):
bot.add_cog(Second(bot))


# =======================================================
@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')

# =======================================================
@bot.event
async def on_message(message):
    # we do not want the bot to reply to itself
    if message.author == bot.user:
        return

# -------------------------------------------------------
    if (message.content.startswith('hello') or message.content.startswith('hey') or  message.content.startswith('hi')):
        print(f"Saying hi to {message.author.name}")
        msg = f"Hello! {message.author.mention}"
        #msg = 'Hello! {0.author.mention}'.format(message)
        embed = discord.Embed(title="(✿◕‿◠)~★", description=msg, color=0x4c8cd6)
        print(embed)
        await bot.send_message(message.channel, embed=embed)

# -------------------------------------------------------
    if (message.content.startswith('c.pic') or message.content.startswith('c.picture')):
        print(f"Sending {message.author.name} a cat pic")
        embed = discord.Embed(title="(✿◕‿◠)~★", description="Here is a cute cat for you~!", color=0x4c8cd6)
        embed.set_image(url="https://images.unsplash.com/photo-1532386236358-a33d8a9434e3?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=500&q=60")
        embed.add_field(name="Credit", value="Photo by Raul Varzar https://unsplash.com/@calypso999 on Unsplash https://unsplash.com/")
        print(embed)
        await bot.send_message(message.channel, embed=embed)

# -------------------------------------------------------
    if (message.content.startswith('c.info') or message.content.startswith('c.botinfo')):
        print(f"telling {message.author.name} info about catbot")
        embed = discord.Embed(title="(✿◕‿◠)~★", description="bot is a basic bot with cute mini games where you can collect cats (=ᵔ ﻌ ᵔ=)ﾉ", color=0x4c8cd6)
        embed.add_field(name="Authors", value="@joclaire2#5534 (bot design) and @ribman#7979 (bot coding)")
        embed.add_field(name="Invite link", value="[Click here to invite catbot to your server!](<https://discordapp.com/api/oauth2/authorize?client_id=625644432741629992&permissions=388160&scope=bot>)")
        embed.add_field(name="Official catbot support server", value="[Click here to join our server!](<https://discord.gg/G6A4VEa>)")
        print(embed)
        await bot.send_message(message.channel, embed=embed)

# =======================================================
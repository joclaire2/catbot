# catbot runner
# version 0.2.0+
# =======================================================
# Load Discord Library
import discord
from discord.ext import commands

# =======================================================
# Load libraries and global parameters
import os
import random
import string
import sqlite3
from dotenv import load_dotenv
load_dotenv('../.secure/.env')

# =======================================================
# Build Discord Client
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
    embedColor = 0x4c8cd6

# -------------------------------------------------------
    if (msgText.startswith('hello') or msgText.startswith('hey') or  msgText.startswith('hi')):
        print(f"Saying hi to {msgrName}")
        msg = f"Hello! {msgAuthor.mention}"
        embed = discord.Embed(title=random_text_face(), description=msg, color=embedColor)
        print(embed)
        await msgChannel.send(embed=embed)

# -------------------------------------------------------
    if (msgText.startswith('c.pic') or msgText.startswith('c.picture')):
        print(f"Sending {msgrName} a cat pic")
        embed = discord.Embed(title=random_text_face(), description="Here is a cute cat for you~!", color=embedColor)
        seed = ''.join(random.choice(string.ascii_lowercase) for x in range(10))
        catPicUrl = f"https://source.unsplash.com/random/?cat&{seed}"
        print(catPicUrl)
        embed.set_image(url=catPicUrl)
        embed.add_field(name="Credit", value="Photos from [Unsplash](<https://unsplash.com/>)")
        print(embed)
        await msgChannel.send(embed=embed)

# -------------------------------------------------------
    if (msgText.startswith('c.info') or msgText.startswith('c.botinfo')):
        print(f"telling {msgrName} info about catbot")
        embed = discord.Embed(title=random_text_face(), description="catbot is a basic bot with cute mini games where you can collect cats (=ᵔ ﻌ ᵔ=)ﾉ", color=embedColor)
        embed.add_field(name="Authors", value="@joclaire2#5534 (bot design), @ribman#7979 (bot coding) and @hananananah#7858 (illustrations)")
        embed.add_field(name="Invite link", value="[Click here to invite catbot to your server!](<https://discordapp.com/api/oauth2/authorize?client_id=625644432741629992&permissions=388160&scope=bot>)")
        embed.add_field(name="Official catbot support server", value="[Click here to join our server!](<https://discord.gg/G6A4VEa>)")
        print(embed)
        await msgChannel.send(embed=embed)

# -------------------------------------------------------
    if (msgText.startswith('c.loaddb')):
        print(f"Loading db for {msgrName}")
        msg = f"Loading db for {msgAuthor.mention}"
        embed = discord.Embed(title=random_text_face(), description=msg, color=embedColor)
        print(embed)
        await msgChannel.send(embed=embed)
        exec_sql('''CREATE TABLE stocks(date text, trans text, symbol text, qty real, price real)''')
        exec_sql("INSERT INTO stocks VALUES ('2006-01-05','BUY','RHAT',100,35.14)")

# -------------------------------------------------------
    if (msgText.startswith('c.getdata')):
        print(f"Get data for {msgrName}")
        msg = f"Get data for {msgAuthor.mention}"
        embed = discord.Embed(title=random_text_face(), description=msg, color=embedColor)
        print(embed)
        await msgChannel.send(embed=embed)
        RESULT = exec_sql("SELECT * FROM stocks")
        print(RESULT)

# =======================================================
def random_text_face():
    return random.choice(textFaces)
    
# =======================================================
def load_text_faces():
    with open('./text_faces.txt') as f:
        lines = f.read().splitlines()
    return lines

# =======================================================
def exec_sql(sql):
    conn = sqlite3.connect('catbot.db')
    cursor = conn.cursor()
    cursor.execute(sql)
    conn.commit()
    conn.close()
    
# =======================================================
# Set up and run the bot

textFaces = load_text_faces()

token = os.getenv('DISCORD_TOKEN')

client.run(token)
# =======================================================

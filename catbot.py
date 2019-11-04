# catbot runner
# Boot
bot_version = '0.3.0'
from datetime import datetime
from datetime import timedelta
dt_string = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
print(f"{dt_string} Bootup catbot version {bot_version}")
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
dbPath = '../sqllite/catbot.db'

# =======================================================
# Build Discord Client
client = discord.Client()

# -------------------------------------------------------
def get_date():
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

# =======================================================
@client.event
async def on_ready():
    dt_string = get_date()
    print(f"{dt_string} Logged in as")
    print(client.user.name)
    print(client.user.id)
    print('------')

# =======================================================
@client.event
async def on_message(message):
    dt_string = get_date()
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
        print(f"{dt_string} Sending {msgrName} a cat pic")
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
        print(f"{dt_string} Telling {msgrName} info about catbot")
        embed = discord.Embed(title=random_text_face(), description="catbot is a basic bot with cute mini games where you can collect cats (=ᵔ ﻌ ᵔ=)ﾉ", color=embedColor)
        embed.add_field(name="Version", value=bot_version)
        embed.add_field(name="Authors", value="@joclaire2#5534 (bot design), @ribman#7979 (bot coding) and @hananananah#7858 (illustrations)")
        embed.add_field(name="Invite link", value="[Click here to invite catbot to your server!](<https://discordapp.com/api/oauth2/authorize?client_id=625644432741629992&permissions=388160&scope=bot>)")
        embed.add_field(name="Official catbot support server", value="[Click here to join our server!](<https://discord.gg/G6A4VEa>)")
        print(embed)
        await msgChannel.send(embed=embed)

# -------------------------------------------------------
    if (msgText.startswith('c.join')):
        print(f"{dt_string} Adding {msgrName} to db")
        msg = f"Adding {msgAuthor.mention} as a cat owner"
        embed = discord.Embed(title=random_text_face(), description=msg, color=embedColor)
        print(embed)
        await msgChannel.send(embed=embed)
        add_owner(msgrName)

# -------------------------------------------------------
    if (msgText.startswith('c.unjoin')):
        print(f"{dt_string} Removing {msgrName} from db")
        msg = f"Ending {msgAuthor.mention}'s cat ownership"
        embed = discord.Embed(title=random_text_face(), description=msg, color=embedColor)
        embed.add_field(name="You're giving up being a cat owner!", value="Waaaah  :( ")
        print(embed)
        await msgChannel.send(embed=embed)
        remove_owner(msgrName)

# -------------------------------------------------------
    if (msgText.startswith('c.member')):
        print(f"{dt_string} Getting data for {msgrName}")
        result = get_owner(msgrName)
        msg = f"Membership info for {msgAuthor.mention}"
        embed = discord.Embed(title=random_text_face(), description=msg, color=embedColor)
        if len(result) > 0:
            embed.add_field(name="Date joined", value=result[0]['join_date'])
        else:
            embed.add_field(name="You're not a cat owner!", value="tut, tut")
        print(embed)
        await msgChannel.send(embed=embed)
        print(f"{dt_string} Result:\n{result}")

# -------------------------------------------------------
    if (msgText.startswith('c.daily')):
        print(f"{dt_string}, {msgrName} is asking for their daily coin")
        now_dt = datetime.now()
        result = get_owner(msgrName)
        last_daily = result[0].get('last_daily')
        last_dt = datetime.strptime(last_daily, '%Y-%m-%d %H:%M:%S')
        diff_dates = now_dt - last_dt
        msg = f"Hey, {msgAuthor.mention}, I last gave you a coin on {last_dt}, that's {diff_dates} timey-things ago. "
        if diff_dates > timedelta(days=1):
          msg += "Let's give you another one! "
          add_coin(msgrName)
          new_coins = get_coins(msgrName)
          msg += f"Now you have {new_coins} coins."
        else:
          coins = get_coins(msgrName)
          msg += f"You already have {coins} coins. Come back tomorrow and I'll give you another one."
        embed = discord.Embed(title=random_text_face(), description=msg, color=embedColor)
        print(embed)
        await msgChannel.send(embed=embed)

# =======================================================
# This doesn't work yet
# @client.event
async def on_group_join(channel, user):
    dt_string = get_date()
    embedColor = 0x4c8cd6
    print(f"Greeting new arrival {user.name} as at {dt_string} on {channel}")
    msg=''
    if not user.bot:
        msg = f"Ahoy to you {user.mention}, looking for a cat?"
    else:
        print(f"{user.name} is a bot!!!")
        msg = f"Hissss ... {user.name} is a bot!"
    embed = discord.Embed(title=random_text_face(), description=msg, color=embedColor)
    print(embed)
    await channel.send(embed=embed)

# =======================================================
# This doesn't work yet
# @client.event
async def on_member_join(member):
    dt_string = get_date()
    embedColor = 0x4c8cd6
    print(f"Greeting new arrival {member.name} as at {dt_string}")
    msg=''
    if not member.user.bot:
        msg = f"Ahoy to you {member.user.mention}, looking for a cat?"
    else:
        print(f"{member.user.name} is a bot!!!")
        msg = f"Hissss ... {member.user.name} is a bot!"
    embed = discord.Embed(title=random_text_face(), description=msg, color=embedColor)
    print(embed)
    msgChannel = member.channel
    await msgChannel.send(embed=embed)
    
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
    conn = sqlite3.connect(dbPath)
    cursor = conn.cursor()
    cursor.execute(sql)
    conn.commit()
    conn.close()

# -------------------------------------------------------
def query_sql(sql):
    conn = sqlite3.connect(dbPath)
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()
    cursor.execute(sql)
    result = [dict(row) for row in cursor.fetchall()]
    conn.close()
    return result

# -------------------------------------------------------
def add_owner(name):
    dt_string = get_date()
    stmt = f"INSERT INTO cat_owners (join_date, owner_id) VALUES ('{dt_string}','{name}');"
    exec_sql(stmt)

# -------------------------------------------------------
def remove_owner(name):
    stmt = f"DELETE FROM cat_owners WHERE owner_id = '{name}';"
    exec_sql(stmt)

# -------------------------------------------------------
def get_owner(name):
    stmt = f"SELECT * FROM cat_owners WHERE owner_id = '{name}';"
    result = query_sql(stmt)
    dt_string = get_date()
    print(f"{dt_string} Result:\n{result}")
    return result

# -------------------------------------------------------
def add_coin(name):
  stmt = f"UPDATE cat_owners SET coins=coins+1, last_daily='{get_date()}' WHERE owner_id='{name}'"
  exec_sql(stmt)

# -------------------------------------------------------
def get_coins(name):
  stmt = f"SELECT coins FROM cat_owners WHERE owner_id='{name}';"
  result = query_sql(stmt)
  return result[0].get('coins')
  
# =======================================================
# Set up and run the bot

textFaces = load_text_faces()

token = os.getenv('DISCORD_TOKEN')

client.run(token)
# =======================================================

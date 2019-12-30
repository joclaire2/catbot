# catbot runner
# Boot
bot_version = '0.3.2'

# from async import async
from datetime import datetime
from datetime import timedelta
import time
# from keep_alive import keep_alive

print('------')
dt_string = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
print("{} Bootup catbot version {}".format(dt_string,bot_version))
# =======================================================
# Load Discord Library
import discord
from discord.ext import commands
from discord import Client
from discord import TextChannel

# =======================================================
# Load libraries and global parameters
import os
import threading
import random
from random import randrange
import string
import sqlite3
from dotenv import load_dotenv
load_dotenv('../.secure/.env')
dbPath = '../sqlite/catbot.db'
catbotChannel = None
random.seed()

# =======================================================
# Build Discord Client
client: Client = discord.Client()

# -------------------------------------------------------
def get_date_str():
	return datetime.now().strftime("%Y-%m-%d")

# -------------------------------------------------------
def get_datetime_str():
	return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

# -------------------------------------------------------
def get_date():
	return datetime.strptime(get_date_str(), '%Y-%m-%d')

# -------------------------------------------------------
def get_datetime():
	return datetime.strptime(get_datetime_str(), '%Y-%m-%d %H:%M:%S')

# =======================================================

async def on_ready_body():
	catbotChannel: TextChannel = await client.fetch_channel('622421258986061837')   # catbot-testing = 622421258986061837
	print("{} - Prowling on {}".format(dt_string, catbotChannel))
	while True:
		print("Prowling channel: {}".format(catbotChannel))
		msg = "Purrrrrrrr"
		if catbotChannel is not None:
			embedColor = 0x4c8cd6
			embed = discord.Embed(title=random_text_face(), description=msg, color=embedColor)
			await catbotChannel.send(embed=embed)
			time.sleep(randrange(5, 20))

@client.event
async def on_ready():
	dt_string = get_datetime_str()
	print("{} - Logged in as name: {}".format(dt_string, client.user.name, client.user.id))
	print('------')
	#thread1: Thread = threading.Thread(target = prowl, args = (client,))
	#thread1.start()
	await on_ready_body()
	
# =======================================================
@client.event
async def on_message(message):
	dt_string = get_datetime_str()
	msgAuthor = message.author
	# we do not want the bot to reply to itself
	if msgAuthor == client.user:
		return
		
	# setup shared common settings
	msgText = message.content.lower()
	msgrName = msgAuthor.name
	msgChannel = message.channel
	embedColor = 0x4c8cd6
	catbotChannel = msgChannel
	
	print ("Channel = {}".format(msgChannel))

# -------------------------------------------------------
	if (msgText in ['c.?','c.info','c.botinfo']):
		print("{} - Telling {} info about catbot".format(dt_string,msgrName))
		embed = discord.Embed(title=random_text_face(), description="catbot is a basic bot with cute mini games where you can collect cats", color=embedColor)
		embed.add_field(name="Version", value=bot_version)
		embed.add_field(name="Authors", value="@joclaire2#5534 (bot design), @ribman#7979 (bot coding) and @hananananah#7858 (illustrations)")
		embed.add_field(name="Invite link", value="[Click here to invite catbot to your server!](<https://discordapp.com/api/oauth2/authorize?client_id=625644432741629992&permissions=388160&scope=bot>)")
		embed.add_field(name="Official catbot support server", value="[Click here to join our server!](<https://discord.gg/G6A4VEa>)")
		await msgChannel.send(embed=embed)

# -------------------------------------------------------
	elif (msgText in ['c.!','hello','hey','hi']):
		print("{} - Saying hi to {}".format(dt_string,msgrName))
		msg = "Hello! {}".format(msgAuthor.mention)
		embed = discord.Embed(title=random_text_face(), description=msg, color=embedColor)
		await msgChannel.send(embed=embed)

# -------------------------------------------------------
	elif (msgText in ['c.*','c.pic','c.picture']):
		print("{} - Sending {} a cat pic".format(dt_string,msgrName))
		embed = discord.Embed(title=random_text_face(), description="Here is a cute cat for you~!", color=embedColor)
		seed = ''.join(random.choice(string.ascii_lowercase) for x in range(10))
		catPicUrl = "https://source.unsplash.com/random/?cat&{}".format(seed)
		print("{} - catPicUrl".format(dt_string))
		embed.set_image(url=catPicUrl)
		embed.add_field(name="Credit", value="Photos from [Unsplash](<https://unsplash.com/>)")
		await msgChannel.send(embed=embed)

# -------------------------------------------------------
	elif (msgText in ['c.+','c.join']):
		print("{} - Getting member data for {}".format(dt_string,msgrName))
		result = get_owner(msgrName)
		if len(result) > 0:
			print("{} - {} asked to join but they are already in the db".format(dt_string,msgrName))
			msg = "You're already a member!  You joined on {}".format(result[0]['join_date'])
		else:
			print("{} - Adding {} to db".format(dt_string,msgrName))
			msg = "Welcome to Cat heaven!  Try c."
			add_owner(msgrName)
		embed = discord.Embed(title=random_text_face(), description=msg, color=embedColor)
		await msgChannel.send(embed=embed)

# -------------------------------------------------------
	elif (msgText in ['c.-','c.unjoin']):
		
		print("{} - Getting member data for {}".format(dt_string,msgrName))
		result = get_owner(msgrName)
		if len(result) > 0:
			print("{} - Removing {} from db".format(dt_string,msgrName))
			msg = "Ending {}'s cat ownership".format(msgAuthor.mention)
			embed = discord.Embed(title=random_text_face(), description=msg, color=embedColor)
			embed.add_field(name="You're giving up being a cat owner!", value="Waaaah  :( ")
			remove_owner(msgrName)
		else:
			print("{} - {} asked to unjoin but they aren't in the db".format(dt_string,msgrName))
			msg = "You're not a member!  Try 'c.join'."
			embed = discord.Embed(title=random_text_face(), description=msg, color=embedColor)
			
		await msgChannel.send(embed=embed)

# -------------------------------------------------------
	elif (msgText in ['c.??','c.member']):
		print("{} - Getting member data for {}".format(dt_string,msgrName))
		result = get_owner(msgrName)
		msg = "Membership info for {}".format(msgAuthor.mention)
		embed = discord.Embed(title=random_text_face(), description=msg, color=embedColor)
		if len(result) > 0:
			embed.add_field(name="Date joined", value=result[0]['join_date'])
		else:
			embed.add_field(name="You're not a cat owner!", value="tut, tut")
		await msgChannel.send(embed=embed)
		print("{} Result:\n{}".format(dt_string,result))

# -------------------------------------------------------
	elif (msgText in ['c.$+','c.daily']):
		print("{} - {} is asking for their daily coin".format(dt_string,msgrName))
		now_dttm = get_datetime()
		print("now_dttm = {}".format(now_dttm))
		now_dt = get_date()
		print("now_dt = {}".format(now_dt))
		result = get_owner(msgrName)
		last_daily = result[0].get('last_daily')
		print("last_daily = {}".format(last_daily))
		last_dttm = datetime.strptime(last_daily, '%Y-%m-%d %H:%M:%S')
		print("last_dttm = {}".format(last_dttm))
		last_dt = datetime.strptime(last_daily, '%Y-%m-%d %H:%M:%S').replace(hour = 0, minute = 0, second = 0, microsecond = 0)
		print("last_dt = {}".format(last_dt))
		diff_datetimes = (now_dttm - last_dttm)
		print("diff_datetimes = {}".format(diff_datetimes))
		diff_dates = (now_dt - last_dt).days
		print("diff_dates = {}".format(diff_dates))
		msg = "Hey, {}, I last gave you a coin at {} GMT and it's now {} GMT, that's {} timey-things ago. ".format(msgAuthor.mention,last_dttm,now_dttm,diff_datetimes)
		
		if diff_dates > 0:
			msg += "Let's give you another one! "
			add_coin(msgrName)
			new_coins = get_coins(msgrName)
			msg += "Now you have {} coins.".format(new_coins)
		else:
			coins = get_coins(msgrName)
			msg += "You already have {} coins. Come back tomorrow (GMT time) and I'll give you another one.".format(coins)
		  
		embed = discord.Embed(title=random_text_face(), description=msg, color=embedColor)
		await msgChannel.send(embed=embed)

# -------------------------------------------------------
	elif (msgText in ['c.$','c.bal','c.balance','c.biscuits','c.money','c.cash','c.coins']):
		print("{} - Getting coins for {}".format(dt_string,msgrName))
		coins = get_coins(msgrName)
		msg = "You have {} coins.  Cool!".format(coins)
		embed = discord.Embed(title=random_text_face(), description=msg, color=embedColor)
		await msgChannel.send(embed=embed)

# -------------------------------------------------------
	elif (msgText in ['c.~','c.prowl']):
		print("{} - prowl requested by {}".format(dt_string,msgrName))
		prowl(client)

# -------------------------------------------------------
	elif (msgText in ['c.#','c.kaput']):
		print("{} - exit requested by {}".format(dt_string,msgrName))
		
		if msgrName == "ribman":
			msg = "Bye!"
			embed = discord.Embed(title=random_text_face(), description=msg, color=embedColor)
			await msgChannel.send(embed=embed)
			await client.logout()
		else:
			msg = "No!"
			embed = discord.Embed(title=random_text_face(), description=msg, color=embedColor)
			await msgChannel.send(embed=embed)
			

# =======================================================
# This doesn't work yet
@client.event
async def on_voice_state_update(member, before, after):
	print ("{} - on_voice_state_update({},{},{})".format(dt_string,member.name,before,after))
	await channel.send(msg='on_voice_state_update')

# =======================================================
# This doesn't work yet
@client.event
async def on_group_join(channel, user):
	print ("{} - on_group_join({},{})".format(dt_string,channel.name,user.name))
	await channel.send(msg='on_group_join')

async def nothing1():
	dt_string = get_datetime_str()
	embedColor = 0x4c8cd6
	print("{} - Greeting new arrival {} as at {} on {}".format(dt_string,user.name,dt_string,channel))
	msg=''
	if not user.bot:
		msg = "Ahoy to you {user.mention}, looking for a cat?".format()
	else:
		print("{} is a bot!!!").format(user.name)
		msg = "Hissss ... {} is a bot!".format(user.name)
	embed = discord.Embed(title=random_text_face(), description=msg, color=embedColor)
	await channel.send(embed=embed)

# =======================================================
# This doesn't work yet
@client.event
async def on_member_join(member):
	print ("{} - on_member_join({})".format(dt_string,member.name))
	await channel.send(msg='on_member_join')

async def nothing2():
	dt_string = get_datetime_str()
	embedColor = 0x4c8cd6
	print("{} - Greeting new arrival {} as at {}".format(dt_string,member.name,dt_string))
	msg=''
	if not member.user.bot:
		msg = "Ahoy to you {}, looking for a cat?".format(member.user.mention)
	else:
		print("{} is a bot!!!").format(member.user.name)
		msg = "Hissss ... {} is a bot!".format(member.user.name)
	embed = discord.Embed(title=random_text_face(), description=msg, color=embedColor)
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
	conn = sqlite3.connect(dbPath, isolation_level=None)
	cursor = conn.cursor()
	cursor.execute(sql)
	conn.commit()
	conn.close()

# -------------------------------------------------------
def query_sql(sql):
	conn = sqlite3.connect(dbPath, isolation_level=None)
	conn.row_factory = sqlite3.Row
	cursor = conn.cursor()
	cursor.execute(sql)
	result = [dict(row) for row in cursor.fetchall()]
	conn.close()
	return result

# -------------------------------------------------------
def add_owner(name):
	dt_string = get_datetime_str()
	stmt = "INSERT INTO cat_owners (join_date, owner_id, coins, last_daily) VALUES ('{}','{}',1,'{}');".format(dt_string,name,dt_string)
	exec_sql(stmt)

# -------------------------------------------------------
def remove_owner(name):
	stmt = "DELETE FROM cat_owners WHERE owner_id = '{}';".format(name)
	exec_sql(stmt)

# -------------------------------------------------------
def get_owner(name):
	stmt = "SELECT * FROM cat_owners WHERE owner_id = '{}';".format(name)
	return query_sql(stmt)

# -------------------------------------------------------
def add_coin(name):
	dt_string = get_datetime_str()
	stmt = "UPDATE cat_owners SET coins=coins+1, last_daily='{}' WHERE owner_id='{}'".format(dt_string,name)
	exec_sql(stmt)

# -------------------------------------------------------
def get_coins(name):
	stmt = "SELECT coins FROM cat_owners WHERE owner_id='{}';".format(name)
	result = query_sql(stmt)
	return result[0].get('coins')

# =======================================================
#  Dev Zone
# =======================================================
async def prowl(theClient):
	catbotChannel: TextChannel = await theClient.fetch_channel('622421258986061837')   # catbot-testing = 622421258986061837
	print("{} - Prowling on {}".format(dt_string, catbotChannel))
	cont = True
	count = 0
	while cont:
		print("Cont: {} count: {} channel: {}".format(cont, count, catbotChannel))
		count = count + 1
		msg = "Purrrrrrrr"
		print(msg)
		if catbotChannel is not None:
			print ('mew')
			embedColor = 0x4c8cd6
			embed = discord.Embed(title=random_text_face(), description=msg, color=embedColor)
			await catbotChannel.send(embed=embed)
		time.sleep(3)
		if count >= 3:
			cont = False 

# =======================================================
# Set up and run the bot
textFaces = load_text_faces()
token = os.getenv('DISCORD_TOKEN')

# keep_alive()
#await client.connect()
#await client.login(token=token, bot=True)

#thread1 = threading.Thread(target = prowl, args = (client))
#thread1.start()

client.run(token)

# =======================================================

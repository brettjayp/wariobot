import discord
import logging
import logging.handlers
import os
import subprocess

from dotenv import load_dotenv


# get secrets
load_dotenv()
botToken = os.getenv('botToken')
broadcast = int(os.getenv('broadcastChannel'))
windrose = rf'{os.getenv('windroseServerExe')}'


# discord.py setup stuff
intents = discord.Intents.default()
intents.message_content = True

logger = logging.getLogger('discord')
logger.setLevel(logging.DEBUG)

handler = logging.handlers.RotatingFileHandler(
	filename = './logging/discord.log',
	encoding = 'utf-8',
	maxBytes = 32 * 1024 * 1024, # 32 MiB
	backupCount = 5
)
dt_fmt = '%Y-%m-%d %H:%M:%S'
formatter = logging.Formatter('[{asctime}] [{levelname:<8}] {name}: {message}', dt_fmt, style='{')
handler.setFormatter(formatter)
logger.addHandler(handler)

# TODO: Migrate from discord.Client to discord.Bot
client = discord.Client(intents=intents)


# subprocess helper
# TODO: switch case, check system for existing process, open process outside of python task tree
windrosePID = int(0)
def pWindrose(command):
	global windrosePID
	if command == 'up':
		global procWindrose
		procWindrose = subprocess.Popen([windrose], creationflags=subprocess.DETACHED_PROCESS)
		windrosePID = int(procWindrose.pid)
		return windrosePID

	if command == 'down':
		if procWindrose:
			procWindrose.terminate()
			windrosePID = 0
		return windrosePID

	if command == 'status':
		return windrosePID


# listener
@client.event
async def on_ready():
	print(f'Bot logged in as {client.user}')

	channel = client.get_channel(broadcast)
	if channel:
		await channel.send('`wariobot` is online.\nPrefix all commands with `!`. wr = windrose\nCurrent commands are: `!hello`, `!wr status`, `!wr up`, `!wr down`')
	else:
		print('Channel not found.')


# TODO: After migration to discord.Bot, ditch message based commands for slash commands. After, see if we can reduce required intents.
@client.event
async def on_message(message):
	status = pWindrose('status')

	if message.author == client.user:
		return

	if message.content.startswith('!hello'):
		await message.channel.send(f'Yo what up, {message.author}?')

	if message.content.startswith('!wr status'):
		if status == 0:
			await message.channel.send('A Windrose dedotated server is not currently detected.')
		else:
			await message.channel.send(f'A Windrose dedotated server is detected with PID: {status}')

	if message.content.startswith('!wr up'):
		if status == 0:
			pWindrose('up')
			status = pWindrose('status')
			await message.channel.send(f'Starting the Windrose dedotated server. Process started with PID: {status}')
		else:
			await message.channel.send(f'A Windrose dedotated server is already running with PID: {status}')

	if message.content.startswith('!wr down'):
		if status != 0:
			pWindrose('down')
			await message.channel.send(f'Shutting down the Windrose dedotated server at PID: {status}')
			status = pWindrose('status')
		else:
			await message.channel.send('No Windrose dedotated server was detected.')


client.run(botToken, log_handler=None)

# Meme credit to Superkai64 and ZodiaxEU. https://knowyourmeme.com/memes/dedotated-wam

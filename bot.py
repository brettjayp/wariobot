import discord
import subprocess
import os

from dotenv import load_dotenv

# get secrets
load_dotenv()
botToken = os.getenv('botToken')
broadcast = os.getenv('broadcastChannel')
windrose = os.getenv('windroseServerExe')

# discord.py setup stuff
intents = discord.Intents.default()
intents.message_content = True
intents.members = True

client = discord.Client(intents=intents)

# listener
@client.event
async def on_ready():
	print(f'Bot logged in as {client.user}')

	channel = client.get_channel(broadcast)
	if channel:
		await channel.send('`wariobot` is online.\n\nPrefix all commands with `!`.\nCurrent commands are: `hello`, `windrose up`, `windrose down`')
	else:
		print('Channel not found.')


@client.event
async def on_message(message):
	if message.author == client.user:
		return

	if message.content.startswith('!hello'):
		await message.channel.send(f'Yo what up, {message.author}?')

	if message.content.startswith('!windrose up'):
		pWindrose = subprocess.Popen([windrose])
		await message.channel.send('Starting Windrose Dedotated Server.')

	if message.content.startswith('!windrose down'):
		pWindrose.terminate()
		await.message.channel.send('Ending Windrose Dedotated Server.')

client.run(botToken)


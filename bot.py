import discord
import os

from dotenv import load_dotenv

load_dotenv()
botToken = os.getenv("botToken")

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
	print(f'Bot logged in as {client.user}')

@client.event
async def on_message(message):
	if message.author == client.user:
		return

	if message.content.startswith('$windrose up'):
		await message.channel.send('Starting Windrose Dedotated Server.')

client.run(botToken)

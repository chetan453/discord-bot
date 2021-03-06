import discord
import os
client=discord.Client()

@client.event
async def on_ready():
  print('the bot is ready in the server \n{0.user}'.format(client))

@client.event
async def on_message(msg):
  if msg.author==client.user:
    return
  
  if msg.content.startswith("$hello"):
   await msg.channel.send("hii budy")


client.run(os.getenv('TOKEN'))
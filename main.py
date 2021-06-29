import discord
import os
import requests
import json
from random import randint

client= discord.Client()

with open('data.json', encoding='utf-8-sig') as data_file:
    data = json.load(data_file)
JOKE_COUNT = len(data)

def get_joke():
    # Return random joke
    random_num = randint(1, JOKE_COUNT)
    joke = data[random_num]
    lmao=joke.replace('\"', "'")
    if "Chuck" in lmao:
      lmao1=lmao.replace("Chuck","Sheldon")

      if "Norris" in lmao1:
        lmao2=lmao1.replace("Norris","Cooper")
        lmao=lmao2
        return lmao
    return lmao

@client.event
async def on_ready():
  print("We have logged in as {0.user}".format(client))

@client.event
async def on_message(message):
  if message.author==client.user:
    return
  if message.content.startswith("!crazy"):
    await message.channel.send("Hey! I'm Not Crazy. My Mother Had Me Tested.")

  if message.content.startswith("!joke"):
    jokes=get_joke()
    await message.channel.send(jokes+"🖖")

client.run(os.environ['token'])
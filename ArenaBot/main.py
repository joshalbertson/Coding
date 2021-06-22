#Arena Discord Bot

import discord
import os
import json
import random

token = os.environ['DISCORD-API-TOKEN']
client = discord.Client()

with open('rewards.json', 'r') as read_file:
        rewards = json.load(read_file)
with open('2v2.json', errors='ignore') as read_file:
        twos = json.load(read_file)
with open('3v3.json', errors='ignore') as read_file:
        threes = json.load(read_file)
with open('5v5.json', errors='ignore') as read_file:
        fives = json.load(read_file)

def cutoff(bracket):

  if bracket in ['2', '2v2', '2s', 'twos']:
    rank1 = 'Infernal Gladiator: ' + str(rewards['rewards'][0]['rating_cutoff']) + '\n'
    gladiator = 'Gladiator: ' + str(rewards['rewards'][1]['rating_cutoff']) + '\n'
    duelist = 'Duelist: ' + str(rewards['rewards'][2]['rating_cutoff']) + '\n'
    rival = 'Rival: ' + str(rewards['rewards'][3]['rating_cutoff']) + '\n'
    challenger = 'Challenger: ' + str(rewards['rewards'][4]['rating_cutoff'])
    cutoffs  = '2v2 Cutoffs:' + '\n' + rank1 + gladiator + duelist + rival + challenger
    return cutoffs

  if bracket in ['3', '3v3', '3s', 'threes']:
    rank1 = 'Infernal Gladiator: ' + str(rewards['rewards'][5]['rating_cutoff']) + '\n'
    gladiator = 'Gladiator: ' + str(rewards['rewards'][6]['rating_cutoff']) + '\n'
    duelist = 'Duelist: ' + str(rewards['rewards'][7]['rating_cutoff']) + '\n'
    rival = 'Rival: ' + str(rewards['rewards'][8]['rating_cutoff']) + '\n'
    challenger = 'Challenger: ' + str(rewards['rewards'][9]['rating_cutoff'])
    cutoffs  = '3v3 Cutoffs:' + '\n' + rank1 + gladiator + duelist + rival + challenger
    return cutoffs

  if bracket in ['5', '5v5', '5s', 'fives']:
    rank1 = 'Infernal Gladiator: ' + str(rewards['rewards'][10]['rating_cutoff']) + '\n'
    gladiator = 'Gladiator: ' + str(rewards['rewards'][11]['rating_cutoff']) + '\n'
    duelist = 'Duelist: ' + str(rewards['rewards'][12]['rating_cutoff']) + '\n'
    rival = 'Rival: ' + str(rewards['rewards'][13]['rating_cutoff']) + '\n'
    challenger = 'Challenger: ' + str(rewards['rewards'][14]['rating_cutoff'])
    cutoffs  = '5v5 Cutoffs:' + '\n' + rank1 + gladiator + duelist + rival + challenger
    return cutoffs
  else:
    cutoffs = 'Enter a bracket, for example: !cutoff 2'
    return cutoffs

def top(bracket):
  top = ''
  if bracket in ['2', '2v2', '2s', 'twos']:
    for i in range(0,10):
      top = top + '\n' + str(i+1) + ' - ' + str(twos['entries'][i]['team']['name']) + ' : ' + str(twos['entries'][i]['rating'])
    return 'Top 10 2v2 Teams: ' + top
  if bracket in ['3', '3v3', '3s', 'threes']:
    for i in range(0,10):
      top = top + '\n' + str(i+1) + ' - ' + str(threes['entries'][i]['team']['name']) + ' : ' + str(threes['entries'][i]['rating'])
    return 'Top 10 3v3 Teams: ' + top
  if bracket in ['5', '5v5', '5s', 'fives']:
    for i in range(0,10):
      top = top + '\n' + str(i+1) + ' - ' + str(fives['entries'][i]['team']['name']) + ' : ' + str(fives['entries'][i]['rating'])
    return 'Top 10 5v5 Teams: ' + top
  else:
    return top

def teams(player):
  twosteam = 'No 2v2 Team Found for ' + player
  threesteam = 'No 3v3 Team Found for ' + player
  fivesteam = 'No 5v5 Team Found for ' + player
  for x in range(len(twos['entries'])):
      if 'members' not in twos['entries'][x]['team']:
          continue
      for y in range(len(twos['entries'][x]['team']['members'])):
          if twos['entries'][x]['team']['members'][y]['character']['name'] == player:
            twosteam = str(twos['entries'][x]['team']['name']) + ' - ' + str(twos['entries'][x]['rating'])

  for x in range(len(threes['entries'])):
      if 'members' not in twos['entries'][x]['team']:
          continue
      for y in range(len(threes['entries'][x]['team']['members'])):
        if threes['entries'][x]['team']['members'][y]['character']['name'] == player:
            threesteam = str(threes['entries'][x]['team']['name']) + ' - ' + str(threes['entries'][x]['rating'])

  for x in range(len(fives['entries'])):
      if 'members' not in twos['entries'][x]['team']:
          continue
      for y in range(len(fives['entries'][x]['team']['members'])):
        if fives['entries'][x]['team']['members'][y]['character']['name'] == player:
            fivesteam = str(fives['entries'][x]['team']['name']) + ' - ' + str(fives['entries'][x]['rating'])

  return player + '\'s teams:' + '\n' + twosteam + '\n' + threesteam + '\n' + fivesteam

def title(player):
  #find ratings
  return 'NYI'

def roll(rollrange):
  rollrange = int(rollrange)
  if rollrange is not None:
    return random.randint(1, rollrange)
  else:
    return random.randint(1, 100)

def eightball():
  number = random.randint(1, 20)
  if number == 1:
    return 'It is certain.'
  if number == 2:
    return 'It is decidedly so.'
  if number == 3:
    return 'Without a doubt.'
  if number == 4:
    return 'Yes definitely.'
  if number == 5:
    return 'You may rely on it.'
  if number == 6:
    return 'As I see it, yes.'
  if number == 7:
    return 'Most likely.'
  if number == 8:
    return 'Outlook good.'
  if number == 9:
    return 'Yes.'
  if number == 10:
    return 'Signs point to yes.'
  if number == 11:
    return 'Reply hazy, try again.'
  if number == 12:
    return 'Ask again later.'
  if number == 13:
    return 'Better not tell you now.'
  if number == 14:
    return 'Cannot predict now.'
  if number == 15:
    return 'Concentrate and ask again.'
  if number == 16:
    return 'Don\'t count on it.'
  if number == 17:
    return 'My reply is no.'
  if number == 18:
    return 'My sources say no.'
  if number == 19:
    return 'Outlook not so good.'
  if number == 20:
    return 'Very doubtful.'

@client.event
async def on_ready():
    print('Logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    msg = message.content

    if msg.startswith('!cutoff'):
        bracket = msg.split("!cutoff ",1)[1]
        await message.channel.send(cutoff(bracket))

    if msg.startswith('!top'):
      bracket = msg.split('!top ',1)[1]
      await message.channel.send(top(bracket))
    
    if msg.startswith('!teams'):
      player = msg.split('!teams ',1)[1]
      await message.channel.send(teams(player))

    if msg.startswith('!title'):
      player = msg.split('!title ',1)[1]
      await message.channel.send(title(player))

    if msg.startswith('!vices'):
      await message.channel.send('Fuck Vices.')

    if msg.startswith('!roll'):
      try:
        rollrange = msg.split('!roll ',1)[1]
      except:
        rollrange = 100
      finally:
        await message.channel.send(roll(rollrange))
    
    if msg.startswith('!hasquinnkilledsireyet'):
      await message.channel.send('No.')
    
    if msg.startswith('!mcdonalds'):
      await message.channel.send('Just the best, honestly.')

    if msg.startswith('!8ball'):
      await message.channel.send(eightball())

client.run(os.environ['DISCORD-API-TOKEN'])

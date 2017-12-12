import discord
import asyncio
from discord.ext.commands import Bot
from discord.ext import commands
import platform
import random

client = Bot(description="Bot by Sean", command_prefix="", pm_help = True)
// This only works on my server// 
@client.event
async def on_member_join(member):
    channel = client.get_channel("385413158975832074")
    server = member.server
    fmt = 'Welcome {0.mention} to {1.name}!'
    await client.send_message(channel, fmt.format(member, server))

@client.command()
async def info(*args):
	await client.say("This is a bot created by Sean Theisen for use in discord")
	await asyncio.sleep(3)

@client.command()
async def internet(*args):
	await client.say("http://i3.kym-cdn.com/photos/images/newsfeed/000/170/791/welcome-to-the-internet-internet-demotivational-poster-1264714433.png.jpg")
	await asyncio.sleep(3)
	
@client.command()
async def commands(*args):
	await client.say("cool")
	await asyncio.sleep(3)

@client.event
async def on_message(message):
#--------------------------------------Moderation--------------------------------------------------------------------
    if message.content.startswith('heck'):
        await client.send_message(message.channel, 'no')

<<<<<<< HEAD
#-------------------------------Guessing game------------------------------------------------------------------------
=======
    if message.author == client.user:
        return
    if message.content.startswith('~ping'):
        await client.send_message(message.channel, 'pong')

    if message.content.startswith('~help'):
        await client.send_message(message.author, ' Bot by Sean, help -- shows this message, pint -- pong,')

#---------------------------------------------------------------------------------------------------------------                
    if message.content.startswith('~fake'):
            await client.send_message(message.channel, 'How many players? ')

            
            a = await client.wait_for_message(timeout=10.0, author=message.author, )
            await client.send_message(message.channel, 'success' )
            a = int(a.content)
            await client.send_message(message.channel, 'Mention all of the players in individual messages: ')
            chosen_player_index = random.randint(0, a-1)
            names = []
            for count in range(a):
                names.append(await client.wait_for_message(timeout=10.0, author=message.author))

            for name in names:
                if names.index(name) == chosen_player_index:
                    await client.send_message(name.mentions[0], 'It worked!')
                
                else:
                    await client.send_message(name.mentions[0], 'It worked!')
        
                    if message.content.startswith('~answer'):
                        fake = chosen_player_index
                        str(fake)
                        await client.send_message(message.channel, fake.content)
#-----------------------------------------------------------------------------------------------------------------
>>>>>>> 39736269a0d278d2663332772839fd3a05c28dff
    if message.content.startswith('~guess'):
        await client.send_message(message.channel, 'Guess a number between 1 to 10')

        def guess_check(m):
            return m.content.isdigit()

        guess = await client.wait_for_message(timeout=5.0, author=message.author, check=guess_check)
        answer = random.randint(1, 10)
        if guess is None:
            fmt = 'Sorry, you took too long. It was {}.'
            await client.send_message(message.channel, fmt.format(answer))
            return
        if int(guess.content) == answer:
            await client.send_message(message.channel, 'You are right!')
            
        else:
            await client.send_message(message.channel, 'Sorry. Its actually {}.'.format(answer))
#----------------------------------Random Message Commands------------------------------------------------------
    if message.author == client.user:
        return
    if message.content.startswith('~ping'):
        await client.send_message(message.channel, 'pong')
    if message.content.startswith('~help'):
        await client.send_message(message.author, ' Bot by Sean, help -- shows this message, pint -- pong,')
#-----------------------------------The Fake Game----------------------------------------------------------------                
    if message.content.startswith('~fake'):
        await client.send_message(message.channel, 'How many players? ')

        playercount = await client.wait_for_message(timeout=10.0, author=message.author, )
        await client.send_message(message.channel, 'success' )
        playercount = int(playercount.content)
        await client.send_message(message.channel, 'Mention all of the players in individual messages: ')
        chosen_player_index = random.randint(0, playercount)
        names = []

        for count in range(playercount):
            names.append(await client.wait_for_message(timeout=10.0, author=message.author)) 
      
    for name in names:
        if names.index(name) == chosen_player_index:
            await client.send_message(name.mentions[0], 'It worked!')
        else:
            await client.send_message(name.mentions[0], 'It worked!')

    await client.send_message(message.channel, "I'm out of the name loop!")

    await client.send_message(message.channel, "Answer now, when you have all answered, the host must type ~answer ")
    message = await client.wait_for_message(timeout=20.0, author=message.author)
    if message.content.startswith('~answer'):
        await client.send_message(message.channel, str(names[chosen_player_index-1].content))
    else:
        await client.send_message(message.channel, "not fixed, message didn't start with") 

#----------------------------On startup in terminal--------------------------------------------------------------------------------------------------------------------------------------
@client.event
async def on_ready():

	print('Logged in as '+client.user.name+' (ID:'+client.user.id+') | Connected to '+str(len(client.servers))+' servers | Connected to '+str(len(set(client.get_all_members())))+' users')
	print('------------------------------------------------------------------------------------------------------------------------------------------------------------------------------')
	print('Current Discord.py Version: {} | Current Python Version: {}'.format(discord.__version__, platform.python_version()))
	print('------------------------------------------------------------------------------------------------------------------------------------------------------------------------------')
	print('Use this link to invite {}:'.format(client.user.name))
	print('https://discordapp.com/oauth2/authorize?client_id={}&scope=bot&permissions=8'.format(client.user.id))
<<<<<<< HEAD
	print('------------------------------------------------------------------------------------------------------------------------------------------------------------------------------')
=======
	print('--------')




client.run('')
>>>>>>> 39736269a0d278d2663332772839fd3a05c28dff

client.run('')
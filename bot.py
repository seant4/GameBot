import discord
import asyncio
from discord.ext.commands import Bot
from discord.ext import commands
import platform
import random

client = Bot(description="Bot by Sean", command_prefix="~", pm_help = True)

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

    if message.author == client.user:
        return
    if message.content.startswith('~ping'):
        await client.send_message(message.channel, 'pong')

    if message.content.startswith('~help'):
        await client.send_message(message.author, ' Bot by Sean, help -- shows this message, pint -- pong,')

#---------------------------------------------------------------------------------------------------------------                
    if message.content.startswith('~fake'):
        await client.send_message(message.channel, 'How many players? (up to 5)')

        def players_check(m):
            return m.content.isdigit()

        players = await client.wait_for_message(timeout=10.0, author=message.author, check=players_check)
        await client.send_message(message.channel, players.content, )
        number = int(players.content)

        if number == 1:
            await client.send_message(message.channel, 'more than 1 player')

        elif number == 2:
            await client.send_message(message.channel, 'Who will be player 1?')
            player1 = await client.wait_for_message(timeout=20.0, author=message.author)
            await client.send_message(message.channel, 'Who will be player 2?')
            player2 = await client.wait_for_message(timeout=20.0, author=message.author)
            final = random.randint(1, number)
            int(final)
            if final == 1:
                await client.send_message(player1.mentions[0], 'It worked!')
                await client.send_message(player2.mentions[0], 'It worked')
                
                message = await client.wait_for_message(timeout=20.0, author=message.author)

                if message.content.startswith('~answer'):
                    await client.send_message(message.channel, player1.content)

            elif final == 2:
                await client.send_message(player1.mentions[0], 'It worked!')
                await client.send_message(player2.mentions[0], 'It worked')
                
                message = await client.wait_for_message(timeout=20.0, author=message.author)

                if message.content.startswith('~answer'):
                    await client.send_message(message.channel, player2.content)
            else:
                await client.send_message(message.channel, 'An error occured, obj_final incorrectly set')
            
        elif number == 3:
            await client.send_message(message.channel, 'Who will be player 1?')
            player1 = await client.wait_for_message(timeout=10.0, author=message.author)
            await client.send_message(message.channel, 'Who will be player 2?')
            player2 = await client.wait_for_message(timeout=10.0, author=message.author)
            await client.send_message(message.channel, 'Who will be player 3?')
            player3 = await client.wait_for_message(timeout=10.0, author=message.author)
            final = random.randint(1, number)
            int(final)
            if final == 1:
                await client.send_message(player1.mentions[0], 'It worked!')
                await client.send_message(player2.mentions[0], 'It worked!')
                await client.send_message(player3.mentions[0], 'It worked!')

            elif final == 2:
                await client.send_message(player1.mentions[0], 'It worked!')
                await client.send_message(player2.mentions[0], 'It worked!')
                await client.send_message(player3.mentions[0], 'It worked!')

            elif final == 3:
                await client.send_message(player1.mentions[0], 'It worked!')
                await client.send_message(player2.mentions[0], 'It worked!')
                await client.send_message(player3.mentions[0], 'It worked!')
            
            else :
                await client.send_message(message.channel, 'An error occured, obj_final incorrectly set')

        elif number == 4:
            await client.send_message(message.channel, 'Who will be player 1?')
            player1 = await client.wait_for_message(timeout=10.0, author=message.author)
            await client.send_message(message.channel, 'Who will be player 2?')
            player2 = await client.wait_for_message(timeout=10.0, author=message.author)
            await client.send_message(message.channel, 'Who will be player 3?')
            player3 = await client.wait_for_message(timeout=10.0, author=message.author)
            await client.send_message(message.channel, 'Who will be player 4?')
            player4 = await client.wait_for_message(timeout=10.0, author=message.author)
            final = random.randint(1, number)
            int(final)
            
            if final == 1:
                await client.send_message(player1.mentions[0], 'It worked!')
                await client.send_message(player2.mentions[0], 'It worked!')
                await client.send_message(player3.mentions[0], 'It worked!')
                await client.send_message(player4.mentions[0], 'It worked!')

            elif final == 2:
                await client.send_message(player1.mentions[0], 'It worked!')
                await client.send_message(player2.mentions[0], 'It worked!')
                await client.send_message(player3.mentions[0], 'It worked!')
                await client.send_message(player4.mentions[0], 'It worked!')

            elif final == 3:
                await client.send_message(player1.mentions[0], 'It worked!')
                await client.send_message(player2.mentions[0], 'It worked!')
                await client.send_message(player3.mentions[0], 'It worked!')
                await client.send_message(player4.mentions[0], 'It worked!')
            
            elif final == 4:
                await client.send_message(player1.mentions[0], 'It worked!')
                await client.send_message(player2.mentions[0], 'It worked!')
                await client.send_message(player3.mentions[0], 'It worked!')
                await client.send_message(player4.mentions[0], 'It worked!')
            
            else :
                await client.send_message(message.channel, 'An error occured, obj_final incorrectly set')

        
        elif number == 5:
            await client.send_message(message.channel, 'Who will be player 1?')
            player1 = await client.wait_for_message(timeout=10.0, author=message.author)
            await client.send_message(message.channel, 'Who will be player 2?')
            player2 = await client.wait_for_message(timeout=10.0, author=message.author)
            await client.send_message(message.channel, 'Who will be player 3?')
            player3 = await client.wait_for_message(timeout=10.0, author=message.author)
            await client.send_message(message.channel, 'Who will be player 4?')
            player4 = await client.wait_for_message(timeout=10.0, author=message.author)
            await client.send_message(message,channel, 'Who will be player 5?')
            player5 = await client.wait_for_message(timeout=10.0, author=message.author)
            final = random.randint(1, number)
            int(final)
            
            if final == 1:
                await client.send_message(player1.mentions[0], 'It worked!')
                await client.send_message(player2.mentions[0], 'It worked!')
                await client.send_message(player3.mentions[0], 'It worked!')
                await client.send_message(player4.mentions[0], 'It worked!')
                await client.send_message(player5.mentions[0], 'It worked!')
                fake = player1
                str (fake)
                
                if message.content.startswith('~answer'):
                    await client.send_message(message.channel, 'The fake was: ', fake.content)

                

            elif final == 2:
                await client.send_message(player1.mentions[0], 'It worked!')
                await client.send_message(player2.mentions[0], 'It worked!')
                await client.send_message(player3.mentions[0], 'It worked!')
                await client.send_message(player4.mentions[0], 'It worked!')
                await client.send_message(player5.mentions[0], 'It worked!')
                fake = player2
                str (fake)

                if message.content.startswith('~answer'):
                    await client.send_message(message.channel, 'The fake was: ', fake.content)

                else :
                    await client.send_message(message.channel, 'The fake was: ', fake.content)

            elif final == 3:
                await client.send_message(player1.mentions[0], 'It worked!')
                await client.send_message(player2.mentions[0], 'It worked!')
                await client.send_message(player3.mentions[0], 'It worked!')
                await client.send_message(player4.mentions[0], 'It worked!')
                await client.send_message(player5.mentions[0], 'It worked!')
                fake = player3
                str (fake)

                if message.content.startswith('~answer'):
                    await client.send_message(message.channel, 'The fake was: ', fake.content)

                else :
                    await client.send_message(message.channel, 'The fake was: ', fake.content)
            
            elif final == 4:
                await client.send_message(player1.mentions[0], 'It worked!')
                await client.send_message(player2.mentions[0], 'It worked!')
                await client.send_message(player3.mentions[0], 'It worked!')
                await client.send_message(player4.mentions[0], 'It worked!')
                await client.send_message(player5.mentions[0], 'It worked!')
                fake = player4
                str (fake)

                if message.content.startswith('~answer'):
                    await client.send_message(message.channel, 'The fake was: ', fake.content)

                else :
                    await client.send_message(message.channel, 'The fake was: ', fake.content)

            elif final == 5:
                await client.send_message(player1.mentions[0], 'It worked!')
                await client.send_message(player2.mentions[0], 'It worked!')
                await client.send_message(player3.mentions[0], 'It worked!')
                await client.send_message(player4.mentions[0], 'It worked!')
                await client.send_message(player5.mentions[0], 'It worked!')
                fake = player5
                str (fake)

                if message.content.startswith('~answer'):
                    await client.send_message(message.channel, 'The fake was: ', fake.content)

                else :
                    await client.send_message(message.channel, 'The fake was: ', fake.content)
            
            else :
                await client.send_message(message.channel, 'An error occured, obj_final incorrectly set')
         
#-----------------------------------------------------------------------------------------------------------------
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
#--------------------------------------------------------------------------------------------------------------------
@client.event
async def on_ready():

	print('Logged in as '+client.user.name+' (ID:'+client.user.id+') | Connected to '+str(len(client.servers))+' servers | Connected to '+str(len(set(client.get_all_members())))+' users')
	print('--------')
	print('Current Discord.py Version: {} | Current Python Version: {}'.format(discord.__version__, platform.python_version()))
	print('--------')
	print('Use this link to invite {}:'.format(client.user.name))
	print('https://discordapp.com/oauth2/authorize?client_id={}&scope=bot&permissions=8'.format(client.user.id))
	print('--------')




client.run('Mzg0ODQ4MDYxNTkzMTU3NjM0.DP4yBg.X8YYVQTlK-5TI5BDdP0pTUnPDXo')


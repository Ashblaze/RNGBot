# bot.py
import os
import sys
import random

import discord
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

bot = commands.Bot(command_prefix='!')
bot.remove_command('help')

message_number = {}

@bot.command(name = 'help')
async def help(ctx):
    embed = discord.Embed(
        colour = discord.Colour.green())
    embed.set_author(name='Help : list of commands available')
    embed.add_field(name='!roll', value='Print a random number. Default start is 1, end is 10', inline=False)
    embed.add_field(name='Git Link', value='https://github.com/Ashblaze/RNGBot')
    await ctx.send(embed=embed)
    #await ctx.send('This is a test.')


@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected to Discord!')


@bot.command(name='roll', help='Roll a random number.')
async def roll(ctx, start = 1, end = 10):
    if start > end:
        start, end = end, start
    
    random_number = random.randint(int(start), int(end))

    await ctx.send(random_number)


@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.errors.BadArgument):
        await ctx.send('Usage: !roll [start<int>(1)] [end<int>(10)]' \
            ' or !roll [end<int>(10)] [start<int>(1)]')


@bot.event
async def on_message(ctx):
    await bot.process_commands(ctx)
    if ctx.author == bot.user or ctx.content.startswith('!'):
        return
    #emoji = '\N{EYES}'
    #await ctx.add_reaction(emoji)
    user_name = ctx.author.name

    if user_name not in message_number:
        message_number[user_name] = 0

    if message_number[user_name] < 10:
        message_number[user_name] += 1
    elif message_number[user_name] == 10:
        message_number[user_name] = 0

    if message_number[user_name] == 1:
        response = get_response(ctx)
        if response:
            await ctx.channel.send(response)
    await bot.process_commands(ctx)


def get_response(ctx):
    user_name = ctx.author.name
    if user_name == 'akshayd31':
        return('%s, yy chikna' % ctx.author.mention)
    elif user_name == 'mintuj':
        return('%s bol raha hai' % ctx.author.mention)
    elif user_name == 'Ashblaze':
        return('%s, yo.' % ctx.author.mention)
    elif user_name == 'Kevin Abraham':
        return('%s, nya nya!' % ctx.author.mention)
    elif user_name == 'kuro':
        return('Hands up, %s!' % ctx.author.mention)
    elif user_name == 'Übermensch':
        return('%s, U?' % ctx.author.mention)
    elif user_name == 'rishirajatroy':
        return('%s, U?' % ctx.author.mention)
    elif user_name == 'DjentleMonK':
        return('Yes, %s, I recommend you get rid of RhythmBot.' % ctx.author.mention)
    elif user_name == 'jakrukuttan':
        return('%s, I recommend you cease your extrapolation.' % ctx.author.mention)
    elif user_name == 'naveenjohn94':
        return('%s, 🙌' % ctx.author.mention)
    elif user_name == 'seldombark':
        return('%s, the fat one sends his regards.' % ctx.author.mention)
    elif user_name == 'pøgbaJr':
        return('%s, I can verify no bananas were stolen.' % ctx.author.mention)
    elif user_name == 'areafunds20':
        return('Well, well... If it ain\'t Fabulous Fuf, %s.' % ctx.author.mention)
    elif user_name == 'mukund':
        return('RAAAAAAAUUUUUUUUULLL!!! %s.' % ctx.author.mention)
    else:
        return ''


bot.run(TOKEN)

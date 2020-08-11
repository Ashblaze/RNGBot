# bot.py
import os
import sys
import random

import discord
from discord.ext import commands
from dotenv import load_dotenv
from responses import response_dict

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
async def roll(ctx, *args):
    try:
        if len(args) == 0:
            start, end = 0, 10
        elif len(args) == 1:
            if int(args[0]) < 0:
                start, end = int(args[0]), 0
            else:
                start, end = 0, int(args[0])
        elif len(args) == 2:
            if int(args[0]) < int(args[1]):
                start, end = int(args[0]), int(args[1])
            else:
                start, end = int(args[1]), int(args[0])
        else:
            await ctx.send('Usage: !roll [start] [end]' \
                ' or !roll [end] [start]')
            return
        
        random_number = random.randint(start, end)

        await ctx.send(random_number)
    except (TypeError, UnboundLocalError, ValueError):
        await ctx.send('Only integers allowed!')


@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.errors.BadArgument):
        await ctx.send('Bad arguments!')
    elif isinstance(error, commands.errors.CommandInvokeError):
        await ctx.send('Oops, something went wrong with the command!')


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

    if message_number[user_name] == 5:
        response = get_response(ctx)
        if response:
            await ctx.channel.send(response)
    await bot.process_commands(ctx)


def get_response(ctx):
    user_name = ctx.author.name
    if response_dict.get(user_name):
        response = random.choice(response_dict[user_name])
        return(' '.join(['%s' % ctx.author.mention, response]))
    else:
        return ''


bot.run(TOKEN)

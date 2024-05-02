import discord
from discord.ext import commands
import asyncio

bot = commands.Bot(command_prefix="!", intents=discord.Intents.all())

nuke_loop = False
sound_loop = False
gif_loop = False
mention_loop = False
rickroll_loop = False

async def nuke_message(ctx, message):
    count = 0
    while nuke_loop:
        if count < 5:
            await ctx.send(message)
            count += 1
        else:
            count = 0
            await asyncio.sleep(1)

@bot.command()
async def nuke(ctx, *, message):
    global nuke_loop
    nuke_loop = True
    await nuke_message(ctx, message)

@bot.command()
async def stop(ctx):
    global nuke_loop, sound_loop, gif_loop, mention_loop, rickroll_loop
    nuke_loop = False
    sound_loop = False
    gif_loop = False
    mention_loop = False
    if rickroll_loop:
        rickroll_loop = False  
        await ctx.send("Rickroll stopped!")
    await ctx.send("All actions stopped!")

async def sound_loop_function(ctx):
    while sound_loop:
        await ctx.send(file=discord.File('audio.mp3'))
        await asyncio.sleep(0.5)

@bot.command()
async def sound(ctx):
    global sound_loop
    sound_loop = True
    await sound_loop_function(ctx)

@bot.command()
async def stop_sound(ctx):
    global sound_loop
    sound_loop = False
    await ctx.send("Sound loop stopped!")

async def gif_loop_function(ctx):
    while gif_loop:
        await ctx.send(file=discord.File('animated.gif'))
        await asyncio.sleep(0.5)

@bot.command()
async def gif(ctx):
    global gif_loop
    gif_loop = True
    await gif_loop_function(ctx)

@bot.command()
async def stop_gif(ctx):
    global gif_loop
    gif_loop = False
    await ctx.send("Gif loop stopped!")

async def mention_users(ctx, user):
    global mention_loop
    if user == 'everyone':
        mention = '@everyone'
    else:
        mention = user
    count = 0
    while mention_loop:
        if count < 5:
            await ctx.send(mention)
            count += 1
        else:
            count = 0

@bot.command()
async def mention(ctx, user):
    global mention_loop
    if user.lower() == 'everyone':
        mention_loop = True
        await mention_users(ctx, 'everyone')
    else:
        mention_loop = True
        await mention_users(ctx, user)

@bot.command()
async def clear(ctx):
    await ctx.channel.purge(check=lambda m: m.author == bot.user)

@bot.command()
async def rickroll(ctx):
    global rickroll_loop
    rickroll_loop = True
    while rickroll_loop:
        await ctx.send(file=discord.File('rickroll.gif'))

@bot.command()
async def stop_rickroll(ctx):
    global rickroll_loop
    if rickroll_loop:
        rickroll_loop = False
        await ctx.send("Rickroll stopped!")
    else:
        await ctx.send("Rickroll is not currently playing.")

bot.run("Bot Token")

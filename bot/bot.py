import os
import random as rd
import discord
from discord.ext import commands

TOKEN = os.getenv('DISCORD_TOKEN')
client = commands.Bot(command_prefix="^")
os.chdir("bot")
num = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
ltr = ['A', 'B', 'C', 'D', 'E', 'F']


@client.event
async def on_ready():
    print(f'{client.user.name} has connected to Discord!')


@client.event
async def on_member_join(member):
    await member.create_dm()
    await member.dm_channel.send(
        f'Hi {member.name}, welcome to my Discord server!'
    )


@client.command
async def ctime(ctx):
    await ctx.send(rd.choice(["It's ", "The current time is: ", "Here's The time: ",
                              "BING BONG BING BONG who's your friend who likes to play?  "]) + str(
        ctx.created_at) + " GMT")


@client.command
async def joke(ctx):
    j = open('./joke', 'r')
    jLines = j.readlines()
    jDat = []
    for line in jLines:
        jDat.append(line.strip().split("±"))
    joke = rd.choice(jDat)
    await ctx.send(joke[0])
    try:
        await ctx.send(joke[1])
    except discord.errors.HTTPException:
        pass


@client.command
async def genkey(ctx):
    await ctx.author.create_dm()
    key = str('Key: ||`' +
              (rd.choice(num) if bool(rd.getrandbits(1)) else rd.choice(ltr)) +
              (rd.choice(num) if bool(rd.getrandbits(1)) else rd.choice(ltr)) +
              (rd.choice(num) if bool(rd.getrandbits(1)) else rd.choice(ltr)) +
              (rd.choice(num) if bool(rd.getrandbits(1)) else rd.choice(ltr)) +
              (rd.choice(num) if bool(rd.getrandbits(1)) else rd.choice(ltr)) +
              (rd.choice(num) if bool(rd.getrandbits(1)) else rd.choice(ltr)) +
              (rd.choice(num) if bool(rd.getrandbits(1)) else rd.choice(ltr)) +
              (rd.choice(num) if bool(rd.getrandbits(1)) else rd.choice(ltr)) +
              (rd.choice(num) if bool(rd.getrandbits(1)) else rd.choice(ltr)) +
              (rd.choice(num) if bool(rd.getrandbits(1)) else rd.choice(ltr)) +
              (rd.choice(num) if bool(rd.getrandbits(1)) else rd.choice(ltr)) +
              (rd.choice(num) if bool(rd.getrandbits(1)) else rd.choice(ltr)) +
              (rd.choice(num) if bool(rd.getrandbits(1)) else rd.choice(ltr)) +
              (rd.choice(num) if bool(rd.getrandbits(1)) else rd.choice(ltr)) +
              (rd.choice(num) if bool(rd.getrandbits(1)) else rd.choice(ltr)) +
              (rd.choice(num) if bool(rd.getrandbits(1)) else rd.choice(ltr)) +
              (rd.choice(num) if bool(rd.getrandbits(1)) else rd.choice(ltr)) +
              (rd.choice(num) if bool(rd.getrandbits(1)) else rd.choice(ltr)) +
              (rd.choice(num) if bool(rd.getrandbits(1)) else rd.choice(ltr)) +
              (rd.choice(num) if bool(rd.getrandbits(1)) else rd.choice(ltr)) +
              '`||')
    if rd.randint(-1000, 1000) == 0:
        f = open("winkeys", "a")
        f.write(key + '\n')
    await ctx.author.dm_channel.send(key)
    await ctx.send("Key has successfully been sent")


@client.command
async def worm(ctx, wlength):
    try:
        if wlength <= 1000:
            await ctx.send("<:wormhead:787786964295614495>" + (
                    "<:wormbody:787786942312874006>" * rd.randint(0, int(
                ctx.lower().split(" ")[1]))) + "<:wormtail:787786975703728208>")
        else:
            await ctx.send("Worm too long, died because it couldn't move!")
    except:
        await ctx.send("<:wormhead:787786964295614495>" + (
                "<:wormbody:787786942312874006>" * rd.randint(0, 10)) + "<:wormtail:787786975703728208>")


@client.event
async def on_message(message):
    f = open("new.log", "a")
    f.write("[" + str(message.created_at) + " GMT] : " + str(message.guild) + " #" + str(message.channel) + " - " + str(
        message.author) + ": " + message.content + "\n")
    f.close()
    print("[" + str(message.created_at) + " GMT] : " + str(message.guild) + " #" + str(message.channel) + " - " + str(
        message.author) + ": " + message.content)
    eq = open('eq', 'r')
    eqLines = eq.readlines()
    eqDat = []
    for line in eqLines:
        eqDat.append(line.strip().split("±"))
    sw = open('sw', 'r')
    swLines = sw.readlines()
    swDat = []
    for line in swLines:
        swDat.append(line.strip().split("±"))
    ew = open('ew', 'r')
    ewLines = ew.readlines()
    ewDat = []
    for line in ewLines:
        ewDat.append(line.strip().split("±"))
    ct = open('ct', 'r')
    ctLines = ct.readlines()
    ctDat = []
    for line in ctLines:
        ctDat.append(line.strip().split("±"))
    if message.author == client.user:
        return
    for data in eqDat:
        if data[0].split("·").__contains__(message.content.lower()):
            await message.channel.send(rd.choice(data[1].split("·")))
    for data in swDat:
        for item in data[0].split("·"):
            if message.content.lower().startswith(item):
                await message.channel.send(rd.choice(data[1].split("·")))
    for data in ewDat:
        for item in data[0].split("·"):
            if message.content.lower().endswith(item):
                await message.channel.send(rd.choice(data[1].split("·")))
    for data in ctDat:
        for item in data[0].split("·"):
            if message.content.lower().__contains__(item):
                await message.channel.send(rd.choice(data[1].split("·")))


client.run(TOKEN)

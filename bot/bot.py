import os
import random as rd
import discord
import pytz
from os import path
from discord.ext import commands
from discord.ext.commands import Bot
from discord.utils import get
from datetime import datetime
import youtube_dl

TOKEN = os.getenv('DISCORD_TOKEN')

client = Bot("^")
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


@client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        return
    await ctx.send(str(error))


class Information(commands.Cog):
    """Informational Commands"""

    @commands.command()
    async def ctime(self, ctx, tz="UTC"):
        """Tells you the current time of day in a timezone[tz], tz is default UTC"""
        dt = datetime.now(pytz.timezone(tz))
        await ctx.send(rd.choice(["It's ", "The current time is: ", "Here's The time: ",
                                  "BING BONG BING BONG who's your friend who likes to play?  "]) + dt.strftime(
            "%Y-%m-%d %H:%M:%S.%f") + " " + tz)


client.add_cog(Information(client))


class Fun(commands.Cog):
    """Commands for all your FUN needs!"""

    @commands.command()
    async def worm(self, ctx, length=69):
        """Makes a worm a given length, length becomes a random number between 0 and 64 inclusive if not defined"""
        if length < 0:
            await ctx.send("Worm cannot be a negative length, YOU DESTROYED THE UNIVERSE WITH A BLACK HOLE",
                           file=discord.File("bot/blackhole.gif"))
        elif length <= 64:
            await ctx.send("<:wormhead:787786964295614495>" + (
                    "<:wormbody:787786942312874006>" * length + "<:wormtail:787786975703728208>"))
        elif length == 69:
            await ctx.send("<:wormhead:787786964295614495>" + (
                    "<:wormbody:787786942312874006>" * rd.randint(0, 64) + "<:wormtail:787786975703728208>"))
        else:
            await ctx.send("Worm too long, died because it couldn't move!")
            await ctx.send(
                "<:deadwormhead:788823709154148384>  <:wormbody:787786942312874006> <:wormbody:787786942312874006><:wormbody:787786942312874006><:wormbody:787786942312874006> <:wormbody:787786942312874006>  <:wormtail:787786975703728208>")

    @commands.command()
    async def joke(self, ctx):
        """A joke-telling command to joke around"""
        j = open('bot/joke', 'r')
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

    @commands.command()
    async def genkey(self, ctx):

        """Sends you a random 20-digit hexadecimal key, has a 1 in 2001 chance of winning"""

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

    @commands.command()
    async def rickroll(self, ctx):

        """Rickrolls your friends in while in a discord call"""

        if not discord.opus.is_loaded():
            discord.opus.load_opus('libopus.so')
        voice = get(client.voice_clients, guild=ctx.guild)
        if path.exists("rickroll.mp3"):
            voice.play(discord.FFmpegPCMAudio("rickroll.mp3"))
            voice.volume = 100
            voice.is_playing()
        else:
            ydl_opts = {
                'format': 'bestaudio/best',
                'postprocessors': [{
                    'key': 'FFmpegExtractAudio',
                    'preferredcodec': 'mp3',
                    'preferredquality': '192',
                }],
            }
            with youtube_dl.YoutubeDL(ydl_opts) as ydl:
                ydl.download(["https://www.youtube.com/watch?v=dQw4w9WgXcQ"])
            for file in os.listdir("./"):
                if file.endswith(".mp3"):
                    os.rename(file, 'rickroll.mp3')
#             await rep_message.guild.fetch_member(776538622958501888).edit(mute=False)
            voice.play(discord.FFmpegPCMAudio("rickroll.mp3"))
            voice.volume = 100
            voice.is_playing()


client.add_cog(Fun(client))


class Audio(commands.Cog):
    """[EXPERIMENTAL] Audio Functionality for EEBot"""

    @commands.command()
    async def join(self, ctx):

        """Join current audio channel"""

        if not discord.opus.is_loaded():
            discord.opus.load_opus('libopus.so')
        await ctx.author.voice.channel.connect()

    @commands.command()
    async def leave(self, ctx):

        """Leaves current audio channel"""

        await ctx.voice_client.disconnect()

    @commands.command()
    async def play(self, ctx, link):

        """Plays audio of given YouTube link"""

        if not discord.opus.is_loaded():
            discord.opus.load_opus('libopus.so')
        voice = get(client.voice_clients, guild=ctx.guild)
        ydl_opts = {
            'format': 'bestaudio/best',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }],
        }
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            ydl.download([link])
        for file in os.listdir("./"):
            if file.endswith(".mp3"):
                os.rename(file, 'song.mp3')
#         await rep_message.guild.fetch_member(776538622958501888).edit(mute=False)
        voice.play(discord.FFmpegPCMAudio("song.mp3"))
        voice.volume = 100
        voice.is_playing()

    @commands.command()
    async def stop(self, ctx):

        """Plays audio of given YouTube link"""

        await ctx.voice_client.disconnect()
        await ctx.author.voice.channel.connect()


client.add_cog(Audio(client))

@client.command()
async def report(ctx, user, reason):
    """Reports person"""
    await ctx.channel.send("This incident has been reported")

@client.listen('on_message')
async def onMessage(message):
    dt = datetime.now(pytz.timezone("UTC"))
    f = open("new.log", "a")
    f.write("[" + dt.strftime("%Y-%m-%d %H:%M:%S.%f") + " UTC] : " + str(message.guild) + " #" + str(
        message.channel) + " - " + str(
        message.author) + ": " + message.content + "\n")
    f.close()
    print(str(message.guild) + " #" + str(message.channel) + " - " + str(
        message.author) + ": " + message.content + "\nMessage ID: " + str(message.id) + ", Channel ID: " + str(message.channel.id))
    eq = open('bot/eq', 'r')
    eqLines = eq.readlines()
    eqDat = []
    for line in eqLines:
        eqDat.append(line.strip().split("±"))
    sw = open('bot/sw', 'r')
    swLines = sw.readlines()
    swDat = []
    for line in swLines:
        swDat.append(line.strip().split("±"))
    ew = open('bot/ew', 'r')
    ewLines = ew.readlines()
    ewDat = []
    for line in ewLines:
        ewDat.append(line.strip().split("±"))
    ct = open('bot/ct', 'r')
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

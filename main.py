from http import client
from discord.ext import commands
import discord
import random
import math

n = random.randint(0, 100000)

bot = commands.Bot(command_prefix='!')


# PING PONG
@bot.command()
async def ping(ctx):
    await ctx.send('pong')


# RANDOM LICZBA
@bot.command()
async def liczba(ctx):
    await ctx.send(n)


# TA SAMA WIADOMOŚĆ
@bot.command()
async def say(ctx, *, message):
    await ctx.send(f"{message}")


# TA SAMA LICZBA
@bot.command()
async def dwieliczby(ctx, arg1, arg2):
    await ctx.send((arg1 + arg2).format(arg1, arg2))


# ALFABETY
@bot.command()
async def polski_alfabet(ctx):
    await ctx.send(' a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, r, s, ś, t, u, w, y, z')


@bot.command()
async def kotek(cxt, *, message):
    if message.author == bot.user:
        return
    if message.content == 'embed':
        embed = discord.Embed(
            title='Hello',
            description='This is a embed',
            colour=discord.Colour.purple())
        embed.set_footer(text='embed')
        embed.set_image(url="https://www.google.com/search?q=trojkat++wzor&tbm=isch&ved=2ahUKEwiSzK_Fg-b2AhW8wgIHHdekD44Q2-cCegQIABAA&oq=trojkat++wzor&gs_lcp=CgNpbWcQAzIFCAAQgAQyBQgAEIAEMgUIABCABDIGCAAQBxAeMgYIABAHEB4yBggAEAcQHjIGCAAQBxAeMgYIABAHEB4yBggAEAcQHjIGCAAQBxAeOgcIIxDvAxAnUPkGWIUMYMcPaABwAHgAgAFIiAHBAZIBATOYAQCgAQGqAQtnd3Mtd2l6LWltZ8ABAQ&sclient=img&ei=_zRAYtLQD7yFi-gP18m-8Ag&bih=939&biw=1879&client=opera-gx&hs=QXT#imgrc=F54-fQLo0y35JM")
    await message.channel.send(embed=embed)


# HELP OKŁADKA
@bot.command()
async def pomoc(ctx):
    embed = discord.Embed(title="!HELP", description=".", color=0xdd0e0e)
    embed.add_field(name="KOMENDY   ( PREFIX !  )",
                    value="SAY(...)    PING   LICZBA ", inline=True)
    await ctx.send(embed=embed)


@bot.command()
async def piesek(ctx):
    embed = discord.Embed(title="Hello", url="", description="test", color=0xa600ff)
    embed.set_thumbnail(url="https://camo.githubusercontent.com/c9ac22ae1c792937eb759c5dac63ed3159488ede5d60faac81acfb3303c57f02/687474703a2f2f692e696d6775722e636f6d2f6b5959435874432e706e67")
    embed.add_field(name="Dziobak", value="tak", inline=True)
    await ctx.send(embed=embed)


bot.run('OTU3MzI3NTI2ODc3ODc2MzI0.Yj9KvA.Huh4764_fgRPrdG4SlCqQc0UQwo')

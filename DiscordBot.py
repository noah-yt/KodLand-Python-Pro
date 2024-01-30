import discord
from discord.ext import commands
import random

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

async def lancio_moneta():
    if random.randint(0, 1) == 1: return "Testa" 
    else: "Croce"

def gen_pass(lenght):
    char = "+-/*!&$#?=@<>"
    return ''.join(random.choice(char) for i in range(lenght))

@bot.event
async def on_ready():
    print(f'Hai fatto l\'accesso come {bot.user}')

@bot.command()
async def passw(ctx, lungh: int):
    await ctx.send(gen_pass(lungh))

@bot.command()
async def moneta(ctx):
    await ctx.send(lancio_moneta())

bot.run("token")

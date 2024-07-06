import discord
from discord.ext import commands
from bot_logic import gen_pass
from bot_logic import moneda

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'Hemos iniciado sesión como {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Hola, soy un bot {bot.user}!')

@bot.command()
async def moneda(ctx):
    await ctx.send(moneda())

@bot.command()
async def pasw(ctx):
    await ctx.send(gen_pass(10))



bot.run("")

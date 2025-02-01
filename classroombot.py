# IMPORT COMMANDS FROM THE DISCORD.EXT MODULE.
import discord
from discord.ext import commands

# CREATES A NEW BOT OBJECT WITH A SPECIFIED PREFIX. IT CAN BE WHATEVER YOU WANT IT TO BE.
bot = commands.Bot(command_prefix=".", intents = discord.Intents.all())
bot.remove_command('help')


@bot.command()
async def help(ctx):
	await ctx.channel.send("```------------------------------------------------------------- SEM V ------------------------------------------------------------\n\nFor web services(WS) Classroom Code Type : .ws \nFor Artificial Intelligence(AI) Classroom Code Type : .ai \nFor Software Testing and Netowk Security(STQA) Classroom Code Type : .stqa \nFor Game Programming Classroom Code Type : .gp \nFor Google Class room code for Information and Network Security (INS) Type : .ins\n\n------------------------------------------------------------- SEM VI ------------------------------------------------------------\n\nFor Cloud Computing Classroom Code type : .cc\nFor Wireless Sensor Networks and Mobile Communication Classroom Code type : .wsnm\nFor Ethical Hacking Classroom Code type : .eh\n\n------------------------------------------------------------- EXTRAS -------------------------------------------------------------\n\nFor Paying Fees Type: .payfees\nFor Checking ping in ms Type: .ping```")
@bot.command()
async def stqa(ctx):
    await ctx.channel.send(":arrow_down: Google Class room code for Software Testing and Netowk Security(STQA) :arrow_down: \n \n                                                                  **abcdefg**")
@bot.command()
async def ai(ctx):
	await ctx.channel.send(":arrow_down: Google Class room code for Artificial Intelligence(AI) :arrow_down:  \n \n                                              **abcdefg**")
@bot.command()
async def ws(ctx):
	await ctx.channel.send(":arrow_down: Google Class room code for web services(WS) :arrow_down:  \n \n                                          **abcdefg**")
@bot.command()
async def gp(ctx):
	await ctx.channel.send(":arrow_down: Google Class room code for Game Programming (GP) :arrow_down:  \n \n                                          **abcdefg**")
@bot.command()
async def ins(ctx):
	await ctx.channel.send(":arrow_down: Google Class room code for Information and Network Security (INS) :arrow_down:  \n \n                                                           **abcdefg**")
@bot.command()
async def cc(ctx):
	await ctx.channel.send(":arrow_down: Google Class room code for Cloud Computing (CC) :arrow_down:  \n \n                                          **abcdefg**\n\n:arrow_down:  Direct Link  :arrow_down:\n\nhttps://classroom.google.com/")
@bot.command()
async def payfees(ctx):
	await ctx.channel.send(":arrow_down: Click Here to Pay Fees :arrow_down:  \n \nhttps://www.google.com")
@bot.command()
async def eh(ctx):
	await ctx.channel.send(":arrow_down: Google Class room code for Ethical Hacking (EH) :arrow_down:  \n \n                                          **abcdefg**\n\n:arrow_down:  Direct Link  :arrow_down:\n\nhttps://classroom.google.com/")
@bot.command()
async def wsnm(ctx):
	await ctx.channel.send(":arrow_down: Google Class room code for Wireless Sensor Networks and Mobile Communication (WSNM) :arrow_down:  \n \n                                                                                    **abcdefg**\n\n:arrow_down:  Direct Link  :arrow_down:\n\nhttps://classroom.google.com/")
@bot.command()
async def ping(ctx):
    await ctx.reply(f'Ping is {round(bot.latency * 1000)} ms')

# EXECUTES THE BOT WITH THE SPECIFIED TOKEN. TOKEN HAS BEEN REMOVED AND USED JUST AS AN EXAMPLE.
print("Bot is Ready To Roll")


@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name=".help"))



bot.run('bot_token')

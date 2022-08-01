import disnake,random,asyncio,asyncpg,datetime,time,os,re,disnake,traceback,sys,psutil,time,datetime, platform
from datetime import date,timedelta
from disnake.ext import tasks, commands
intents = disnake.Intents.all()
#intents.members = True
client = commands.Bot(command_prefix=disnake.ext.commands.when_mentioned, intents = intents)
botname = 'Bot Manager'
ver = '0.1'
date1 = 'June 30, 2022'
built = 'Yota'
num = '#0556'
bul = '\u2022'
blank = '\u200b'
black = 000000
color = 0xa488fa
color1 = disnake.Colour(0xff0000) #errors
color2 = disnake.Colour.light_gray() #modlog embeds
color3 = black #help 
color4 = disnake.Colour.green() #suggestion accept color
color5 = disnake.Color.blue()
color6 = disnake.Color.red()
for filename in os.listdir("./cogs"):
    if filename.endswith(".py"):
        client.load_extension(f"cogs.{filename[:-3]}")
test_guilds = [798352530564055050, 810552816527081472, 894073671172382753]
#on ready
@client.event
async def on_ready():
    await client.change_presence(activity=disnake.Activity(type=disnake.ActivityType.playing, name='Bot Manager'))
    print(f'{client.user.name} has connected to Discord!')
@client.event
async def on_slash_command_error(inter, error):
    try:
        mem_id = 839281450671013898
        user = client.get_user(mem_id)
        embed = disnake.Embed(title = f'**An Error Has Occurred **', description = f'{error}', color = color1)
        embed.set_footer(text=f'{client.user.name} | Executed by {inter.author.name}', icon_url = client.user.display_avatar.url)
        embed.set_thumbnail(url=client.user.display_avatar.url)
        await user.send(embed = embed)
    except:
        mem_id = 839281450671013898
        user = bot.get_user(mem_id)
        embed = disnake.Embed(title = f'**An Error Has Occurred **', description = f'{error}', color = color1)
        embed.set_footer(text=f'{client.user.name} | Executed in {inter.guild}', icon_url = client.user.display_avatar.url)
        embed.set_thumbnail(url=client.user.display_avatar.url)
        await user.send(embed = embed)
#@client.event
#async def on_command_error(inter, error):
#    pass
#end of bot stuff
from datetime import datetime
now1 = datetime.now()
start_time= now1.strftime('%I:%M %p')
print(f'Version: {ver}')
print(f'Built by: {built}{num}')
print('Last run at:', start_time)
print(f'{botname} Started Sucessfully')
with open("token.txt") as f:
    token = f.readline()
client.run(token)

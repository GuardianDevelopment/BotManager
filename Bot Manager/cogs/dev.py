from main import *
import disnake
from datetime import datetime
from subprocess import call
from requests.exceptions import HTTPError, Timeout
starttime = datetime.now()
class dev(commands.Cog):
    def __init__(self,client):
        self.client = client
    #restart command
    @commands.slash_command(description= 'Restart the bot (Dev use only)')
    async def restart(self, inter):
        await inter.response.defer()
        if str(inter.author.id) == 'your_id':
            embed = disnake.Embed(title=f'**__Restarting {client.user.name}__**', description = f'```Please Allow For Up To Five (5) Seconds For Me To Be Back Up And Running.```', color=color)
            embed.set_footer(text=f'{client.user.name} v{ver} | Executed by {inter.author.name}', icon_url=client.user.display_avatar.url)
            embed.set_thumbnail(url=client.user.display_avatar.url)
            await inter.send(embed=embed)
            call(["python3.10", "startup.py"])
            exit()
        elif str(inter.author.id) == 'your_id':
            embed = disnake.Embed(title=f'**__Restarting {client.user.name}__**', description = f'```Please Allow For Up To Five (5) Seconds For Me To Be Back Up And Running.```', color=color)
            embed.set_footer(text=f'{client.user.name} v{ver} | Executed by {inter.author.name}', icon_url=client.user.display_avatar.url)
            embed.set_thumbnail(url=client.user.display_avatar.url)
            await inter.send(embed=embed)
            call(["python3.10", "startup.py"])
            exit()
        else:
            embed = disnake.Embed(title=f'**__Restart Error__**', description = f'```{inter.author.name}, You Are Not Authorized To Use /Restart.```', color=color1)
            embed.set_footer(text=f'{client.user.name} v{ver} | Executed by {inter.author.name}', icon_url=client.user.display_avatar.url)
            embed.set_thumbnail(url=client.user.display_avatar.url)
            await inter.send(embed=embed)
    #stop command
    @commands.slash_command(description= 'Stop the bot (Dev Use Only)')
    async def stop(self, inter):
        await inter.response.defer()
        if str(inter.author.id) == 'your_id':
            embed = disnake.Embed(title=f'**__Stopping {client.user.name}__**', description = f'```Please Allow For Up To Five (5) Seconds For Me To Be Fully Shut Down.```', color=color)
            embed.set_footer(text=f'{client.user.name} v{ver} | Executed by {inter.author.name}', icon_url=client.user.display_avatar.url)
            embed.set_thumbnail(url=client.user.display_avatar.url)
            await inter.send(embed=embed)
            exit()
        elif str(inter.author.id) == 'your_id':
            embed = disnake.Embed(title=f'**__Stopping {client.user.name}__**', description = f'```Please Allow For Up To Five (5) Seconds For Me To Be Fully Shut Down.```', color=color)
            embed.set_footer(text=f'{client.user.name} v{ver} | Executed by {inter.author.name}', icon_url=client.user.display_avatar.url)
            embed.set_thumbnail(url=client.user.display_avatar.url)
            await inter.send(embed=embed)
            exit()
        else:
            embed = disnake.Embed(title=f'**__Restart Error__**', description = f'```{inter.author.name}, You Are Not Authorized To Use /Stop.```', color=color1)
            embed.set_footer(text=f'{client.user.name} v{ver} | Executed by {inter.author.name}', icon_url=client.user.display_avatar.url)
            embed.set_thumbnail(url=client.user.display_avatar.url)
            await inter.send(embed=embed)
    
    @commands.slash_command(description="View information about the bot")
    async def info(self, inter):
        await inter.response.defer()
        now = datetime.now()
        elapsed = now - starttime
        seconds = elapsed.seconds
        minutes, seconds = divmod(seconds, 60)
        hours, minutes = divmod(minutes, 60)
        cpu = psutil.Process(os.getpid()).memory_info().rss / 1024 ** 2
        cpu1 = psutil.cpu_percent()
        servers = client.guilds
        servers1 = len(client.guilds)
        embed=disnake.Embed(title=f'__**{client.user.name}**__',description="About the bot!",color=color)
        embed.set_footer(text=f'{client.user.name} | Requested by {inter.author.name}', icon_url = client.user.display_avatar.url)
        embed.set_thumbnail(url=client.user.display_avatar.url)
        embed.add_field(name='__**Info**__', value="```Ping: {} ms\nVersion: {}\nCPU Usage: {}%\nUptime: {}d {}h {}m {}s\nDeveloper: {}{}\nCurrently in: {} servers\nReleased on: {}```".format(round(client.latency * 1000),ver, cpu1,elapsed.days, hours, minutes, seconds, built, num, servers1, date1), inline=False)
        await inter.send(embed=embed)
    
        
def setup(client):
    client.add_cog(dev(client))

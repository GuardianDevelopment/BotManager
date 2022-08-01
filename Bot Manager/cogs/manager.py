from main import *
import disnake
from datetime import datetime
import subprocess
import os
from subprocess import call
class manager(commands.Cog):
    def __init__(self,client):
        self.client = client
        self.status.start()
    test_guilds = []
    
    @commands.slash_command(guild_ids = test_guilds, description="")
    @commands.default_member_permissions(administrator=True)
    async def bot(self, inter):
        pass
    bot_list = commands.option_enum(["Ark Guardian", "Ark Pop", "Bic Development", "BMS Manager", "Guardian", "Tickets", "Dupe Protection"])
    @bot.sub_command(guild_ids = test_guilds, description = 'Restart A Bot If It Went Down')
    async def restart(self, inter, bot: bot_list):
        """
    Choose A Bot To Restart

    Parameters
    ----------
    bot: Select A Bot To Restart

    """
        await inter.response.defer()
        if bot == 'Ark Guardian':
            member = inter.guild.get_member(bot_id)
            if str(inter.author.id) != 'your_user_id' or str(inter.author.id) != 'your_user_id':
                if str(member.status) == 'offline':
                    embed = disnake.Embed(title=f'**__Restarting {bot}__**', description = f'```Please Allow For Up To Five (5) Seconds For {bot} To Be Up And Running.```', color=color)
                    embed.set_footer(text=f'{client.user.name} v{ver} | Executed by {inter.author.name}', icon_url=client.user.display_avatar.url)
                    embed.set_thumbnail(url=client.user.display_avatar.url)
                    await inter.send(embed=embed)
                    os.chdir("/path to your bot file")
                    subprocess.Popen("screen -dm bash -c; python3.10 your_bot.py", shell=True)
                else:
                    embed = disnake.Embed(title=f'**__Restart Error__**', description = f'```{inter.author.name}, {bot} Is Online And Does Not Need To Be Restarted.```', color=color1)
                    embed.set_footer(text=f'{client.user.name} v{ver} | Executed by {inter.author.name}', icon_url=client.user.display_avatar.url)
                    embed.set_thumbnail(url=client.user.display_avatar.url)
                    await inter.send(embed=embed)                    
            else:
                embed = disnake.Embed(title=f'**__Restart Error__**', description = f'```{inter.author.name}, You Are Not Authorized To Restart {bot}.```', color=color1)
                embed.set_footer(text=f'{client.user.name} v{ver} | Executed by {inter.author.name}', icon_url=client.user.display_avatar.url)
                embed.set_thumbnail(url=client.user.display_avatar.url)
                await inter.send(embed=embed)
        elif bot == 'Ark Pop':
            member = inter.guild.get_member(bot_id)
            if str(inter.author.id) != 'your_user_id' or str(inter.author.id) != 'your_user_id':
                if str(member.status) == 'offline':
                    embed = disnake.Embed(title=f'**__Restarting {bot}__**', description = f'```Please Allow For Up To Five (5) Seconds For {bot} To Be Up And Running.```', color=color)
                    embed.set_footer(text=f'{client.user.name} v{ver} | Executed by {inter.author.name}', icon_url=client.user.display_avatar.url)
                    embed.set_thumbnail(url=client.user.display_avatar.url)
                    await inter.send(embed=embed)
                    os.chdir("/path to your bot file")
                    subprocess.Popen("screen -dm bash -c; python3.10 your_bot.py", shell=True)
                else:
                    embed = disnake.Embed(title=f'**__Restart Error__**', description = f'```{inter.author.name}, {bot} Is Online And Does Not Need To Be Restarted.```', color=color1)
                    embed.set_footer(text=f'{client.user.name} v{ver} | Executed by {inter.author.name}', icon_url=client.user.display_avatar.url)
                    embed.set_thumbnail(url=client.user.display_avatar.url)
                    await inter.send(embed=embed) 
            else:
                embed = disnake.Embed(title=f'**__Restart Error__**', description = f'```{inter.author.name}, You Are Not Authorized To Restart {bot}.```', color=color1)
                embed.set_footer(text=f'{client.user.name} v{ver} | Executed by {inter.author.name}', icon_url=client.user.display_avatar.url)
                embed.set_thumbnail(url=client.user.display_avatar.url)
                await inter.send(embed=embed)
        elif bot == 'Bic Development':
            member = inter.guild.get_member(bot_id)
            if str(inter.author.id) != 'your_user_id' or str(inter.author.id) != 'your_user_id':
                if str(member.status) == 'offline':
                    embed = disnake.Embed(title=f'**__Restarting {bot}__**', description = f'```Please Allow For Up To Five (5) Seconds For {bot} To Be Up And Running.```', color=color)
                    embed.set_footer(text=f'{client.user.name} v{ver} | Executed by {inter.author.name}', icon_url=client.user.display_avatar.url)
                    embed.set_thumbnail(url=client.user.display_avatar.url)
                    await inter.send(embed=embed)
                    os.chdir("/path to your bot file")
                    subprocess.Popen("screen -dm bash -c; python3.10 your_bot.py", shell=True)
                else:
                    embed = disnake.Embed(title=f'**__Restart Error__**', description = f'```{inter.author.name}, {bot} Is Online And Does Not Need To Be Restarted.```', color=color1)
                    embed.set_footer(text=f'{client.user.name} v{ver} | Executed by {inter.author.name}', icon_url=client.user.display_avatar.url)
                    embed.set_thumbnail(url=client.user.display_avatar.url)
                    await inter.send(embed=embed)
            else:
                embed = disnake.Embed(title=f'**__Restart Error__**', description = f'```{inter.author.name}, You Are Not Authorized To Restart {bot}.```', color=color1)
                embed.set_footer(text=f'{client.user.name} v{ver} | Executed by {inter.author.name}', icon_url=client.user.display_avatar.url)
                embed.set_thumbnail(url=client.user.display_avatar.url)
                await inter.send(embed=embed)
        elif bot == 'BMS Manager':
            member = inter.guild.get_member(bot_id)
            if str(inter.author.id) != 'your_user_id' or str(inter.author.id) != 'your_user_id':
                if str(member.status) == 'offline':
                    embed = disnake.Embed(title=f'**__Restarting {bot}__**', description = f'```Please Allow For Up To Five (5) Seconds For {bot} To Be Up And Running.```', color=color)
                    embed.set_footer(text=f'{client.user.name} v{ver} | Executed by {inter.author.name}', icon_url=client.user.display_avatar.url)
                    embed.set_thumbnail(url=client.user.display_avatar.url)
                    await inter.send(embed=embed)
                    os.chdir("/path to your bot file")
                    subprocess.Popen("screen -dm bash -c; python3.10 your_bot.py", shell=True)
                else:
                    embed = disnake.Embed(title=f'**__Restart Error__**', description = f'```{inter.author.name}, {bot} Is Online And Does Not Need To Be Restarted.```', color=color1)
                    embed.set_footer(text=f'{client.user.name} v{ver} | Executed by {inter.author.name}', icon_url=client.user.display_avatar.url)
                    embed.set_thumbnail(url=client.user.display_avatar.url)
                    await inter.send(embed=embed)
            else:
                embed = disnake.Embed(title=f'**__Restart Error__**', description = f'```{inter.author.name}, You Are Not Authorized To Restart {bot}.```', color=color1)
                embed.set_footer(text=f'{client.user.name} v{ver} | Executed by {inter.author.name}', icon_url=client.user.display_avatar.url)
                embed.set_thumbnail(url=client.user.display_avatar.url)
                await inter.send(embed=embed)
        elif bot == 'Guardian':
            member = inter.guild.get_member(bot_id)
            if str(inter.author.id) != 'your_user_id' or str(inter.author.id) != 'your_user_id':
                if str(member.status) == 'offline':
                    embed = disnake.Embed(title=f'**__Restarting {bot}__**', description = f'```Please Allow For Up To Five (5) Seconds For {bot} To Be Up And Running.```', color=color)
                    embed.set_footer(text=f'{client.user.name} v{ver} | Executed by {inter.author.name}', icon_url=client.user.display_avatar.url)
                    embed.set_thumbnail(url=client.user.display_avatar.url)
                    await inter.send(embed=embed)
                    os.chdir("/path to your bot file")
                    subprocess.Popen("screen -dm bash -c; python3.10 your_bot.py", shell=True)
                else:
                    embed = disnake.Embed(title=f'**__Restart Error__**', description = f'```{inter.author.name}, {bot} Is Online And Does Not Need To Be Restarted.```', color=color1)
                    embed.set_footer(text=f'{client.user.name} v{ver} | Executed by {inter.author.name}', icon_url=client.user.display_avatar.url)
                    embed.set_thumbnail(url=client.user.display_avatar.url)
                    await inter.send(embed=embed)
            else:
                embed = disnake.Embed(title=f'**__Restart Error__**', description = f'```{inter.author.name}, You Are Not Authorized To Restart {bot}.```', color=color1)
                embed.set_footer(text=f'{client.user.name} v{ver} | Executed by {inter.author.name}', icon_url=client.user.display_avatar.url)
                embed.set_thumbnail(url=client.user.display_avatar.url)
                await inter.send(embed=embed)
        elif bot == 'Tickets':
            member = inter.guild.get_member(bot_id)
            if str(inter.author.id) != 'your_user_id' or str(inter.author.id) != 'your_user_id':
                if str(member.status) == 'offline':
                    embed = disnake.Embed(title=f'**__Restarting {bot}__**', description = f'```Please Allow For Up To Five (5) Seconds For {bot} To Be Up And Running.```', color=color)
                    embed.set_footer(text=f'{client.user.name} v{ver} | Executed by {inter.author.name}', icon_url=client.user.display_avatar.url)
                    embed.set_thumbnail(url=client.user.display_avatar.url)
                    await inter.send(embed=embed)
                    os.chdir("/path to your bot file")
                    subprocess.Popen("screen -dm bash -c; python3.10 your_bot.py", shell=True)
                else:
                    embed = disnake.Embed(title=f'**__Restart Error__**', description = f'```{inter.author.name}, {bot} Is Online And Does Not Need To Be Restarted.```', color=color1)
                    embed.set_footer(text=f'{client.user.name} v{ver} | Executed by {inter.author.name}', icon_url=client.user.display_avatar.url)
                    embed.set_thumbnail(url=client.user.display_avatar.url)
                    await inter.send(embed=embed)
            else:
                embed = disnake.Embed(title=f'**__Restart Error__**', description = f'```{inter.author.name}, You Are Not Authorized To Restart {bot}.```', color=color1)
                embed.set_footer(text=f'{client.user.name} v{ver} | Executed by {inter.author.name}', icon_url=client.user.display_avatar.url)
                embed.set_thumbnail(url=client.user.display_avatar.url)
                await inter.send(embed=embed)
        elif bot == 'Dupe Protection':
            member = inter.guild.get_member(bot_id)
            if str(inter.author.id) != 'your_user_id' or str(inter.author.id) != 'your_user_id':
                if str(member.status) == 'offline':
                    embed = disnake.Embed(title=f'**__Restarting {bot}__**', description = f'```Please Allow For Up To Five (5) Seconds For {bot} To Be Up And Running.```', color=color)
                    embed.set_footer(text=f'{client.user.name} v{ver} | Executed by {inter.author.name}', icon_url=client.user.display_avatar.url)
                    embed.set_thumbnail(url=client.user.display_avatar.url)
                    await inter.send(embed=embed)
                    os.chdir("/path to your bot file")
                    subprocess.Popen("screen -dm bash -c; python3.10 your_bot.py", shell=True)
                else:
                    embed = disnake.Embed(title=f'**__Restart Error__**', description = f'```{inter.author.name}, {bot} Is Online And Does Not Need To Be Restarted.```', color=color1)
                    embed.set_footer(text=f'{client.user.name} v{ver} | Executed by {inter.author.name}', icon_url=client.user.display_avatar.url)
                    embed.set_thumbnail(url=client.user.display_avatar.url)
                    await inter.send(embed=embed)
            else:
                embed = disnake.Embed(title=f'**__Restart Error__**', description = f'```{inter.author.name}, You Are Not Authorized To Restart {bot}.```', color=color1)
                embed.set_footer(text=f'{client.user.name} v{ver} | Executed by {inter.author.name}', icon_url=client.user.display_avatar.url)
                embed.set_thumbnail(url=client.user.display_avatar.url)
                await inter.send(embed=embed)
    @commands.slash_command(guild_ids = test_guilds, description="Set Up The Bot Status")
    @commands.default_member_permissions(administrator=True)
    async def setup(self, inter, channel:disnake.TextChannel):
        """
    Set Up The Bot Status

    Parameters
    ----------
    channel: Enter The Channel To Send The Status Embeds To
    """
        await inter.response.defer()
        await inter.send('sending now')
        embed = disnake.Embed(title=f'**__Bot Status__**', description = f'Please Wait', color=color)
        embed.set_footer(text=f'{client.user.name} v{ver} | Executed by {client.user.name}', icon_url=client.user.display_avatar.url)
        embed.set_thumbnail(url=client.user.display_avatar.url)
        await channel.send(embed=embed)

        embed2 = disnake.Embed(title=f'**__VPS Status__**', description = f'Please Wait', color=color)
        embed2.set_footer(text=f'{client.user.name} v{ver} | Executed by {client.user.name}', icon_url=client.user.display_avatar.url)
        embed2.set_thumbnail(url=client.user.display_avatar.url)
        await channel.send(embed=embed2)

    @tasks.loop(minutes = 5)
    async def status(self):
        await client.wait_until_ready()
        for guild in client.guilds:
            if guild.id == your_guild_id:
                #try:
                channel = client.get_channel(channel_id_of_the_status_channel)
                bot_message = await channel.fetch_message(message_id_of_bot_status_message)
                vps_message = await channel.fetch_message(message_id_of_vps_status_message)
                ark_guardian = guild.get_member(bot_id)
                ark_pop = guild.get_member(bot_id2)
                guardian = guild.get_member(bot_id3)
                tickets = guild.get_member(bot_id4)
                dupe = guild.get_member(bot_id5)
                cpu = psutil.Process(os.getpid()).memory_info().rss / 1024 ** 2
                cpu1 = psutil.cpu_percent()

                now1 = datetime.now()
                start_time1= now1.strftime('%I:%M %p')
                
                embed = disnake.Embed(title=f'**__Bot Status__**', description = f'', color=color)
                embed.set_footer(text=f'{client.user.name} v{ver} | Updated {start_time1}', icon_url=client.user.display_avatar.url)
                embed.set_thumbnail(url=client.user.display_avatar.url)

                embed1 = disnake.Embed(title=f'**__VPS Status__**', description = f'', color=color)
                embed1.set_footer(text=f'{client.user.name} v{ver} | Updated {start_time1}', icon_url=client.user.display_avatar.url)
                embed1.set_thumbnail(url=client.user.display_avatar.url)

                if str(ark_guardian.status) == 'offline':
                    dot1 = ':red_circle:'
                    act1 == 'Bot is offline'
                    os.chdir("/path to your bot file")
                    subprocess.Popen("screen -dm bash -c; python3.10 your_bot.py", shell=True)
                if str(ark_guardian.status) == 'online':
                    dot1 = ':green_circle:'
                    try:
                        act1 = f'{ark_guardian.activity.type.name.upper()} {ark_guardian.activity.name.upper()}'
                    except:
                        act1 = f'Bot is online'
                if str(ark_pop.status) == 'offline':
                    dot2 = ':red_circle:'
                    act2 = 'Bot is offline'
                    os.chdir("/path to your bot file")
                    subprocess.Popen("screen -dm bash -c; python3.10 your_bot.py", shell=True)
                if str(ark_pop.status) == 'online':
                    dot2 = ':green_circle:'
                    try:
                        act2 = f'{ark_pop.activity.type.name.upper()} {ark_pop.activity.name.upper()}'
                    except:
                        act2 = 'Bot is online'
                if str(guardian.status) == 'offline':
                    dot3 = ':red_circle:'
                    act3 == 'Bot is offline'
                    os.chdir("/path to your bot file")
                    subprocess.Popen("screen -dm bash -c; python3.10 your_bot.py", shell=True)
                if str(guardian.status) == 'online':
                    dot3 = ':green_circle:'
                    try:
                        act3 = f'{guardian.activity.type.name.upper()} {guardian.activity.name.upper()}'
                    except:
                        act3 = 'Bot is online'
                if str(tickets.status) == 'offline':
                    dot4 = ':red_circle:'
                    act4 = 'Bot is offline'
                    os.chdir("/path to your bot file")
                    subprocess.Popen("screen -dm bash -c; python3.10 your_bot.py", shell=True)
                if str(tickets.status) == 'online':
                    dot4 = ':green_circle:'
                    try:
                        act4 = f'{tickets.activity.type.name.upper()} {tickets.activity.name.upper()}'
                    except:
                        act4 = 'Bot is online'
                if str(dupe.status) == 'offline':
                    dot5 = ':red_circle:'
                    act5 = 'Bot is offline'
                    os.chdir("/path to your bot file")
                    subprocess.Popen("screen -dm bash -c; python3.10 your_bot.py", shell=True)
                if str(dupe.status) == 'online':
                    dot5 = ':green_circle:'
                    try:
                        act5 = f'{dupe.activity.type.name.upper()} {dupe.activity.name.upper()}'
                    except:
                        act5 = 'Bot is online'

                embed.add_field(name = f'{dot1} Ark Guardian', value = f'```{act1}```', inline = False)
                embed.add_field(name = f'{dot2} Ark Pop', value = f'```{act2}```', inline = False)
                embed.add_field(name = f'{dot5} Ark Server Protection', value = f'```{act5}```', inline = False)
                embed.add_field(name = f'{dot3} Guardian', value = f'```{act3}```', inline = False)
                embed.add_field(name = f'{dot4} Tickets', value = f'```{act4}```', inline = False)

                embed1.add_field(name = f'<:cpu:1002940699043434576> CPU Usage', value = f'{blank}```{cpu1}%```{blank}', inline = False)
                embed1.add_field(name = f'<:ram:1002941360048971816> Ram Usage', value = f'{blank}```{psutil.virtual_memory()[2]}%```{blank}', inline = False)
                embed1.add_field(name = f'<:os:1002942156434067568> Operating System', value = f'{blank}```{platform.system()} {platform.release()}```{blank}', inline = False)
                
                await bot_message.edit(embed=embed)
                
                await vps_message.edit(embed=embed1)
                    
                #except:
                    #pass
                
        
def setup(client):
    client.add_cog(manager(client))

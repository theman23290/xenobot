import discord
from discord.ext import commands
bot = commands.Bot(command_prefix='>')
bot.remove_command("help")

title = '''| || || |     | |                       
| || || | ____| | ____ ___  ____   ____ 
| ||_|| |/ _  ) |/ ___) _ \|    \ / _  )
| |___| ( (/ /| ( (__| |_| | | | ( (/ / 
 \______|\____)_|\____)___/|_|_|_|\____)
'''

ascii = '''```██████╗ ██╗ ██████╗      ██████╗  █████╗ ██╗   ██╗
██╔══██╗██║██╔════╝     ██╔════╝ ██╔══██╗╚██╗ ██╔╝
██████╔╝██║██║  ███╗    ██║  ███╗███████║ ╚████╔╝ 
██╔══██╗██║██║   ██║    ██║   ██║██╔══██║  ╚██╔╝  
██████╔╝██║╚██████╔╝    ╚██████╔╝██║  ██║   ██║   
╚═════╝ ╚═╝ ╚═════╝      ╚═════╝ ╚═╝  ╚═╝   ╚═╝```'''

thinkEmoji = '''```⠀⠰⡿⠿⠛⠛⠻⠿⣷
⠀⠀⠀⠀⠀⠀⣀⣄⡀⠀⠀⠀⠀⢀⣀⣀⣤⣄⣀⡀
⠀⠀⠀⠀⠀⢸⣿⣿⣷⠀⠀⠀⠀⠛⠛⣿⣿⣿⡛⠿⠷
⠀⠀⠀⠀⠀⠘⠿⠿⠋⠀⠀⠀⠀⠀⠀⣿⣿⣿⠇
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠁

⠀⠀⠀⠀⣿⣷⣄⠀⢶⣶⣷⣶⣶⣤⣀
⠀⠀⠀⠀⣿⣿⣿⠀⠀⠀⠀⠀⠈⠙⠻⠗
⠀⠀⠀⣰⣿⣿⣿⠀⠀⠀⠀⢀⣀⣠⣤⣴⣶⡄
⠀⣠⣾⣿⣿⣿⣥⣶⣶⣿⣿⣿⣿⣿⠿⠿⠛⠃
⢰⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡄
⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡁
⠈⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠁
⠀⠀⠛⢿⣿⣿⣿⣿⣿⣿⡿⠟
⠀⠀⠀⠀⠀⠉⠉⠉```'''
@bot.event
async def on_ready():
    print(" ")
    print(title)
    print('Successfully connected.')
    print('Bot:', bot.user.name)
    print('Bot ID:', bot.user.id)
    print("discord.py: Version:", discord.__version__)
    print('---------------------------')
    game = discord.Game(name=">help")
    await bot.change_presence(status=discord.Status.do_not_disturb, game=game)




@bot.command()
@commands.has_permissions(ban_members=True)
async def ban(ctx, member:discord.Member):
    """Bans User (Need Ban Permissions to use)."""
    await member.ban()
    await ctx.send(f":hammer: {member.mention} has been **banned**, goodbye!")


@bot.command()
async def help(ctx):
    embed = discord.Embed(title="XenoBot Commands", colour=discord.Colour(0xff18),
                          description="A basic list of XenoBot's commands")
    embed.set_thumbnail(url="https://i.imgur.com/dNZlpA8.jpg%22")
    embed.set_author(name="Giggl3z#3009", url="https://discordapp.com/", icon_url="https://i.imgur.com/oUbUJjO.jpg%22")
    embed.set_footer(text="Developed by: Giggl3z#3009", icon_url="https://i.imgur.com/oUbUJjO.jpg%22")

    embed.add_field(name="think", value="Thinking Emoji in ASCII.\n")
    embed.add_field(name="help", value="Shows this message.\n")
    embed.add_field(name="octosniff", value="Link for a PS4/PS3 IP sniffer.\n")
    embed.add_field(name="rules", value="tells user to follow rules.\n")
    embed.add_field(name="invite", value="Creates an invite link to this server.\n")
    embed.add_field(name="keemstar", value="IM YOUR HOST, KILLER KEEMSTAAR.\n")
    embed.add_field(name="think", value="ASCII Thinking Emoji :thinking:.\n")
    embed.add_field(name="rickroll", value="NEVER GONNA GIVE YOU UP.\n")
    embed.add_field(name="spaghet", value="SOMEBODY TOUCHA MY SPAGHET.\n")
    embed.add_field(name="biggay", value="'Big Gay' in ASCII Art.\n")
    embed.add_field(name="skid <mention>", value="Useless Insult to User.\n")
    embed.add_field(name="uinfo", value="Shows information of User.", inline=False)
    embed.add_field(name="warn", value="Warns User.", inline=False)
    await ctx.send(content="**List of Commands**", embed=embed)




@bot.command()
async def uinfo(ctx, member: discord.Member):
    """Says when a member joined."""
    await ctx.send(f'**{member.name}** joined on **{member.joined_at}**')
    await ctx.send(f'**{member.name}** created account on **{member.created_at}**')


@bot.command()
async def think(ctx):
    await ctx.send(thinkEmoji)

@bot.command()
@commands.has_permissions(administrator=True)
async def warn(ctx, member:discord.Member):
    await ctx.send(f"{member.mention} has been warned. If you continue with that behaviour, you may get kicked/banned.")


@bot.command()
@commands.has_permissions(kick_members=True)
async def kick(ctx, member:discord.Member):
    """Kicks User (Need Kick Permissions to use)."""
    await member.kick()
    await ctx.send(f":boot: **{member.name}** has been kicked goodbye!")


@bot.command()
@commands.has_permissions(administrator=True)
async def rules(ctx):
    """Links the server rules"""
    await ctx.send("Read **#rules** before doing anything stupid.")


@bot.command()
async def invite(ctx):
    """Sends Invite Link"""
    await ctx.send("**White Hat Hackers Invite Link:**")
    await ctx.send("https://discord.gg/Zus37hg")

@bot.command()
async def biggay(ctx):
    """"Big Gay" in ASCII Art"""
    await ctx.send(ascii)

@bot.command()
@commands.has_permissions(administrator=True)
async def skid(ctx, member:discord.Member):
    """>skid @user"""
    await ctx.send(f"Uh oh, SKID alert, WE GOT A SKID. All Welcome {member.mention}")

@bot.command()
async def spaghet(ctx):
    """Spaghet xD"""
    await ctx.send("SOMEBODY TOUCHA MY SPAGHET")
    await ctx.send("https://www.youtube.com/watch?v=cE1FrqheQNI")

@bot.command()
async def octosniff(ctx):
    """OctoSniff Link"""
    await ctx.send("Wanna sniff them packets on consoles? Download OctoSniff today for $10")
    await ctx.send("https://octosniff.net")

@bot.command()
async def rickroll(ctx):
    """Never Gonna Give You Up"""
    await ctx.send("You just got Rick Rolled! :joy:")
    await ctx.send("https://www.youtube.com/watch?v=dQw4w9WgXcQ")

@bot.command()
async def keemstar(ctx):
    """ITS YOUR HOST, KILLER KEEMSTAAAR"""
    await ctx.send("LEETS GET RIIIGHT, INTO THE NEEWS")
    await ctx.send("https://i.imgur.com/Ssf22e7.png")


bot.run('token')



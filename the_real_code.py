import asyncio
import os
import random
from datetime import datetime
import discord
from discord.commands import Option
from dotenv import load_dotenv

load_dotenv()
owner_id = int(os.getenv('OWNER_ID'))
token = str(os.getenv('TOKEN'))
bot = discord.Bot(intents=discord.Intents.all())


class Colors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    END = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


@bot.event
async def on_member_join(member):
    channel = bot.get_channel()#put your welcome channel id here
    await member.send(f"Hey buddy welcome to indigo park!")
    await channel.send(f'{member.mention}')
    embed = discord.Embed(title="Hey buddy!", description=f"{member.mention} just entered the park.")
    await channel.send(embed=embed)


@bot.event
async def on_member_remove(member):
    channel = bot.get_channel()#put your leave channel id here
    embed = discord.Embed(title="Cya buddy!", description=f"{member.mention} just left the park")
    await channel.send(embed=embed)


def now():
    raw_now = datetime.now()
    return raw_now.strftime('%X')


@bot.event
async def on_ready():
    print(f"{Colors.OKGREEN}[READY, {now()}]{Colors.END} Logged in successfully as "
          f"{Colors.BOLD}{bot.user}{Colors.END} with user id {owner_id}")


@bot.slash_command(name="indigo_park", description="Get the link to the game")
async def park(ctx):
    owner = await bot.fetch_user(985576431625076766)
    user = ctx.user.id
    await owner.send(f"Alert! A user <@{user}> has requested the game")
    await ctx.respond(f'Ok giving you the link to the game', ephemeral=True)
    await asyncio.sleep(2)
    await ctx.send(f'The link to the game is:')
    await asyncio.sleep(2)
    await ctx.send(f'https://store.steampowered.com/app/2504480?snr=5000_5100___primarylinks')


@bot.slash_command(name="indigo_park_ad", description="Get an ad for indigo park")
async def ad(ctx):
    owner = await bot.fetch_user(985576431625076766)
    user = ctx.user.id
    await owner.send(f"Alert! A user <@{user}> has requested a vintage ad")
    await owner.send("Alert! A user has requested a vintage ad")
    await ctx.respond(f'Ok giving you an ad for the park', ephemeral=True)
    await asyncio.sleep(2)
    await ctx.send(f"Hi there! I'm Rambley, Rambley the raccoon, "
                   f"and I'll be telling you about the best place on earth ")
    await asyncio.sleep(2)
    await ctx.send(f'INDIGO PARK')
    await asyncio.sleep(2)
    await ctx.send(f'At Indigo park we have mascots that are so life-like that you could mistake them for being alive')
    await asyncio.sleep(3)
    await ctx.send(f'Just visit our website, or call 1908-23414-INDIGO')


@bot.slash_command(name="talk_as_rambley", description="What would he say")
async def nuke(ctx,
               message: Option(str, "what message shall I send?")):
    owner = await bot.fetch_user(985576431625076766)
    user = ctx.user.id
    await owner.send(f"Alert! A user <@{user}> has talked as rambley with the message {message}")
    if len(message) > 2000:
        await ctx.respond(
            f"**Error:** due to Discord's api limits the character limit is 2000. Your message length:"
            f" {len(message)}", ephemeral=True)
        print(f"{Colors.FAIL}[ERROR, {now()}] Could not run /nuke command from {ctx.author} due to str length: "
              f"{len(message)}")
    print(f'{Colors.OKBLUE}[LOG, {now()}]{Colors.END} someone {ctx.user} is running nuke, {message}')
    await ctx.respond(f'ok he talks w/ message "{message}"', ephemeral=True)
    await ctx.send(f' {message}')


@bot.event
async def on_message(message):
    channel = bot.get_channel(1252115167790104578)
    rambley = 1244773437881454613
    randm = random.randint(1, 50)
    if randm == 1:
        print(f'{Colors.OKBLUE}[LOG, {now()}]{Colors.END} some is being responed to, by rambley')
        if message.author.id == rambley:
            return
        else:
            await channel.send("hey buddy")


@bot.slash_command(name="character_fave", description="rambley asks you a question, please only say the name")
async def fave_character(ctx):
    owner = await bot.fetch_user(985576431625076766)
    user = ctx.user.id
    await owner.send(f"Alert! A user <@{user}> has told rambley their favorite")
    await ctx.respond(f"Who is your favorite character")
    print(f'{Colors.OKBLUE}[LOG, {now()}]{Colors.END} someone {ctx.user} is running character_fave')
    name = await bot.wait_for('message', check=lambda message: message.author == ctx.author)
    if name.content.lower() == "lloyd":
        await ctx.send(f'Eww... Why')
    elif name.content.lower() == "mollie":
        await ctx.send(f'Mollie is such a good friend')
    elif name.content.lower() == "finnley":
        await ctx.send(f'I wish finnley was less shy, but whatever floats your boat')
    elif name.content.lower() == "rambley":
        await ctx.send(f'Thanks buddy I like me too')
    elif name.content.lower() == "salem":
        await ctx.send(f'ah yes salem')
    elif name.content.lower() == "ed":
        await ctx.send(f"ed? who's ed?")
    else:
        await ctx.send(f'who is that')


@bot.slash_command(name="summon", description="summon someone")
async def summon(ctx):
    owner = await bot.fetch_user(985576431625076766)
    user = ctx.user.id
    await owner.send(f"Alert! A user <@{user}> has summoned someone")
    await ctx.respond(f"Who shall I summon today, {str(ctx.author)}?")
    error = random.randint(1, 50)
    chance = random.randint(100, 10000)
    name = await bot.wait_for('message', check=lambda message: message.author == ctx.author)
    print(f"{Colors.OKBLUE}[LOG, {now()}]{Colors.END} {ctx.author} ran summon with name: {str(name.content)}")
    loc = ["Critter corner", "Rambley's railroad", "Mollie's landing pad", "Oceanic odyssey", "Mollies rooftop races",
           "Lloyd's main stage theatre"]
    if error < 3:
        await ctx.send(f"sorry there was an error summoning your {str(name.content)}")
        for i in range(1, 10):
            await ctx.send(f"{int(chance)} replacement {str(name.content)}s are on the way")
            chance = random.randint(2, 100000)
            await ctx.send("error")
    elif name.content.lower() == "rambley":
        await ctx.send(f'Hey buddy...')
        await asyncio.sleep(2)
        await ctx.send(f"I'm right here")
    else:
        loc = random.choice(loc)
        await ctx.send(f"{str(name.content)} has been summoned!")
        await ctx.send(f"They are located at {str(loc)}")


@bot.slash_command(name="where_are_bodies", description="ask Rambley were the bodies are")
async def bodies(ctx):
    owner = await bot.fetch_user(985576431625076766)
    user = ctx.user.id
    await owner.send(f"Alert! A user <@{user}> has asked about the bodies, they need to be taken out back  ")
    random_num = random.randint(1, 100)
    print(f"{Colors.OKBLUE}[LOG, {now()}]{Colors.END} {ctx.author} has attempted to find the bodies {random_num}")
    await ctx.respond(f'ah the bodies I know where they are')
    await asyncio.sleep(4)
    if random_num == 1:
        await ctx.send(f'under the railroad')
    else:
        await ctx.send(f'graveyards')


@bot.slash_command(name="credits")
async def sex(ctx):
    print(f"{Colors.OKBLUE}[LOG, {now()}]{Colors.END} {ctx.author} has looked at the credits    `")
    await ctx.respond(f'ok giving you the credits', ephemeral=True)
    await asyncio.sleep(2)
    await ctx.send(f'Bot development: bobler6')
    await asyncio.sleep(2)
    await ctx.send(f'Bot development assistance: wgrav')
    await asyncio.sleep(2)
    await ctx.send(f'Indigo park and rambley by Unique Geese')
    await asyncio.sleep(2)
    await ctx.send(f'Beta testers: IMDHI, Meepx13, the_real_rambley. irishman702, NASA_kid, xavier1228, and Xenexodus')
    await asyncio.sleep(2)
    await ctx.send(f'NOTE, the bot is still in beta')

bot.run(token)

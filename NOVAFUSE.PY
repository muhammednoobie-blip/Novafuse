import discord # type: ignore
from discord.ext import commands # type: ignore
from mcrcon import MCRcon # type: ignore

TOKEN = "MTQ3NjI3MTQxMDA2MTExNTU2Mg.GnHWMs.UWcTa-1EbKhC6mbCXEJb8vQDXHaEq4sChIJOOE"

# Minecraft server RCON info
RCON_HOST = "YOUR_SERVER_IP"
RCON_PORT = 25575
RCON_PASSWORD = "YOUR_RCON_PASSWORD"

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

# -----------------------------
# BOT READY
# -----------------------------
@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")

# -----------------------------
# CHECK ONLINE PLAYERS
# -----------------------------
@bot.command()
async def online(ctx):
    try:
        with MCRcon(RCON_HOST, RCON_PASSWORD, port=RCON_PORT) as mcr:
            response = mcr.command("list")
        await ctx.send(f"**Online Players:** {response}")
    except:
        await ctx.send("Server offline or RCON not configured.")

# -----------------------------
# WHITELIST COMMAND
# -----------------------------
@bot.command()
async def whitelist(ctx, player: str):
    try:
        with MCRcon(RCON_HOST, RCON_PASSWORD, port=RCON_PORT) as mcr:
            mcr.command(f"whitelist add {player}")
        await ctx.send(f"Added **{player}** to the whitelist.")
    except:
        await ctx.send("Failed to whitelist player.")

# -----------------------------
# SERVER STATUS
# -----------------------------
@bot.command()
async def status(ctx):
    try:
        with MCRcon(RCON_HOST, RCON_PASSWORD, port=RCON_PORT) as mcr:
            response = mcr.command("list")
        await ctx.send("Server is **online**.")
    except:
        await ctx.send("Server is **offline**.")
@bot.command()
async def ping(ctx):
    await ctx.send("bot is online")
@bot.command()
async def rules(ctx):
    rules = """📜 General Rules 📜
No hack clients, Freecam, Minimap and other stuff
No griefing spawn or making traps in or near spawn
No alt accounts
If you report, you need to give proof (screenshots or video proof)
AFK killing is bannable.
Players must play daily or have a reasonable excuse to not play. (EX: Being busy with a task)

⚔️ Base Combat Rules ⚔️
If you use /spawn, that's an immediate ban (Basically no combat logging at ALL)
Any form of abuse is strictly prohibited (including bug abusing)
No long water fights, Short water fights are ok.
Tier 2 pots are NOT Allowed
Don't abuse techs
Don't stay in login for 30 seconds or more.

---- Server Rules ----
Do NOT ping Admin or Founder, it will result in a timeout.
No insults.
No swears or slurs.
Use common sense, if something feels wrong to say or do, don't do it.
NO NSFW.
Light Racism as a joke is allowed, don't make it go too far though.
Must be 13+"""
    await ctx.send(rules)
@bot.command()
async def ip(ctx):
    await ctx.send("The SMP IP will be announced soon!(march 14 possibly)")    
@bot.command()
async def info(ctx):
    embed = discord.Embed(
        title="SMP Information",
        description="Everything you need to know about the server.",
        color=discord.Color.blue()
    )
    embed.add_field(name="Status", value="Coming soon...", inline=False)
    embed.add_field(name="IP", value="To be announced", inline=False)
    embed.set_footer(text="SMP Bot by muhammed")

    await ctx.send(embed=embed)
bot.run(TOKEN)
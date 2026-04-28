import discord
from discord.ext import commands
import random
import datetime

# 🔑 Put your bot token here
TOKEN = "YOUR_BOT_TOKEN_HERE"

# ---------------- INTENTS ----------------
intents = discord.Intents.default()
intents.message_content = True
intents.members = True

# ---------------- BOT SETUP ----------------
bot = commands.Bot(
    command_prefix=["!", "?"],  # supports ! and ?
    intents=intents
)

# ---------------- READY EVENT ----------------
@bot.event
async def on_ready():
    await bot.tree.sync()  # sync slash commands
    print(f"✅ Logged in as {bot.user}")
    print("✅ Slash commands synced")

# ---------------- ERROR HANDLER ----------------
@bot.event
async def on_command_error(ctx, error):
    await ctx.send(f"❌ Error: {str(error)}")

# ---------------- CORE COMMANDS ----------------

@bot.hybrid_command(name="ping", description="Check bot latency")
async def ping(ctx):
    await ctx.send(f"🏓 Pong! `{round(bot.latency * 1000)}ms`")

@bot.hybrid_command(name="coin", description="Flip a coin")
async def coin(ctx):
    await ctx.send(f"🪙 {random.choice(['Heads', 'Tails'])}")

@bot.hybrid_command(name="rand", description="Random number generator")
async def rand(ctx, min_num: int = 1, max_num: int = 100):
    await ctx.send(f"🎲 {random.randint(min_num, max_num)}")

@bot.hybrid_command(name="roll", description="Roll a dice")
async def roll(ctx, sides: int = 6):
    await ctx.send(f"🎲 You rolled: {random.randint(1, sides)}")

@bot.hybrid_command(name="say", description="Bot repeats your message")
async def say(ctx, *, text: str):
    await ctx.send(text)

# ---------------- FUN COMMANDS ----------------

@bot.hybrid_command(name="joke", description="Random joke")
async def joke(ctx):
    jokes = [
        "Why did the computer crash? It had too many tabs open.",
        "I told my code a joke… it didn’t compile.",
        "Why do programmers hate nature? Too many bugs."
    ]
    await ctx.send(random.choice(jokes))

@bot.hybrid_command(name="8ball", description="Magic 8-ball")
async def eightball(ctx, *, question: str):
    answers = [
        "Yes 👍",
        "No 👎",
        "Maybe 🤔",
        "Definitely!",
        "Ask again later ⏳",
        "Absolutely not"
    ]
    await ctx.send(f"🎱 Question: {question}\nAnswer: {random.choice(answers)}")

# ---------------- INFO COMMANDS ----------------

@bot.hybrid_command(name="avatar", description="Get user avatar")
async def avatar(ctx, member: discord.Member = None):
    member = member or ctx.author
    await ctx.send(member.avatar.url)

@bot.hybrid_command(name="userinfo", description="User info")
async def userinfo(ctx, member: discord.Member = None):
    member = member or ctx.author

    embed = discord.Embed(title="👤 User Info", color=discord.Color.blue())
    embed.add_field(name="Name", value=member.name, inline=True)
    embed.add_field(name="ID", value=member.id, inline=True)
    embed.add_field(
        name="Joined Server",
        value=member.joined_at.strftime("%Y-%m-%d") if member.joined_at else "Unknown",
        inline=False
    )
    await ctx.send(embed=embed)

@bot.hybrid_command(name="serverinfo", description="Server information")
async def serverinfo(ctx):
    guild = ctx.guild

    embed = discord.Embed(title="🏠 Server Info", color=discord.Color.green())
    embed.add_field(name="Server Name", value=guild.name, inline=True)
    embed.add_field(name="Members", value=guild.member_count, inline=True)
    embed.add_field(name="Created", value=guild.created_at.strftime("%Y-%m-%d"), inline=False)

    await ctx.send(embed=embed)

# ---------------- MODERATION ----------------

@bot.hybrid_command(name="clear", description="Delete messages (admin only)")
@commands.has_permissions(manage_messages=True)
async def clear(ctx, amount: int = 5):
    await ctx.channel.purge(limit=amount + 1)
    await ctx.send(f"🧹 Deleted {amount} messages", delete_after=3)

# ---------------- RUN BOT ----------------
bot.run(TOKEN)

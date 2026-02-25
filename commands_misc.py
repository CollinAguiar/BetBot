import discord
from bot_config import bot
from economy import users, get_user
from bets import bets_data
from discord.ext import commands

@bot.tree.command(name="leaderboard", description="Shows top balances in the server")
async def leaderboard(interaction: discord.Interaction):
    top = sorted(users.items(), key=lambda x:x[1]["balance"], reverse=True)[:10]
    embed = discord.Embed(title="Leaderboard - Top Balances", color=discord.Color.purple())
    for i, (uid, data) in enumerate(top,1):
        member = interaction.guild.get_member(int(uid))
        name = member.display_name if member else f"User {uid}"
        embed.add_field(name=f"{i}. {name}", value=f"{data['balance']} coins", inline=False)
    embed.timestamp = discord.utils.utcnow()
    await interaction.response.send_message(embed=embed)

@bot.tree.command(name="activebets", description="Shows all currently active bets")
async def activebets(interaction: discord.Interaction):
    active = [f"ID {bid}: {data['name']}" for bid,data in bets_data["bets"].items() if not data["resolved"]]
    if not active:
        embed = discord.Embed(description="No active bets.", color=discord.Color.dark_gray())
    else:
        embed = discord.Embed(title="Active Bets", description="\n".join(active), color=discord.Color.blue())
    embed.timestamp = discord.utils.utcnow()
    await interaction.response.send_message(embed=embed)

@bot.tree.command(name="brokemeter", description="Shows how many times a user hit 0 coins")
async def brokemeter(interaction: discord.Interaction, member: discord.Member):
    user = get_user(member.id)
    count = user.get("times_broke",0)
    embed = discord.Embed(title=f"{member.display_name} Broke Meter", description=f"{member.mention} has hit 0 coins {count} times", color=discord.Color.orange())
    await interaction.response.send_message(embed=embed)

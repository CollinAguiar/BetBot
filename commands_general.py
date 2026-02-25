import discord
from discord.ext import commands
from economy import get_user

@bot.tree.command(name="help", description="Shows all commands")
async def help_command(interaction: discord.Interaction):
    embed = discord.Embed(title="Commands", color=discord.Color.blue())
    embed.description = (
        "/createbet [name] [Option 1, Option 2, Option 3 ...]\n"
        "/bet [id] [option number] [amount]\n"
        "/resolvebet [id] [correct_option_number]\n"
        "/balance [@user]\n"
        "/daily\n"
        "/activebets\n"
        "/leaderboard\n"
        "/brokemeter [@user]\n"
    )
    await interaction.response.send_message(embed=embed)

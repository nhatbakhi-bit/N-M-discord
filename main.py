import discord
from discord import app_commands
from discord.ext import commands
import random

intents = discord.Intents.default()
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    await bot.tree.sync()
    print("Bot đã online!")

@bot.tree.command(name="taixiu", description="Chơi xúc xắc bằng điểm ảo")
async def taixiu(interaction: discord.Interaction):
    dice = [random.randint(1, 6) for _ in range(3)]
    total = sum(dice)
    result = "TÀI" if total >= 11 else "XỈU"

    await interaction.response.send_message(
        f"🎲 Kết quả: {dice}\n"
        f"Tổng: {total}\n"
        f"Kết quả: **{result}**"
    )

bot.run("MTU2NjMzMzM5NzcwMDQ1MjM3Mg.GSmxSG.KpNeYizKi4NlsTuYKt5K9XIb1sfPQa1Alfiofw")

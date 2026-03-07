import discord
from discord.ext import commands
import os

# هيروح يدور على التوكن في Variables بتاعة Railway
TOKEN = os.getenv("DISCORD_TOKEN") 

VERIFIED_ROLE_NAME = "Member"

class VerifyView(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)

    @discord.ui.button(label="Verify", style=discord.ButtonStyle.green, custom_id="verify_button_unique_id")
    async def verify_button(self, interaction: discord.Interaction, button: discord.ui.Button):
        guild = interaction.guild
        member = interaction.user
        role = discord.utils.get(guild.roles, name=VERIFIED_ROLE_NAME)

        if not role:
            await interaction.response.send_message("Role not found! Please contact admin.", ephemeral=True)
            return

        if role in member.roles:
            await interaction.response.send_message("You are already verified!", ephemeral=True)
            return

        await member.add_roles(role)
        await interaction.response.send_message("You are now verified. Welcome to the server!", ephemeral=True)

class MyBot(commands.Bot):
    def __init__(self):
        intents = discord.Intents.default()
        intents.members = True
        intents.message_content = True
        super().__init__(command_prefix="!", intents=intents)

    async def setup_hook(self):
        self.add_view(VerifyView())

bot = MyBot()

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")
    print("------")

@bot.command()
@commands.has_permissions(administrator=True)
async def rules(ctx):
    embed = discord.Embed(
        title=f"Welcome to {ctx.guild.name}!",
        description=f"""
Hey, welcome to **{ctx.guild.name}**!

We’re a friendly, active, and fun-loving community focused on positivity, enjoying the game, and supporting each other in a vibrant, chill environment!

**Be Civil**
We encourage respectful conversation. Cursing is allowed, but it shouldn’t be aimed at insulting others. Hate speech, including racism, sexism, and homophobia, is strictly prohibited. Please refrain from meme spamming.

**No NSFW Content**
Any NSFW material, including pornography and gore, is not allowed on this server.

**No Drama**
Keep personal or sensitive topics, as well as any drama, out of the main chat. Please handle these discussions via DMs.

**Keep the Chat English**
To ensure everyone can participate, please communicate in English.

**Use Common Sense**
If you're posting flickering images or anything that may be unsettling, please use spoilers and include a warning!

**Don’t Get Banned**
Violating these rules could result in a ban.

**Match Your Discord Name with Your In-Game Name**
Make sure your Discord name matches your in-game name. If we can't identify you, you may be removed.


*Let’s create a fun and friendly environment for everyone!*
""",
        color=discord.Color.green()
    )
    
    await ctx.send(embed=embed, view=VerifyView())

bot.run(TOKEN)

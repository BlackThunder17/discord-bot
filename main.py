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

*Change your name on the server to your name in the game.*

*Let’s create a fun and friendly environment for everyone!*
""",
        color=discord.Color.green()
    )
    
    await ctx.send(embed=embed, view=VerifyView())

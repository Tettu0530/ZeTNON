# Import General Package
import asyncio

# Import Discord Package
import discord
from discord import app_commands
from discord.ext import commands

class CleanConfirmButtonView(discord.ui.View):
    def __init__(self, bot: commands.Bot):
        super().__init__(timeout=None)

    @discord.ui.button(label="ð¥æ¶å» | CLEAN", style=discord.ButtonStyle.danger, custom_id="persistent_view:btn_clanallow")
    async def callback_cleanallow(self, button: discord.ui.Button, interaction: discord.Interaction):
        await button.channel.purge(limit=1000)
        embed_cleaned = discord.Embed(
            title="â Success - Clean", description="æ­£å¸¸ã«ãã£ã³ãã«ã­ã°ãæ¶å»ãã¾ããã\nãã®ã¡ãã»ã¼ã¸ã¯10ç§å¾ã«æ¶å»ããã¾ã", color=0x00ff00)
        embed_cleaned.set_footer(text="Status - 200 | Made by Tettu0530#0530",
                                 icon_url="https://cdn.discordapp.com/avatars/941871491337814056/fb276cd1dc430e643f233594564e0559.webp?size=128")
        i = await button.channel.send(embed=embed_cleaned)
        await asyncio.sleep(10)
        await i.delete()

    @discord.ui.button(label="âã­ã£ã³ã»ã« | CANCEL", style=discord.ButtonStyle.primary, custom_id="persistent_view:btn_cleandeny")
    async def callback_cleandeny(self, button: discord.ui.Button, interaction: discord.Interaction):
        await button.message.delete()

    
class CleanCog(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot: commands.Bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print("[COGS]CleanSlashCog on ready.")

    @app_commands.command(
        name="clean",
        description="ãã£ã³ãã«ã­ã°ãå¨æ¶å»ãã¾ã"
    )
    async def clean(self, interaction: discord.Interaction):
        if interaction.user.guild_permissions.administrator:
            embed = discord.Embed(title="â ç¢ºèª | Confirm", description="æ¬å½ã«ãã£ã³ãã«ã­ã°ãæ¶å»ãã¾ããï¼\n**æ¶å»ãæ¼ããå¾æä½ã¯åãæ¶ãã¾ãã**", color=0xffff00)
            embed.set_footer(text="Status - 200 | Made by Tettu0530#0530",
                                     icon_url="https://cdn.discordapp.com/avatars/941871491337814056/fb276cd1dc430e643f233594564e0559.webp?size=128")
            await interaction.response.send_message("æ¬å½ã«ãã£ã³ãã«ã­ã°ãæ¶å»ãã¾ããï¼", view=CleanConfirmButtonView(bot=self.bot))

async def setup(bot: commands.Bot):
    await bot.add_cog(CleanCog(bot))
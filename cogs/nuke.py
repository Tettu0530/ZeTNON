# Import General Package
import asyncio
import datetime
import pytz

# Import Discord Package
import discord
from discord import app_commands
from discord.ext import commands


class NukeConfirmButtonView(discord.ui.View):
    def __init__(self, bot: commands.Bot):
        super().__init__(timeout=None)
        self.bot = bot

    @discord.ui.button(label="ð¥æ¶å» | NUKE", style=discord.ButtonStyle.danger, custom_id="persistent_view:btn_nukeallow")
    async def callback_nukeallow(self, button: discord.ui.Button, interaction: discord.Interaction):
        if button.user.guild_permissions.manage_messages:
            try:
                if button.channel.topic is None:
                    topic = None
                else:
                    topic = button.channel.topic
                newch = await button.channel.category.create_text_channel(name=button.channel.name, position=button.channel.position, overwrites=button.channel.overwrites, topic=topic)
                await button.channel.delete()
                embed_cleaned = discord.Embed(
                    title="â Success - Nuke", description="æ­£å¸¸ã«ãã£ã³ãã«ã­ã°ãæ¶å»ãã¾ããã\nãã®ã¡ãã»ã¼ã¸ã¯10ç§å¾ã«æ¶å»ããã¾ã", color=0x00ff00)
                embed_cleaned.set_footer(text="Status - 200 | Made by Tettu0530#0530",
                                         icon_url="https://cdn.discordapp.com/avatars/941871491337814056/fb276cd1dc430e643f233594564e0559.webp?size=128")
                i = await newch.send(embed=embed_cleaned)
                await asyncio.sleep(10)
                await i.delete()
            except:
                if button.channel.topic is None:
                    topic = None
                else:
                    topic = button.channel.topic
                newch = await button.guild.create_text_channel(name=button.channel.name, position=button.channel.position, overwrites=button.channel.overwrites, topic=topic)
                await button.channel.delete()
                embed_cleaned = discord.Embed(
                    title="â Success - Nuke", description="æ­£å¸¸ã«ãã£ã³ãã«ã­ã°ãæ¶å»ãã¾ããã\nãã®ã¡ãã»ã¼ã¸ã¯10ç§å¾ã«æ¶å»ããã¾ã", color=0x00ff00)
                embed_cleaned.set_footer(text="Status - 200 | Made by Tettu0530#0530",
                                         icon_url="https://cdn.discordapp.com/avatars/941871491337814056/fb276cd1dc430e643f233594564e0559.webp?size=128")
                i = await newch.send(embed=embed_cleaned)
                await asyncio.sleep(10)
                await i.delete()
            print(f"[{datetime.datetime.now(tz=pytz.timezone('Asia/Tokyo')).strftime('%Y/%m/%d %H:%M:%S')}]{button.user.name}(ID:{button.user.id})ãnukeã³ãã³ãããµã¼ãã¼:{str(button.guild_id)}ã§ä½¿ç¨ãã¾ããã")

    @discord.ui.button(label="âã­ã£ã³ã»ã« | CANCEL", style=discord.ButtonStyle.primary, custom_id="persistent_view:btn_nukedeny")
    async def callback_nukedeny(self, button: discord.ui.Button, interaction: discord.Interaction):
        await button.message.delete()


class NukeCog(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot: commands.Bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print("[COGS]NukeSlashCog on ready.")

    @app_commands.command(
        name="nuke",
        description="ãã£ã³ãã«ã­ã°ãå¨æ¶å»ãã¾ã(Botãªã©ããã£ã³ãã«ã«ç»é²ãã¦ããå ´åã¯/cleanãä½¿ç¨ãã¦ãã ãã)"
    )
    async def nuke(self, interaction: discord.Interaction):
        if interaction.user.guild_permissions.administrator:
            embed = discord.Embed(title="â ç¢ºèª | Confirm", description="æ¬å½ã«ãã£ã³ãã«ã­ã°ãæ¶å»ãã¾ããï¼\n**æ¶å»ãæ¼ããå¾æä½ã¯åãæ¶ãã¾ãã**\n(**BotãWebHookãªã©ãç»é²ãã¦ããå ´åã¯`/clean`ãä½¿ããã¨ãå¼·ãæ¨å¥¨ãã¾ã**)", color=0xffff00)
            embed.set_footer(text="Status - 200 | Made by Tettu0530#0530",
                                     icon_url="https://cdn.discordapp.com/avatars/941871491337814056/fb276cd1dc430e643f233594564e0559.webp?size=128")
            await interaction.response.send_message(embed=embed, view=NukeConfirmButtonView(bot=self.bot))

async def setup(bot: commands.Bot):
    await bot.add_cog(NukeCog(bot))
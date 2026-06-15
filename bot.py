"""
🤖 Bot do Discord em Python
Um bot moderno e escalável para Discord, construído com discord.py.

Como usar:
1. Crie um arquivo .env com base no .env.example
2. Instale as dependências: pip install -r requirements.txt
3. Execute: python bot.py
"""

import os
import discord
from discord.ext import commands
from dotenv import load_dotenv

# Carrega variáveis de ambiente do arquivo .env
load_dotenv()

# Configurações do bot
TOKEN = os.getenv("DISCORD_TOKEN")
PREFIX = os.getenv("BOT_PREFIX", "!")

# Intents necessários para o bot funcionar corretamente
intents = discord.Intents.default()
intents.message_content = True  # Necessário para ler conteúdo das mensagens
intents.members = True  # Necessário para acessar informações de membros

# Cria a instância do bot
bot = commands.Bot(command_prefix=PREFIX, intents=intents)


@bot.event
async def on_ready():
    """Evento chamado quando o bot está pronto e conectado."""
    print(f"✅ Bot conectado como {bot.user.name}")
    print(f"🆔 ID: {bot.user.id}")
    print(f"📊 Conectado em {len(bot.guilds)} servidor(es)")
    await bot.change_presence(
        activity=discord.Activity(type=discord.ActivityType.listening, name=f"{PREFIX}help")
    )


@bot.event
async def on_command_error(ctx: commands.Context, error):
    """Manipulador de erros global para comandos."""
    if isinstance(error, commands.CommandNotFound):
        return  # Ignora comandos não encontrados
    elif isinstance(error, commands.MissingPermissions):
        await ctx.send("❌ Você não tem permissão para usar este comando.")
    elif isinstance(error, commands.MissingRequiredArgument):
        await ctx.send(f"⚠️ Argumento faltando: `{error.param.name}`")
    else:
        await ctx.send(f"❌ Ocorreu um erro: `{error}`")


# ========== COMANDOS BÁSICOS ==========

@bot.command(name="ping")
async def ping(ctx: commands.Context):
    """Verifica a latência do bot."""
    latency = round(bot.latency * 1000)
    await ctx.send(f"🏓 Pong! Latência: `{latency}ms`")


@bot.command(name="info")
async def info(ctx: commands.Context):
    """Mostra informações sobre o bot."""
    embed = discord.Embed(
        title="🤖 Informações do Bot",
        description="Bot moderno e escalável em Python",
        color=discord.Color.blue()
    )
    embed.add_field(name="📚 Biblioteca", value="discord.py v2.x", inline=True)
    embed.add_field(name="🔗 Prefixo", value=f"`{PREFIX}`", inline=True)
    embed.add_field(name="🛠️ Comandos", value=f"`{len(bot.commands)}`", inline=True)
    embed.add_field(name="📊 Servidores", value=f"`{len(bot.guilds)}`", inline=True)
    embed.set_footer(text=f"Solicitado por {ctx.author}", icon_url=ctx.author.avatar.url if ctx.author.avatar else None)
    
    await ctx.send(embed=embed)


@bot.command(name="serverinfo")
async def serverinfo(ctx: commands.Context):
    """Mostra informações do servidor."""
    guild = ctx.guild
    embed = discord.Embed(title=f"📋 {guild.name}", color=discord.Color.green())
    
    if guild.icon:
        embed.set_thumbnail(url=guild.icon.url)
    
    embed.add_field(name="👑 Dono", value=guild.owner.mention if guild.owner else "N/A", inline=True)
    embed.add_field(name="👥 Membros", value=guild.member_count, inline=True)
    embed.add_field(name="🎭 Cargos", value=len(guild.roles), inline=True)
    embed.add_field(name="💬 Canais", value=len(guild.channels), inline=True)
    embed.add_field(name="📅 Criado em", value=guild.created_at.strftime("%d/%m/%Y"), inline=True)
    
    await ctx.send(embed=embed)


@bot.command(name="help")
async def custom_help(ctx: commands.Context):
    """Lista todos os comandos disponíveis."""
    embed = discord.Embed(
        title="📖 Comandos Disponíveis",
        description=f"Use `{PREFIX}comando` para executar um comando",
        color=discord.Color.purple()
    )
    
    embed.add_field(
        name="🔧 Utilidades",
        value=f"`{PREFIX}ping` - Verifica a latência\n"
              f"`{PREFIX}info` - Informações do bot\n"
              f"`{PREFIX}serverinfo` - Informações do servidor",
        inline=False
    )
    
    await ctx.send(embed=embed)


# Rodar o bot
if __name__ == "__main__":
    if not TOKEN:
        print("❌ ERRO: Token do Discord não encontrado!")
        print("💡 Crie um arquivo .env com base no .env.example")
        exit(1)
    
    print("🚀 Iniciando o bot...")
    bot.run(TOKEN)

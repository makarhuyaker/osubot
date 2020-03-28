import discord
from discord.ext import commands
import inspect
import asyncio
import random
import os
import json
from datetime import datetime

Bot = commands.Bot(command_prefix="osu!")
Bot.remove_command("help")

@Bot.event
async def on_ready():
    print(f"{Bot.user} workk!")

@Bot.command(pass_context= True)
async def help(ctx):
    emb = discord.Embed(color=0xf90aff, description="<a:osivisualizer:688403122523209731>Привет я osu!bot бот с кучей команд вот и они:\n Комманды модерации\n `mute` Выдает мут нужны права изменение ролей\n`unmute` Снимает мут с участника нужны права изменение ролей\n `ban` Банит участника права для роли банить участников\n `lock` Выдает роль блокировки права упраление каналами\n `unlock` Снимает блокировку права для роли изменять каналы\n `kick` Кикает участника права для роли кикать участников\n `createblockroom` Создает каналы для заблокированных\n Простые комманды\n `8ball` Обычный шар\n `minesweper` Сапер в дискорде\n `say` Сказать что то через бота\n `info` Информация о боте\n `report` Отправить баг репорт\n `updates` Обновления бота\n Команды создателя\n `crd` Перезапуск cogs\n `shutdown` Отключение бота\n `eval` Выполнение строк кода")
    emb.set_footer(text="osu!bot copyright 2020-2020", icon_url="https://media.discordapp.net/attachments/675294482991808513/687743226102546545/lazer.png?width=585&height=585")
    await ctx.send(embed = emb)

owners_bot = [521313537943928852, 466310620132802583, 639144156123365386, 477733320583544838]
def you_user(ctx):
    return ctx.message.author.id in owners_bot
    
@Bot.command(name='eval', aliases=["e", "vzlomjopi", "durka"], pass_context=True)
@commands.check(you_user)
async def eval_(ctx, *, command):
    res = eval(command)
    if inspect.isawaitable(res):
        await ctx.send(await res)
    else:
        await ctx.send(res)   

@Bot.command(pass_context= True)
@commands.has_permissions(kick_members=True)
async def kick(ctx, member:discord.Member = None):
    if not member:
        emb = discord.Embed(color=0xf90aff, title = "osu!kick", description="**Укажите кого надо кикнуть!<:redTick:596576672149667840>**")
        emb.set_footer(text="osu!bot Copyright 2020-2020", icon_url="https://media.discordapp.net/attachments/675294482991808513/687743226102546545/lazer.png?width=585&height=585")
        await ctx.send(embed = emb)
        return
    await member.kick()
    emb = discord.Embed(color=0xf90aff, title = "osu!kick", description=f"{member.mention} **Был кикнут!<:greenTick:596576670815879169>**")
    emb.set_footer(text="osu!bot Copyright 2020-2020", icon_url="https://media.discordapp.net/attachments/675294482991808513/687743226102546545/lazer.png?width=585&height=585")
    await ctx.send(embed = emb)

@kick.error
async def kick_error(ctx, error):
    if isinstance(error, commands.CheckFailure):
      emb = discord.Embed(color=0xf90aff, title = "osu!kick", description="**Ты не можешь использовать эту комманду<:redTick:596576672149667840>**")
      emb.set_footer(text="osu!bot Copyright 2020-2020", icon_url="https://media.discordapp.net/attachments/675294482991808513/687743226102546545/lazer.png?width=585&height=585")
      await ctx.send(embed = emb)

@Bot.command(pass_context= True)
@commands.has_permissions(manage_roles=True)
async def mute(ctx, member: discord.Member=None):
    if not member:
        emb = discord.Embed(color=0xf90aff, title = "osu!mute", description="**Укажите кого надо замутить!<:redTick:596576672149667840>**")
        emb.set_footer(text="osu!bot Copyright 2020-2020", icon_url="https://media.discordapp.net/attachments/675294482991808513/687743226102546545/lazer.png?width=585&height=585")
        await ctx.send(embed = emb)
        return
    emb = discord.Embed(color=0xf90aff, title = "osu!mute", description=f"{member.mention} **Был замучен!<:greenTick:596576670815879169>**")
    emb.set_footer(text="osu!bot Copyright 2020-2020", icon_url="https://media.discordapp.net/attachments/675294482991808513/687743226102546545/lazer.png?width=585&height=585")
    await ctx.send(embed = emb)
    role = discord.utils.get(ctx.guild.roles, name="Muted")
    await member.add_roles(role)

@mute.error
async def mute_error(ctx, error):
    if isinstance(error, commands.CheckFailure):
        emb = discord.Embed(color=0xf90aff, title = "osu!mute", description="**Ты не можешь замутить этого пользователя!<:redTick:596576672149667840>**")
        emb.set_footer(text="osu!bot Copyright 2020-2020", icon_url="https://media.discordapp.net/attachments/675294482991808513/687743226102546545/lazer.png?width=585&height=585")
        await ctx.send(embed = emb)
 
@Bot.command(pass_context= True)
@commands.has_permissions(manage_roles=True)
async def unmute(ctx, member: discord.Member=None):
    if not member:
        emb = discord.Embed(color=0xf90aff, title = "osu!unmute", description="**Укажите кого надо размутить!<:redTick:596576672149667840>**")
        emb.set_footer(text="osu!bot Copyright 2020-2020", icon_url="https://media.discordapp.net/attachments/675294482991808513/687743226102546545/lazer.png?width=585&height=585")
        await ctx.send(embed = emb)
        return
    emb = discord.Embed(color=0xf90aff, title = "osu!unmute", description=f"{member.mention} **Был размучен!<:greenTick:596576670815879169>**")
    emb.set_footer(text="osu!bot Copyright 2020-2020", icon_url="https://media.discordapp.net/attachments/675294482991808513/687743226102546545/lazer.png?width=585&height=585")
    await ctx.send(embed = emb)    
    role = discord.utils.get(ctx.guild.roles, name="Muted")
    await member.remove_roles(role)

@mute.error
async def unmute_error(ctx, error):
    if isinstance(error, commands.CheckFailure):
        emb = discord.Embed(color=0xf90aff, title = "osu!unmute", description="**Ты не можешь размутить этого пользователя!<:redTick:596576672149667840>**")
        emb.set_footer(text="osu!bot Copyright 2020-2020", icon_url="https://media.discordapp.net/attachments/675294482991808513/687743226102546545/lazer.png?width=585&height=585")
        await ctx.send(embed = emb)
        
@Bot.command(pass_context= True)
@commands.has_permissions(administrator=True)
async def ban(ctx, member:discord.Member = None):
    if not member:
        emb = discord.Embed(color=0xf90aff, title = "osu!ban", description="Укажите кого надо **забанить!**<:redTick:596576672149667840>")
        emb.set_footer(text="osu!bot Copyright 2020-2020", icon_url="https://media.discordapp.net/attachments/675294482991808513/687743226102546545/lazer.png?width=585&height=585")
        await ctx.send(embed = emb)
        return
    await member.ban()
    emb = discord.Embed(color=0xf90aff, title = "osu!ban", description=f"{member.mention} Был **забанен!**<:greenTick:596576670815879169>**")
    emb.set_footer(text="osu!bot Copyright 2020-2020", icon_url="https://media.discordapp.net/attachments/675294482991808513/687743226102546545/lazer.png?width=585&height=585")
    await ctx.send(embed = emb)

@ban.error
async def ban_error(ctx, error):
    if isinstance(error, commands.CheckFailure):
      emb = discord.Embed(color=0xf90aff, title = "osu!ban", description="**Ты не **можешь использовать** эту комманду<:redTick:596576672149667840>**")
      emb.set_footer(text="osu!bot Copyright 2020-2020", icon_url="https://media.discordapp.net/attachments/675294482991808513/687743226102546545/lazer.png?width=585&height=585")
      await ctx.send(embed = emb)

@Bot.command(pass_context= True)
async def invite(ctx):
    emb = discord.Embed(color=0xf90aff, title = "osu!invite", description="[Пригласить бота!](https://discordapp.com/oauth2/authorize?client_id=684136563017515038&scope=bot&permissions=66186303)")
    emb.set_footer(text="osu!bot copyright 2020-2020", icon_url="https://media.discordapp.net/attachments/675294482991808513/687743226102546545/lazer.png?width=585&height=585")
    await ctx.send(embed = emb)

@Bot.command(name='8ball', pass_context= True)
async def lox(ctx, arg):
        if arg != '':
            messages = ['Да.', 'Нет.', 'Ага!', 'Ну, наверно!', 'Конечно, нет!', 'Спроси позже!', 'Неа, не буду отвечать)0)0)). 😎']
            kv1 = int(len(messages))
            messages_output = messages.pop(random.randint(0, kv1 - 1))
            await ctx.send(f'{messages_output}')

@Bot.command(name= 'updates', pass_context=True)
async def hui(ctx):
    emb = discord.Embed(color=0xf90aff, title = "osu!updates", description="** <:toker:685203815288275106>Обновления бота: Бот релизнут <:sanitar:678951482506346496>**")
    emb.set_footer(text="osu!bot Copyright 2020-2020", icon_url="https://media.discordapp.net/attachments/675294482991808513/687743226102546545/lazer.png?width=585&height=585")
    await ctx.send(embed = emb)

@Bot.command()
async def say(ctx, *, msg):
    await ctx.message.delete()
    embed = discord.Embed(
        title = "<a:osuvisualizer:688403122523209731>Кто-то что-то сказал...",
        color=0xf90aff, description = "{}" .format(msg)
    )
    await ctx.send(embed = embed)

initial_extensions = ['status', 'minesweeper', 'inter','osu'] 

def reloader(ctx):
    for extension in initial_extensions:
        Bot.unload_extension(extension)
        Bot.load_extension(extension)

@Bot.command(pass_context=True)
@commands.check(you_user)
async def crd(ctx):
    try:
        if __name__ == '__main__':
            reloader(ctx)
            await ctx.send(f"{ctx.author.mention}, перезагрузка завершена!")
    except Exception as errrrr:
        await ctx.send(f"{ctx.author.mention}, не удалось перезагрузить! `Error: {errrrr}`")

if __name__ == '__main__':
    for extension in initial_extensions:
        Bot.load_extension(extension)  

@Bot.command(pass_context= True)
async def report(ctx, *args):
    mesg1 = ' '.join(args)
    emb = discord.Embed(title=f'{ctx.author}', description=f"{mesg1}")
    await Bot.get_user(521313537943928852).send(embed = emb)
    await ctx.send("Отправлено!")

@Bot.command(name= 'info', pass_context=True)
async def loh(ctx):
    emb = discord.Embed(color=0xf90aff, title = "osu!info", description="**Привет, я osu!bot \n Мой создатель: insert#9035 \n Помощники в разработке: MrModer#6697 и mihagreen#1082 \n Внимание \n Бот все еще разрабатывается хоть он и релизнут но все же он еще не полностью готов**")
    emb.set_footer(text="osu!bot Copyright 2020-2020", icon_url="https://media.discordapp.net/attachments/675294482991808513/687743226102546545/lazer.png?width=585&height=585")
    await ctx.send(embed = emb)

@Bot.command(name= 'shutdown', pass_context=True)
@commands.is_owner()
async def lol(ctx):
    msg = await ctx.send("<a:loadingg:689150668359205064> **see next time**")
    await asyncio.sleep(5)
    await msg.edit(content = "<a:loadingg:689150668359205064> **Бот отключен**")
    await Bot.close()

@Bot.command(name='lock', pass_context= True)
@commands.has_permissions(manage_channels=True)
async def lal(ctx, member: discord.Member=None):
    if not member:
        emb = discord.Embed(color=0xf90aff, title = "osu!lock", description="**Укажите кого надо заблокировать!<:redTick:596576672149667840>**")
        emb.set_footer(text="osu!bot Copyright 2020-2020", icon_url="https://media.discordapp.net/attachments/675294482991808513/687743226102546545/lazer.png?width=585&height=585")
        await ctx.send(embed = emb)
        return
    emb = discord.Embed(color=0xf90aff, title = "osu!lock", description=f"{member.mention} **Был заблокирован!<:greenTick:596576670815879169>**")
    emb.set_footer(text="osu!bot Copyright 2020-2020", icon_url="https://media.discordapp.net/attachments/675294482991808513/687743226102546545/lazer.png?width=585&height=585")
    await ctx.send(embed = emb)
    role = discord.utils.get(ctx.guild.roles, name="Blocked")
    await member.add_roles(role)

@Bot.command(name='unlock', pass_context= True)
@commands.has_permissions(manage_roles=True)
async def lul(ctx, member: discord.Member=None):
    if not member:
        emb = discord.Embed(color=0xf90aff, title = "osu!unlock", description="**Укажите кого надо разблокировать!<:redTick:596576672149667840>**")
        emb.set_footer(text="osu!bot Copyright 2020-2020", icon_url="https://media.discordapp.net/attachments/675294482991808513/687743226102546545/lazer.png?width=585&height=585")
        await ctx.send(embed = emb)
        return
    emb = discord.Embed(color=0xf90aff, title = "osu!unlock", description=f"{member.mention} **Был разбокирован!<:greenTick:596576670815879169>**")
    emb.set_footer(text="osu!bot Copyright 2020-2020", icon_url="https://media.discordapp.net/attachments/675294482991808513/687743226102546545/lazer.png?width=585&height=585")
    await ctx.send(embed = emb)    
    role = discord.utils.get(ctx.guild.roles, name="Blocked")
    await member.remove_roles(role)

@Bot.command(name='createblockroom', pass_context=True)
@commands.has_permissions(administrator=True)
async def her(ctx):
    await ctx.guild.create_category('Для заблокированных')
    await ctx.guild.create_text_channel('чат для блокнутых')
    await ctx.guild.create_text_channel('бот канал')
    await ctx.guild.create_text_channel('флудилка')
    await ctx.guild.create_role(name="Blocked")
    await ctx.send("Комнаты были созданы, вам нужно только их настроить")

@Bot.command()
@commands.has_permissions(manage_messages=True)
async def clear(ctx, amount = 1000):
    await ctx.channel.purge(limit=amount)
    emb = discord.Embed(color=0xf90aff, title = "osu!clear", description=f'{amount} Сообщений было удалено<:greenTick:596576670815879169>')
    emb.set_footer(text="osu!bot Copyright 2020-2020", icon_url="https://media.discordapp.net/attachments/675294482991808513/687743226102546545/lazer.png?width=585&height=585")
    await ctx.send(embed = emb)    
@clear.error
async def clear_error(ctx, error):
    if isinstance(error, commands.CheckFailure):
       emb = discord.Embed(color=0xf90aff, title = "osu!clear", description="**Ты не можешь удалять сообщения!<:greenTick:596576670815879169>")
       emb.set_footer(text="osu!bot Copyright 2020-2020", icon_url="https://media.discordapp.net/attachments/675294482991808513/687743226102546545/lazer.png?width=585&height=585")
       await ctx.send(embed = emb)

@Bot.command()
async def ping(ctx):
    ping = round(Bot.latency * 1000)
    await ctx.send(f"Пинг бота равен: `{ping}ms`")
    
Bot.run("token")

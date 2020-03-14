import discord
from discord.ext import commands
import inspect
import asyncio
import random
import os

Bot = commands.Bot(command_prefix="osu!")
Bot.remove_command("help")

@Bot.event
async def on_ready():
    print(f"{Bot.user} работает!")

@Bot.command(pass_context= True)
async def help(ctx):
    emb = discord.Embed(color=0xf90aff, description="<a:osivisualizer:688403122523209731>Привет я osu!bot мой префикс `osu!` \n `help` Показывает это меню \n `mute` Выдает мут \n `kick` Кикает участника с сервера \n `unmute` Размучивает участника \n `invite` Пригласить бота к себе на сервер! \n `eval` Команда создателя ее невозможно использовать \n `ping` Проверить пинг бота комманда бесполезна \n `updates` Обновления бота \n `clear` Очистить чат в пределах 1000 сообщений")
    emb.set_footer(text="osu!bot copyright 2020-2020", icon_url="https://media.discordapp.net/attachments/675294482991808513/687743226102546545/lazer.png?width=585&height=585")
    await ctx.send(embed = emb)

def you_user(ctx):
    return ctx.message.author.id == 521313537943928852

@Bot.command(name='eval', aliases=["e"], pass_context=True)
@commands.check(you_user)
async def eval_(ctx, *, command):
    res = eval(command)
    if inspect.isawaitable(res):
        await ctx.send(await res)
    else:
        await ctx.send(res)   

@Bot.command(pass_context=False)
async def ping(ctx):
    ping = round(Bot.latency * 1000)
    await ctx.send(f"Пинг: `{ping}ms`")

@Bot.command(pass_context= True)
@commands.has_permissions(administrator=True)
async def kick(ctx, member:discord.Member = None):
    if not member:
        emb = discord.Embed(color=0xf90aff, description="**Укажите кого надо кикнуть!<:redTick:596576672149667840>**")
        emb.set_footer(text="osu!bot Copyright 2020-2020", icon_url="https://media.discordapp.net/attachments/675294482991808513/687743226102546545/lazer.png?width=585&height=585")
        await ctx.send(embed = emb)
        return
    await member.kick()
    emb = discord.Embed(description=f"{member.mention} **Был кикнут!<:greenTick:596576670815879169>**")
    emb.set_footer(text="osu!bot Copyright 2020-2020", icon_url="https://media.discordapp.net/attachments/675294482991808513/687743226102546545/lazer.png?width=585&height=585")
    await ctx.send(embed = emb)

@kick.error
async def kick_error(ctx, error):
    if isinstance(error, commands.CheckFailure):
      emb = discord.Embed(color=0xf90aff, description="**Ты не можешь использовать эту комманду<:redTick:596576672149667840>**")
      emb.set_footer(text="osu!bot Copyright 2020-2020", icon_url="https://media.discordapp.net/attachments/675294482991808513/687743226102546545/lazer.png?width=585&height=585")
      await ctx.send(embed = emb)

@Bot.command(pass_context= True)
@commands.has_permissions(administrator=True)
async def mute(ctx, member: discord.Member=None):
    if not member:
        emb = discord.Embed(color=0xf90aff, description="**Укажите кого надо замутить!<:redTick:596576672149667840>**")
        emb.set_footer(text="osu!bot Copyright 2020-2020", icon_url="https://media.discordapp.net/attachments/675294482991808513/687743226102546545/lazer.png?width=585&height=585")
        await ctx.send(embed = emb)
        return
    emb = discord.Embed(color=0xf90aff, description=f"{member.mention} **Был замучен!<:greenTick:596576670815879169>**")
    emb.set_footer(text="osu!bot Copyright 2020-2020", icon_url="https://media.discordapp.net/attachments/675294482991808513/687743226102546545/lazer.png?width=585&height=585")
    await ctx.send(embed = emb)
    role = discord.utils.get(ctx.guild.roles, name="Muted")
    await member.add_roles(role)

@mute.error
async def mute_error(ctx, error):
    if isinstance(error, commands.CheckFailure):
        emb = discord.Embed(color=0xf90aff, description="**Ты не можешь замутить этого пользователя!<:redTick:596576672149667840>**")
        emb.set_footer(text="osu!bot Copyright 2020-2020", icon_url="https://media.discordapp.net/attachments/675294482991808513/687743226102546545/lazer.png?width=585&height=585")
        await ctx.send(embed = emb)
 
@Bot.command(pass_context= True)
@commands.has_permissions(administrator=True)
async def unmute(ctx, member: discord.Member=None):
    if not member:
        emb = discord.Embed(color=0xf90aff, description="**Укажите кого надо размутить!<:redTick:596576672149667840>**")
        emb.set_footer(text="osu!bot Copyright 2020-2020", icon_url="https://media.discordapp.net/attachments/675294482991808513/687743226102546545/lazer.png?width=585&height=585")
        await ctx.send(embed = emb)
        return
    emb = discord.Embed(color=0xf90aff, description=f"{member.mention} **Был размучен!<:greenTick:596576670815879169>**")
    emb.set_footer(text="osu!bot Copyright 2020-2020", icon_url="https://media.discordapp.net/attachments/675294482991808513/687743226102546545/lazer.png?width=585&height=585")
    await ctx.send(embed = emb)    
    role = discord.utils.get(ctx.guild.roles, name="Muted")
    await member.remove_roles(role)

@mute.error
async def unmute_error(ctx, error):
    if isinstance(error, commands.CheckFailure):
        emb = discord.Embed(color=0xf90aff, description="**Ты не можешь размутить этого пользователя!<:redTick:596576672149667840>**")
        emb.set_footer(text="osu!bot Copyright 2020-2020", icon_url="https://media.discordapp.net/attachments/675294482991808513/687743226102546545/lazer.png?width=585&height=585")
        await ctx.send(embed = emb)

@Bot.command(pass_context= True)
async def invite(ctx):
    emb = discord.Embed(color=0xf90aff, description="[Пригласить бота!](https://discordapp.com/oauth2/authorize?client_id=684136563017515038&scope=bot&permissions=66186303)")
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
    emb = discord.Embed(color=0xf90aff, description="** <:toker:685203815288275106>Обновления бота: Бот релизнут <:sanitar:678951482506346496>**")
    emb.set_footer(text="osu!bot Copyright 2020-2020", icon_url="https://media.discordapp.net/attachments/675294482991808513/687743226102546545/lazer.png?width=585&height=585")
    await ctx.send(embed = emb)

1
@Bot.command()
async def say(ctx, *, msg):
    await ctx.message.delete()
    embed = discord.Embed(
        title = "<a:osuvisualizer:688403122523209731>Кто-то что-то сказал...",
        description = "{}" .format(msg)
    )
    await ctx.send(embed = embed)

initial_extensions = ['status', 'minesweeper'] 

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
    emb = discord.Embed(color=0xf90aff, description="**Привет, я osu!bot \n Мой создатель: insert worst nightmare#9035 \n Помощники в разработке: MrModer#6697 и mihagreen#1082 \n Внимание \n Бот все еще разрабатывается хоть он и релизнут но все же он еще не полностью готов**")
    emb.set_footer(text="osu!bot Copyright 2020-2020", icon_url="https://media.discordapp.net/attachments/675294482991808513/687743226102546545/lazer.png?width=585&height=585")
    await ctx.send(embed = emb)

Bot.run("Njg0MTM2NTYzMDE3NTE1MDM4.XmQqhQ.kf5VSZl-2Bx6MUWCVjW2ZRiqTfY")
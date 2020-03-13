import discord
from discord.ext import commands
import inspect
import asyncio
import random

Bot = commands.Bot(command_prefix="osu!")
Bot.remove_command("help")
@Bot.event
async def on_ready():
    await Bot.change_presence(activity=discord.Game(name='osu!help - Для помощи'))
    print(f"{Bot.user} why nahui!")

@Bot.command(pass_context= True)
async def help(ctx):
    emb = discord.Embed(description="**Привет я osu!bot. Мой префикс `osu!` \n `help` Показывает это меню \n `mute` Выдает мут \n `kick` Кикает участника с сервера \n `unmute` Размучивает участника \n `invite` Пригласить бота к себе на сервер! \n `eval` Команда создателя ее невозможно использовать \n `ping` Проверить пинг бота комманда бесполезна \n `updates` Обновления бота \n `clear` Очистить чат в пределах 1000 сообщений**")
    emb.set_footer(text="osu!bot copyright 2020-2020", icon_url="https://media.discordapp.net/attachments/675294482991808513/687743226102546545/lazer.png?width=585&height=585")
    await ctx.send(embed = emb)

def you_user(ctx):
    return ctx.message.author.id == 521313537943928852

@Bot.command(name='eval', pass_context=True)
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
        emb = discord.Embed(description="**Укажите кого надо кикнуть!**")
        emb.set_footer(text="osu!bot Copyright 2020-2020", icon_url="https://media.discordapp.net/attachments/675294482991808513/687743226102546545/lazer.png?width=585&height=585")
        await ctx.send(embed = emb)
        return
    await member.kick()
    emb = discord.Embed(description=f"{member.mention} **Был кикнут!**")
    emb.set_footer(text="osu!bot Copyright 2020-2020", icon_url="https://media.discordapp.net/attachments/675294482991808513/687743226102546545/lazer.png?width=585&height=585")
    await ctx.send(embed = emb)

@kick.error
async def kick_error(ctx, error):
    if isinstance(error, commands.CheckFailure):
      emb = discord.Embed(description="**Ты не можешь использовать эту комманду**")
      emb.set_footer(text="osu!bot Copyright 2020-2020", icon_url="https://media.discordapp.net/attachments/675294482991808513/687743226102546545/lazer.png?width=585&height=585")
      await ctx.send(embed = emb)

@Bot.command(pass_context= True)
@commands.has_permissions(administrator=True)
async def mute(ctx, member: discord.Member=None):
    if not member:
        emb = discord.Embed(description="**Укажите кого надо замутить!**")
        emb.set_footer(text="osu!bot Copyright 2020-2020", icon_url="https://media.discordapp.net/attachments/675294482991808513/687743226102546545/lazer.png?width=585&height=585")
        await ctx.send(embed = emb)
        return
    emb = discord.Embed(description=f"{member.mention} **Был замучен!**")
    emb.set_footer(text="osu!bot Copyright 2020-2020", icon_url="https://media.discordapp.net/attachments/675294482991808513/687743226102546545/lazer.png?width=585&height=585")
    await ctx.send(embed = emb)
    role = discord.utils.get(ctx.guild.roles, name="Muted")
    await member.add_roles(role)

@mute.error
async def mute_error(ctx, error):
    if isinstance(error, commands.CheckFailure):
        emb = discord.Embed(description="**Ты не можешь замутить этого пользователя!**")
        emb.set_footer(text="osu!bot Copyright 2020-2020", icon_url="https://media.discordapp.net/attachments/675294482991808513/687743226102546545/lazer.png?width=585&height=585")
        await ctx.send(embed = emb)
 
@Bot.command(pass_context= True)
@commands.has_permissions(administrator=True)
async def unmute(ctx, member: discord.Member=None):
    if not member:
        emb = discord.Embed(description="**Укажите кого надо размутить!**")
        emb.set_footer(text="osu!bot Copyright 2020-2020", icon_url="https://media.discordapp.net/attachments/675294482991808513/687743226102546545/lazer.png?width=585&height=585")
        await ctx.send(embed = emb)
        return
    emb = discord.Embed(description=f"{member.mention} **Был размучен!**")
    emb.set_footer(text="osu!bot Copyright 2020-2020", icon_url="https://media.discordapp.net/attachments/675294482991808513/687743226102546545/lazer.png?width=585&height=585")
    await ctx.send(embed = emb)    
    role = discord.utils.get(ctx.guild.roles, name="Muted")
    await member.remove_roles(role)

@mute.error
async def unmute_error(ctx, error):
    if isinstance(error, commands.CheckFailure):
        emb = discord.Embed(description="**Ты не можешь размутить этого пользователя!**")
        emb.set_footer(text="osu!bot Copyright 2020-2020", icon_url="https://media.discordapp.net/attachments/675294482991808513/687743226102546545/lazer.png?width=585&height=585")
        await ctx.send(embed = emb)

@Bot.command(pass_context= True)
async def invite(ctx):
    await ctx.send(f'https://discordapp.com/oauth2/authorize?client_id={Bot.user.id}&scope=bot&permissions=66186303')

@Bot.command(name='8ball', pass_context= True)
async def lox(ctx, arg):
        if arg != '':
            messages = ['Да.', 'Нет.', 'Ага!', 'Ну, наверно!', 'Конечно, нет!', 'Спроси позже!', 'Неа, не буду отвечать)0)0)). 😎']
            kv1 = int(len(messages))
            messages_output = messages.pop(random.randint(0, kv1 - 1))
            await ctx.send(f'{messages_output}')

@Bot.command(name= 'updates', pass_context=True)
async def hui(ctx):
    emb = discord.Embed(description="**Обновления бота: \n Были исправлены опечатки в коммандах, \n Была добавлена комманда `updates` \n Была добавлена комманда `clear` \n Теперь, половина бота теперь в embed стиле**")
    emb.set_footer(text="osu!bot Copyright 2020-2020", icon_url="https://media.discordapp.net/attachments/675294482991808513/687743226102546545/lazer.png?width=585&height=585")
    await ctx.send(embed = emb)

@Bot.command()
@commands.has_permissions(manage_messages=True)
async def clear(ctx, amount = 1000):
    await ctx.channel.purge(limit=amount)
    await ctx.send(f'Удалено {amount} сообщений')
@clear.error
async def clear_error(ctx, error):
    if isinstance(error, commands.CheckFailure):
        await ctx.send("Ты не имеешь право очищать сообщения.")

@Bot.command(pass_context= True)
async def say(ctx, *, msg):
    await ctx.message.delete()
    await ctx.send("{}" .format(msg))  

@Bot.command(name= 'block', pass_context= True)
@commands.has_permissions(administrator=True)
async def flame(ctx, member: discord.Member=None):
    if not member:
        emb = discord.Embed(description="**Укажите кого надо замутить!**")
        emb.set_footer(text="osu!bot Copyright 2020-2020", icon_url="https://media.discordapp.net/attachments/675294482991808513/687743226102546545/lazer.png?width=585&height=585")
        await ctx.send(embed = emb)
        return
    emb = discord.Embed(description=f"{member.mention} **Был замучен!**")
    emb.set_footer(text="osu!bot Copyright 2020-2020", icon_url="https://media.discordapp.net/attachments/675294482991808513/687743226102546545/lazer.png?width=585&height=585")
    await ctx.send(embed = emb)
    role = discord.utils.get(ctx.guild.roles, name="Blocked")
    await member.add_roles(role)

Bot.run("Njg0MTM2NTYzMDE3NTE1MDM4.XmQqhQ.kf5VSZl-2Bx6MUWCVjW2ZRiqTfY")
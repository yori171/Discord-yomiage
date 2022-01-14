import discord
from discord.ext import commands
import asyncio
import os
import subprocess
import ffmpeg
from voice_generator import creat_WAV

client = commands.Bot(command_prefix='.')
voice_client = None
ch = None
while(1):

    @client.event
    async def on_ready():
        print('Logged in as')
        print(client.user.name)
        print(client.user.id)
        print('------')

    @client.command()
    async def join(ctx):
        print('#join')
        global ch
        ch = ctx.channel.id
        print(ch)
        print('#voicechannelを取得')
        vc = ctx.author.voice.channel
        print('#voicechannelに接続\n')
        await vc.connect()

    @client.command()
    async def bye(ctx):
        print('#bye')
        print('#切断')
        await ctx.voice_client.disconnect()

    @client.command()
    async def dic(ctx, arg1, arg2):
         with open('C:/open_jtalk/bin/dic.txt', mode='a') as f:
            f.write('\n'+ arg1 + ',' + arg2)
            print('dic.txtに書き込み：''\n'+ arg1 + ',' + arg2)
         await ctx.send('`' + arg1+'` を `'+arg2+'` として登録しました')

    @client.event
    async def on_message(message):
        global ch
        print('---on_message_start---')
        msgclient = message.guild.voice_client
        print(msgclient)
        if message.content.startswith('<'):
            pass

        elif message.content.startswith('.'):
            pass
        elif message.channel.id==ch :
            if message.guild.voice_client:
                print('#message.content:'+ message.content)
                creat_WAV(message.content)
                source = discord.FFmpegPCMAudio("output.wav")
                message.guild.voice_client.play(source)
            else:
                pass
        else:
                pass
        await client.process_commands(message)
        print('---on_message_end---\n\n')



    client.run("　　　とーくん　　　　")

import asyncio
import discord
import os


app = discord.Client()


@app.event
async def on_ready():
    print("다음으로 로그인합니다 : ")
    print(app.user.name)
    print(app.user.id)
    print("============")

    await app.change_presence(game=discord.Game(name="하나둘셋", type=1))

@app.event
async def on_message(message):
    
    if message.author.bot:
        return None
    if message.content == "콤보시작!":
        await app.send_message(message.channel,"하나!")
    if message.content == "하나!":
        await app.send_message(message.channel, "둘!")       
    if message.content == "둘!":
         await app.send_message(message.channel, "셋!")
    if message.content == "셋!":
         await app.send_message(message.channel, "야!")
    if message.content == "야!":
        await app.send_message(message.channel,"이분 최소 배우신 분 ㅇㅈ")
    if message.content == "!미간":
        await app.send_message(message.channel,"이거슨 제 미간이 아니라 찌찌입니다.")
    if message.content == "!김나":
        await app.send_message(message.channel,"성방!")
access_token = os.environ["BOT_TOKEN"]
app.run(access_token)

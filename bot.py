import discord
import asyncio
from discord.ext import commands
from datetime import date
from datetime import datetime
import os
import random
from discord.utils import get




bot = commands.Bot(command_prefix = '!')



@bot.event
async def on_ready():
  # [discord.Status.online = 온라인],[discord.Status.idle = 자리비움],[discord.Status.dnd = 다른용무],[discord.Status.offline = 오프라인]
  await bot.change_presence(status=discord.Status.online)

  await bot.change_presence(activity=discord.Game(name="강좌 적기"))
  #await bot.change_presence(activity=discord.Streaming(name="스트림 방송중", url='링크'))
  #await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name="노래 듣는중"))
  #await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="영상 시청중"))
  
  print("봇 이름:",bot.user.name,"봇 아이디:",bot.user.id,"봇 버전:",discord.__version__)





@bot.event
async def on_message(message): # 메시지가 들어 올 때마다 가동되는 구문입니다.
  if message.author.bot: # 채팅을 친 사람이 봇일 경우
    return None # 반응하지 않고 구문을 종료합니다.
  
  if message.content == "!애드센스": # !명령어   라는 채팅을 친다면
    await message.author.send("1차-승인거절 (사유:컨텐츠부족)\n2차-승인거절 (사유:컨텐츠부족)\n3차-승인거절 (사유:컨텐츠부족)\n4차-승인거절 (사유:중복계정)\n5차-승인거절 (사유:중복계정)\n6차-승인거절 (사유:중복계정)\n7차-승인거절 (사유:중복계정)\n8차-승인거절 (사유:중복계정)\n9차-승인거절 (사유:컨텐츠 위반)\n10차-승인거절 (사유:컨텐츠 위반)\n11차-승인거절 (사유:중복계정)\n12차-승인거절 (사유:중복계정)")
    await message.channel.send("개인 채팅으로 답변완료했습니다.")


  if message.content == "!음식추천": # !명령어   라는 채팅을 친다면
    foodlist = ["피자","햄버거","치킨","짜장면","짬뽕","탕수육","샌드위치","우동","라면","돈가스","규카츠","소고기","부리또","타코","보쌈","굴라쉬","국밥","닭꼬치","양꼬치","연어","육회","족발",
    "회덮밥","파스타","삼겹살","쌀국수","무뼈닭발","유린기"]
    choicefood = random.choice(foodlist)
    ingredientlist = ["담백한걸","기름진걸","살찌는걸","짭조름 한걸","간단한걸"]
    choiceingredient = random.choice(ingredientlist)
    now = datetime.now()
    htime = now.strftime("%H")
    realtime = htime + 3
    await message.channel.send("지금이 " + '%s' % (realtime) + "시니까 " + choiceingredient + " 먹는게 좋을것 같아..... 그러니까 " + choicefood + "을(를) 추천할게!")
  
  if message.content == "!테스트":
    roles = discord.utils.find (lambda r: r.name == '역할이름', message.guild.roles)
    if roles in message.author.roles :
      await message.channel.send("개인 채팅으로 답변완료했습니다.")



#서버 자체 있는지 확인
#@bot.command()
#async def modrole(ctx):
#    if get(ctx.guild.roles, name="BotMod"):
#        await ctx.send("Role already exists")
#    else:
#        await ctx.guild.create_role(name="BotMod", colour=discord.Colour(0x0062ff))

#@bot.command()
#async def mute(ctx, user: discord.Member):
#    role = discord.utils.get(ctx.guild, name='member')
#    await user.remove_roles(role))

#if 문 안속에 넣는거

#roles = discord.utils.find (lambda r: r.name == '역할이름', message.guild.roles)
#if roles in message.author.roles :
# 명령어



#@bot.command()
#@commands.has_any_role("test")
#async def test(ctx):
#    await ctx.send('You can manage messages.')






bot.run(os.environ['token'])
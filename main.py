Token = '7952540608:AAH90ohBZbLvFLVfJVoir2TetGbyV-xhtN4'

import asyncio
import time
from aiogram import *
from aiogram.filters import *
from aiogram.methods import *
from aiogram.types import *

bot = Bot(Token)
router = Router()
dispatch = Dispatcher()
clocking = time.time()
Mess = ["членовыжигатель",2.5,0]
Statuses = []
async def starting(indexer):
    for i in range(0,99999):
        ta = Statuses[indexer-1]
        ta[1] = i
        await bot.send_message(chat_id = Mess[2], text=Mess[0])
        await asyncio.sleep(Mess[1])
@dispatch.message(Command('fuck'))
async def mainss(message: Message):
    Trash = await message.reply('Ожидание ответа от сервера...')
    await bot.delete_message(Trash.chat.id,Trash.message_id)
    index = 0
    for i in Statuses :
        index += 1
    ar = "Статусер : " + str(index+1)
    Statuses.insert(index+1,[ar, 0])
    await starting(index + 1)
@dispatch.message(Command('sm'))
async def mas(message:Message):
    Mess[0] = message.text[17:99999999]
    emoji = ReactionTypeEmoji(emoji='👌')
    await message.react([emoji])
    textv = "В-X: "+ str(Mess[0])
    await message.reply(text=textv)

@dispatch.message(Command('inter'))
async def mas(message:Message):
    Mess[1] = float(message.text[20:99999999])
    emoji = ReactionTypeEmoji(emoji='👌')
    await message.react([emoji])
    textv = "I-X: "+ str(Mess[1])
    await message.reply(text=textv)

@dispatch.message(Command('ider'))
async def mas(message:Message):
    Mess[2] = int(message.text[19:99999999])
    emoji = ReactionTypeEmoji(emoji='👌')
    await message.react([emoji])
    textv = "ID-X: "+ str(Mess[2])
    await message.reply(text=textv)

@dispatch.message(Command('statuser'))
async def mas(message:Message):
    Messe = ""
    for i in Statuses:
        t = i
        Messe = Messe + str(t[0]) + str(t[1]) + "\n"
    await message.reply(Messe + str("\nSX-X"))

@dispatch.message(Command('this'))
async def mas(message:Message):
    await message.reply(str(message.chat.id) + str("\nID-GX"))
async def starting_bot():
    print(f"Бот запущен за ~{int(time.time()-clocking)} секунд.")
    await dispatch.start_polling(bot)

asyncio.run(starting_bot())

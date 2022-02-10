from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from telebot import types
import asyncio

from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
import datetime

from get_holiday import Holidays
from config import TOKEN


bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

data: Holidays
my_date: datetime.date
id_: int


@dp.message_handler(commands=['start'])
async def welcome(message: types.Message):
    global my_date, id_
    global data

    my_date = datetime.date.today()
    data = Holidays()
    id_ = message.chat.id

    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    item = KeyboardButton('Какой сегодня праздник?')
    markup.add(item)

    await message.reply("Привет! Я персональный бот от Ксюхи\n"
                        "", reply_markup=markup)


# @dp.message_handler(commands=['help'])
# async def process_help_command(message: types.Message):
#     await message.reply("Напиши мне что-нибудь, и я отпрпавлю этот текст тебе в ответ!")


async def fun(wait_for):
    global my_date
    while True:
        await asyncio.sleep(wait_for)

        if my_date != datetime.date.today():
            data.update_holidays()
            my_date = datetime.date.today()

        await bot.send_message(id_, data.get_holiday(), disable_notification=True)


@dp.message_handler()
async def echo_message(msg: types.Message):
    if msg.text == 'Какой сегодня праздник?':
        await bot.send_message(msg.from_user.id, str(data.get_holiday()))
    else:
        await bot.send_message(msg.from_user.id, msg.text)


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.create_task(fun(10))
    executor.start_polling(dp)

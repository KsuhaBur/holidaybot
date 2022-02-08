from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from telebot import types

from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton
import random

from config import TOKEN

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def welcome(message: types.Message):

    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    item = KeyboardButton('Рандомное число')
    markup.add(item)

    await message.reply("Привет! Я персональный бот от Ксюхи", reply_markup=markup)


# @dp.message_handler(commands=['help'])
# async def process_help_command(message: types.Message):
#     await message.reply("Напиши мне что-нибудь, и я отпрпавлю этот текст тебе в ответ!")


@dp.message_handler()
async def echo_message(msg: types.Message):
    if msg.text == 'Рандомное число':
        await bot.send_message(msg.from_user.id, str(random.randint(0, 100)))
    else:
        await bot.send_message(msg.from_user.id, msg.text)


if __name__ == '__main__':
    executor.start_polling(dp)

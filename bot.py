from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from telebot import types

from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton
import random

import get_holiday

from config import TOKEN

import requests
from bs4 import BeautifulSoup

url = 'https://kakoyprazdnik.com/'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'lxml')

# holidays = soup.find_all('h4')


bot = Bot(token=TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def welcome(message: types.Message):

    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    item = KeyboardButton('Какой сегодня праздник?')
    markup.add(item)

    await message.reply("Привет! Я персональный бэтмен-бот от Ксюхи\n"
                        "", reply_markup=markup)


# @dp.message_handler(commands=['help'])
# async def process_help_command(message: types.Message):
#     await message.reply("Напиши мне что-нибудь, и я отпрпавлю этот текст тебе в ответ!")


@dp.message_handler()
async def echo_message(msg: types.Message):
    if msg.text == 'Какой сегодня праздник?':
        await bot.send_message(msg.from_user.id, str(get_holiday.get_all_holidays()))
    else:
        await bot.send_message(msg.from_user.id, msg.text)


if __name__ == '__main__':
    executor.start_polling(dp)

from main import bot, dp
from aiogram.types import Message
from config import admin_id

from pyowm import OWM  # OpenWeatherMap.org API


async def send_to_admin(*args):
    await bot.send_message(chat_id=admin_id, text="I'm started!")


@dp.message_handler()
async def get_weather(message: Message):
    text = f"Ты написал: {message.text}, но я тебя не понял. Я еще учусь"
    lat = message.location.latitude
    lot = message.location.longitude
    if message == "Погода" or "погода":
        await message.answer("Пришли мне свою геопозицию")
        if message == message.answer_location(latitude=lat, longitude=lot):
            await message.answer("Ваша геопозиция: ", lat, lot)

    else:
        await message.reply(text=text)

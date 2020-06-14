from main import bot, dp, owm
from aiogram import types
from config import admin_id
from aiogram.types.location import Location
from aiogram.types import ParseMode
import pyowm
from time import sleep
import sys

async def send_to_admin(*args):
    await bot.send_message(chat_id=admin_id, text="I'm started!")


# @dp.message_handler(content_types=types.ContentType.LOCATION)
# async def get_location(call):
#  print("Ваша геопозиция: ", call.location)
# print("Ваша геопозиция: ",  call.location.latitude,  call.location.longitude)
# lat = call.location.latitude, long = call.location.longitude
# return lat, long
#   await get_weather(types.Message.location)
#  return call.location

message1: types.Message


@dp.message_handler()
async def get_weather(message: types.Message):
    global message1
    message1 = message
    if message.text == 'Погода':
        await message.answer('Пришли свою геопозицию')
        message1.text = '1'
    else:
        text = f"Ты написал: {message.text}, но я тебя не понял. Я еще учусь"
        await message.reply(text=text)
        message1.text = '0'


@dp.message_handler(content_types=types.ContentType.LOCATION)
async def get_location(call):
    global message1
    if message1.text == '1':
        message1.text = call.location
        global owm
        mgr = owm.weather_manager()
        obs = mgr.weather_at_coords(call.location.latitude, call.location.longitude) # Create a weather observation
        w = obs.weather
        l = obs.location
        #f = l.forecast
        print(w) # <Weather - reference time=2013-12-18 09:20, status=Clouds>
        print(l.name, l.country)
        placename = str(l.name)
        country = str(l.country)
        d_stat = str(w.detailed_status)
        print(d_stat)
       # l = obs.get_location()  # create a location related to our already created weather object And send the parameters
        #status = str(obs.)

        #wtime = str(w.reference_time) #(timeformat='iso')
        temperature = str(w.temperature('celsius').get('temp'))
        await message1.answer('Сейчас погода в ' + placename +',' + country + ': ' + d_stat +', температура= ' + temperature + '°C')
    else:
        await message1.answer('Ты лох!')



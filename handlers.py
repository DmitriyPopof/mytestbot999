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
    if message.text == 'Погода' or 'погода':
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
        obs = mgr.weather_at_coords(call.location.latitude, call.location.longitude)  # Create a weather observation
        forc = mgr.forecast_at_coords(call.location.latitude, call.location.longitude, '3h')
        w = obs.weather
        f = forc.forecast
        l = obs.location
        placename = str(l.name)
        country = str(l.country)
        d_stat = str(w.detailed_status)
        ref_time = str(w.reference_time('date'))
        wind = str(w.wnd.get('speed'))
        srise_time = str(w.sunrise_time('iso'))
        sset_time = str(w.sunset_time('iso'))
        pressure = str(w.pressure.get('press'))
        temperature = str(w.temperature('celsius').get('temp'))
        t_feels = str(w.temperature('celsius').get('feels_like'))
        rain = str(w.rain.get('_len_'))
        snow = str(w.snow.get('_len_'))
        forcast_d_stat = str(f.weathers.get(index))
        print(l.name, l.country, wind, pressure, d_stat, temperature)

        await message1.answer(
            'Сейчас (' + ref_time + ') \nпогода в ' + placename + ',' + country + ': \n' + d_stat + ', температура: ' +
            temperature + '°C,\n' + 'чувствуется как: '+t_feels + '°C'+', \nветер: ' + wind + 'м/с' + ', \nдавление: '
            + pressure + 'мм.рт.ст.\nРассвет: ' + srise_time + '.\nЗакат: ' + sset_time + '\nБлижайшие 3 часа: ' +
            forcast_d_stat)
    else:
        await message1.reply('Это не геолокация!')

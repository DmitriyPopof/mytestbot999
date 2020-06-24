import asyncio

from aiogram import Bot,Dispatcher, executor
from config import BOT_TOKEN, OWM_TOKEN
from pyowm import OWM  # OpenWeatherMap.org API
from pyowm.utils.config import get_default_config


loop = asyncio.get_event_loop()

bot = Bot(BOT_TOKEN, parse_mode='HTML')
dp = Dispatcher(bot, loop=loop)

config_dict = get_default_config()
config_dict['language'] = 'ru'
owm = OWM(OWM_TOKEN, config_dict)  # initialize the Weather API

if __name__=="__main__":
    from handlers import dp, send_to_admin
    executor.start_polling (dp, on_startup=send_to_admin)
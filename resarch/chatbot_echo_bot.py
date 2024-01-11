import logging
from aiogram import Bot, Dispatcher , executor , types
from dotenv import load_dotenv
import os

load_dotenv()
Chatbot_API_key = os.getenv("TOOKEN")
# print(Chatbot_API_key)

# configuration
logging.basicConfig(level=logging.INFO)

# initalize bot and dispatcher
bot = Bot(token=Chatbot_API_key)
dp = Dispatcher(bot)

@dp.message_handler(commands = ['start' , 'help'])
async def command_start_handler(message: types.Message):
    """
    This handler receives messages with `/start` or  `/start` command
    """
    await message.reply("Hi \nI am here to Connect You \nto my BOSS.")
    
    
    
@dp.message_handler()
async def echo(message: types.Message):
    """
    This will return Echo
    """
    await message.answer(message.text)
    
if __name__ == "__main__":
    executor.start_polling(dp , skip_updates=True)
    
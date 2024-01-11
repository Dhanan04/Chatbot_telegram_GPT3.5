from dotenv import load_dotenv
from aiogram import Bot, Dispatcher , executor , types
import os
import openai
import sys



class Reference:
    
    # Class to remember the previous response
    
    
    def __init__(self) -> None:
        self.response = ""
    
load_dotenv()
openai.api_key  = os.getenv("OpenAI_API_KEY")

reference = Reference()

TOKEEN = os.getenv("TOOKEN")


# Define ai model name
MODEL_NAME = 'gpt-3.5-turbo'

# initalize bot and dispatcher
bot = Bot(token=TOKEEN)
dp = Dispatcher(bot)



def clear_past():
    #to clear the previous context
    reference.response = ""
    
    
@dp.message_handler(commands = ['start'])
async def welcome(message: types.Message):
    """
    This handler receives messages with `/start` or  `/start` command
    """
    await message.reply("Hi \nI am Chatbot\n I am here to Connect You To my BOSS Arjun.\n How can i assist you?")
    
@dp.message_handler(commands = ['clear'])
async def clear(message: types.Message):
    """
    This will remove the previous response 
    """
    clear_past()
    await message.reply("Hi i have removed the Previous Context")
    
    

@dp.message_handler(commands = ['help'])
async def helper(message: types.Message):
    """
    This handler display the helper menu
    """
    
    help_commands = """ 
    Hi i am a Chatbot Created By Arjun ,, Please Follow These Commands For help,
    /start - To Start The Conversation 
    /clear - To Clear the Past Conversation and Contexts
    /help - To get Help
    Email us at on - Pappucant@gmail.com -
    Hope This Will Help :)
    """
    await message.reply(help_commands)
    

@dp.message_handler()
async def chatgpt(message: types.Message):
    
    print(f">>> USER: \n\t{message.text}")
    response = openai.ChatCompletion.create(
        model = MODEL_NAME ,
        messages = [
            {"role" : "assistant" , "content" : reference.response },
            { "role" : "user" , "content" : message.text}
        ]
    )
    
    reference.response = response['choices'][0]['message']['content']
    print(f">>> chatGPT: \n\t{reference.response}")
    await bot.send_message(chat_id = message.chat.id , text = reference.response)


if __name__ == "__main__":
    executor.start_polling(dp , skip_updates=False)
    
    
    
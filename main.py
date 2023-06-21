from aiogram import Bot, Dispatcher, executor, types
from pytube import YouTube
import time
import os

TOKEN = "6138392575:AAFumBrTx7VDCaPKnarqsGpG3GhfoHubuHc"
DEFAULT_PATH = 'C:\\Users\\Pavel\\Desktop\\download'

bot = Bot(token=TOKEN)
dp = Dispatcher(bot=bot)

def dowload_video(url):
    yt = YouTube(url, use_oauth=True, allow_oauth_cache=True)
    yt = yt.streams.get_highest_resolution()
    yt.download(DEFAULT_PATH, f"video.mp4")

def dowload_audio(url):
    yt = YouTube(url, use_oauth=True, allow_oauth_cache=True)
    yt.streams.filter(abr="160kbps", progressive=False).first().download(output_path = DEFAULT_PATH, filename="audio.mp3")

@dp.message_handler(commands=['start'])
async def start_handler(message: types.Message):
    user_id = message.from_user.id
    name = message.from_user.first_name
    await bot.send_message(user_id, "Hello, " + name + "! Send /help to get information about all commands")

@dp.message_handler(commands=['help'])
async def help_handler(message: types.Message):
    user_id = message.from_user.id
    await bot.send_message(user_id, "/downloadVideo <your url>| enter this command to download video from YouTube\n" + "/sendVoice <your url>| enter this command to send voice message with sound from YouTube\n" + "/downloadAudio <your url>| enter this command to download audio from YouTube\n" + "/help| print info\n" + "/start| Print hello to user and give some info\n"+ "/sendVideo| enter this command to send voice message with video from YouTube\n")

@dp.message_handler(commands=['downloadVideo'])
async def downloadVideo_handler(message: types.Message):
    user_id = message.from_user.id
    text = message.text.split(' ')
    if len(text) != 2:
        time.sleep(1)
        await bot.send_message(user_id, "Please, enter link to the YT")
    else:
        dowload_video(text[1])
        await bot.send_message(user_id, "All is done!")

@dp.message_handler(commands=['downloadAudio'])
async def downloadAudio_handler(message: types.Message):
    user_id = message.from_user.id
    text = message.text.split(' ')
    if len(text) != 2:
        time.sleep(1)
        await bot.send_message(user_id, "Please, enter link to the YT")
    else:
        dowload_audio(text[1])
        await bot.send_message(user_id, "All is done!")
        await bot.send_audio(user_id, open(os.path.join(DEFAULT_PATH, 'audio.mp3'), "r"), performer = "Performer", title = "Title")

@dp.message_handler(commands=['sendVoice'])
async def sendVoice_handler(message: types.Message):
    user_id = message.from_user.id
    text = message.text.split(' ')
    if len(text) != 2:
        time.sleep(1)
        await bot.send_message(user_id, "Please, enter link to the YT")
    else:
        dowload_audio(text[1])
        audio = open(os.path.join(DEFAULT_PATH, 'audio.mp3'), "rb")
        await bot.send_audio(user_id, audio)

@dp.message_handler(commands=['sendVideo'])
async def sendVoice_handler(message: types.Message):
    user_id = message.from_user.id
    text = message.text.split(' ')
    if len(text) != 2:
        time.sleep(1)
        await bot.send_message(user_id, "Please, enter link to the YT")
    else:
        dowload_video(text[1])
        await bot.send_video(user_id, open(os.path.join(DEFAULT_PATH, "video.mp4"), 'rb'))

if __name__ == "__main__":
    executor.start_polling(dp)

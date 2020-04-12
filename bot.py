import telebot
import config
from find_music import download_music

bot = telebot.TeleBot(config.token)


@bot.message_handler(commands=["start", ])
def start_message(message):
    bot.send_message(message.chat.id, 'Hi,Я Enot, я могу найти любую музыку!')


@bot.message_handler(commands=['find_music', ])
def find_music(message):
    chat_id = message.chat.id
    msg = bot.send_message(chat_id=chat_id, text='Отправь исполнителя и название песни')
    bot.register_next_step_handler(msg, send_music)


def send_music(message):
    song = message.text.split()
    song_to_url = '+'.join(song)
    binary_song = download_music(song_to_url)
    bot.send_audio(chat_id=message.chat.id, audio=binary_song)


if __name__ == '__main__':
    bot.polling(none_stop=True)

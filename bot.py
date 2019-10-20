import telebot
import config
import time
from find_music import find_mus, download_music
from os import listdir

bot = telebot.TeleBot(config.token)


@bot.message_handler(commands=["start"])
def start_message(message):
    bot.send_message(message.chat.id, 'Hi,Я Enot, я могу найти любую музыку!')


@bot.message_handler(content_types=['text'])
def send(message):
    saved_song = listdir('music')
    start_time = time.time()
    song = message.text
    if song + '.mp3' in saved_song:
        bot.send_audio(chat_id=message.chat.id, audio=open(f'music/{message.text}.mp3', 'rb'))
        print(f'I have this mus in folder. My time is {start_time - time.time()}')
    else:
        song = song.split()
        song = '+'.join(song)
        song_url = find_mus(song)
        print(song_url)
        print(f'got Url{start_time - time.time()}')
        if song_url == 'Error':
            bot.send_message(message.chat.id,'Song not found')
        else:
            download_music(song_url, message.text)
            time_save = time.time()
            print(f'save mus {time_save - time.time()}')
            send_mus = time.time()
            bot.send_audio(chat_id=message.chat.id, audio=open(f'music/{message.text}.mp3', 'rb'))

            print(f'send music{send_mus - time.time()}')


if __name__ == '__main__':
    bot.polling(none_stop=True)

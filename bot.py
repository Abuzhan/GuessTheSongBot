import telebot
import config
import os
import time
import random
import utils
from SQLighter import SQLighter
from telebot import types

bot = telebot.TeleBot(config.token)

@bot.message_handler(commands=['bill'])
def find_file_ids(message):
    for file in os.listdir('music/'):
        if file.split('.')[-1] == 'ogg':
            f = open('music/'+file, 'rb')
            res = bot.send_voice(message.chat.id, f, None, timeout=10)
            print(res)
            #bot.send_message(message.chat.id, msg.voice.file_id, reply_to_message_id=msg.id)
        time.sleep(3)

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, 'Добро пожаловать в игру угадай песню! Я буду отправлять вам отрывки разных песен, а старайтесь отгадать. Чтобы начать, введите команду /game.')

@bot.message_handler(commands=['game'])
def game(message):
    db_worker = SQLighter(config.database_name)
    if db_worker.check_new_user(message.chat.id) == False:
        db_worker.save_user(message.chat.id)
    else:
        db_worker.reset_user(message.chat.id)
    next_song(message)
    db_worker.close()           
    #rows = utils.get_rows_count()
    #num = message.chat.id    
    #row = db_worker.select_single(random.randint(1, utils.get_rows_count()))
    #markup = utils.generate_markup(row[2], row[3])
    #bot.send_voice(message.chat.id, row[1], reply_markup=markup, duration=20)
    #utils.set_user_game(message.chat.id, row[2])


@bot.message_handler(commands=['next'])
def next_song(message):
    db_worker = SQLighter(config.database_name)
    user = db_worker.get_user(message.chat.id)
    song_order = user[3]
    score = user[2]
    rownum = utils.get_rows_count()
    if song_order >= rownum+1:
        db_worker.reset_user(message.chat.id)
        bot.send_message(message.chat.id, 'Упс! Песни закончились и ваш результат {} угаданных из {}! Чтобы начать игру заново, введите команду /game'.format(score, rownum))
    else:
        song = db_worker.select_single(song_order)
        markup = utils.generate_markup(song[2], song[3])
        bot.send_voice(message.chat.id, song[1], reply_markup=markup)
        utils.set_user_game(message.chat.id, song[2])
    db_worker.close()


@bot.message_handler(func=lambda message: True, content_types=['text'])
def check_answer(message):
    answer = utils.get_answer_for_user(message.chat.id)
    db_worker = SQLighter(config.database_name)
    if not answer:
        bot.send_message(message.chat.id, 'Чтобы начать игру, введите команду /game')
    else:
        keyboard_hider = types.ReplyKeyboardRemove()
        if message.text == answer:
            #f = open('images/correct.png', 'rb')
            bot.send_message(message.chat.id, 'Вы молодец! Попробуйте отгадать еще одну:', reply_markup=keyboard_hider)
            db_worker.add_score(message.chat.id)
        else:
            #f = open('images/wrong.png', 'rb')
            bot.send_message(message.chat.id, 'К сожалению вы не отгадали. Попробуйте следующую песню:)', reply_markup=keyboard_hider)
            db_worker.add_song_id(message.chat.id)
        utils.finish_user_game(message.chat.id)
    next_song(message)
    

if __name__ == '__main__':
    utils.count_rows()
    random.seed()
    bot.polling(none_stop=True)

    

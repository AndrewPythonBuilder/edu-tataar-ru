from telegram import  ReplyKeyboardMarkup
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import constants, test_auth
import logging
import datetime

vk_first = False

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                     level=logging.INFO)
updater = Updater(token=constants.token)
dispatcher = updater.dispatcher

def start(bot, update):
    message = update.message
    bottons = [['Расписание']]
    user_markup = ReplyKeyboardMarkup(bottons)
    bot.send_message(message.chat.id, 'Вечер в хату!) Выбирай действие!', reply_markup=user_markup)


def answer(bot, update):
    today = datetime.date.today()
    global vk_first
    message = update.message
    if message.text == 'Расписание':
        bottons = [['Пн', 'Вт', 'Ср'], ['Чт', 'Пт', 'Сб'], ['Назад, на улице холодно!']]
        user_markup = ReplyKeyboardMarkup(bottons)
        bot.send_message(message.chat.id, 'Ты вышел на улицу. Выбери день недели!', reply_markup=user_markup)
    elif message.text == 'Пн':
        if 0 - today.weekday() <= 0:
            day = datetime.date(year=today.year, month=today.month, day = 7 - today.weekday() + today.day)
            l = test_auth.unix_time(day)
            if l != 'Не удалось':
                e = test_auth.analization(l)
                i = 0
                while i < len(e)-1:
                    pr = ''
                    pr += e[i] + '\n'
                    pr += e[i+1]
                    bot.send_message(message.chat.id, pr)
                    i+=2
            else:
                bot.send_message(message.chat.id, 'Что-то не фартовый ты! Пробуй еще раз')
        else:
            day = datetime.date(year=today.year, month=today.month, day=today.day + 0 - today.weekday())
            l = test_auth.unix_time(day)
            if l != 'Не удалось':
                e = test_auth.analization(l)
                i = 0
                while i < len(e) - 1:
                    pr = ''
                    pr += e[i] + '\n'
                    pr += e[i + 1]
                    bot.send_message(message.chat.id, pr)
                    i += 2
            else:
                bot.send_message(message.chat.id, 'Что-то не фартовый ты! Пробуй еще раз')

    elif message.text == 'Вт':
        if 1 - today.weekday() <= 0:
            day = datetime.date(year=today.year, month=today.month, day = 8 - today.weekday() + today.day)
            l = test_auth.unix_time(day)
            if l != 'Не удалось':
                e = test_auth.analization(l)
                i = 0
                while i < len(e)-1:
                    pr = ''
                    pr += e[i] + '\n'
                    pr += e[i+1]
                    bot.send_message(message.chat.id, pr)
                    i+=2
            else:
                bot.send_message(message.chat.id, 'Что-то не фартовый ты! Пробуй еще раз')
        else:
            day = datetime.date(year=today.year, month=today.month, day=today.day + 1 - today.weekday())
            l = test_auth.unix_time(day)
            if l != 'Не удалось':
                e = test_auth.analization(l)
                i = 0
                while i < len(e) - 1:
                    pr = ''
                    pr += e[i] + '\n'
                    pr += e[i + 1]
                    bot.send_message(message.chat.id, pr)
                    i += 2
            else:
                bot.send_message(message.chat.id, 'Что-то не фартовый ты! Пробуй еще раз')

    elif message.text == 'Ср':
        if 2 - today.weekday() <= 0:
            day = datetime.date(year=today.year, month=today.month, day = 9 - today.weekday() + today.day)
            l = test_auth.unix_time(day)
            if l != 'Не удалось':
                e = test_auth.analization(l)
                i = 0
                while i < len(e)-1:
                    pr = ''
                    pr += e[i] + '\n'
                    pr += e[i+1]
                    bot.send_message(message.chat.id, pr)
                    i+=2
            else:
                bot.send_message(message.chat.id, 'Что-то не фартовый ты! Пробуй еще раз')
        else:
            day = datetime.date(year=today.year, month=today.month, day=today.day + 2 - today.weekday())
            l = test_auth.unix_time(day)
            if l != 'Не удалось':
                e = test_auth.analization(l)
                i = 0
                while i < len(e) - 1:
                    pr = ''
                    pr += e[i] + '\n'
                    pr += e[i + 1]
                    bot.send_message(message.chat.id, pr)
                    i += 2
            else:
                bot.send_message(message.chat.id, 'Что-то не фартовый ты! Пробуй еще раз')

    elif message.text == 'Чт':
        if 3 - today.weekday() <= 0:
            day = datetime.date(year=today.year, month=today.month, day = 10 - today.weekday() + today.day)
            l = test_auth.unix_time(day)
            if l != 'Не удалось':
                e = test_auth.analization(l)
                i = 0
                while i < len(e)-1:
                    pr = ''
                    pr += e[i] + '\n'
                    pr += e[i+1]
                    bot.send_message(message.chat.id, pr)
                    i+=2
            else:
                bot.send_message(message.chat.id, 'Что-то не фартовый ты! Пробуй еще раз')
        else:
            day = datetime.date(year=today.year, month=today.month, day=today.day + 3 - today.weekday())
            l = test_auth.unix_time(day)
            if l != 'Не удалось':
                e = test_auth.analization(l)
                i = 0
                while i < len(e) - 1:
                    pr = ''
                    pr += e[i] + '\n'
                    pr += e[i + 1]
                    bot.send_message(message.chat.id, pr)
                    i += 2
            else:
                bot.send_message(message.chat.id, 'Что-то не фартовый ты! Пробуй еще раз')

    elif message.text == 'Пт':
        if 4 - today.weekday() <= 0:
            day = datetime.date(year=today.year, month=today.month, day = 11 - today.weekday() + today.day)
            l = test_auth.unix_time(day)
            if l != 'Не удалось':
                e = test_auth.analization(l)
                i = 0
                while i < len(e)-1:
                    pr = ''
                    pr += e[i] + '\n'
                    pr += e[i+1]
                    bot.send_message(message.chat.id, pr)
                    i+=2
            else:
                bot.send_message(message.chat.id, 'Что-то не фартовый ты! Пробуй еще раз')
        else:
            day = datetime.date(year=today.year, month=today.month, day=today.day + 4 - today.weekday())
            l = test_auth.unix_time(day)
            if l != 'Не удалось':
                e = test_auth.analization(l)
                i = 0
                while i < len(e) - 1:
                    pr = ''
                    pr += e[i] + '\n'
                    pr += e[i + 1]
                    bot.send_message(message.chat.id, pr)
                    i += 2
            else:
                bot.send_message(message.chat.id, 'Что-то не фартовый ты! Пробуй еще раз')

    elif message.text == 'Сб':
        if 5 - today.weekday() <= 0:
            day = datetime.date(year=today.year, month=today.month, day = 12 - today.weekday() + today.day)
            l = test_auth.unix_time(day)
            if l != 'Не удалось':
                e = test_auth.analization(l)
                i = 0
                while i < len(e)-1:
                    pr = ''
                    pr += e[i] + '\n'
                    pr += e[i+1]
                    bot.send_message(message.chat.id, pr)
                    i+=2
            else:
                bot.send_message(message.chat.id, 'Что-то не фартовый ты! Пробуй еще раз')
        else:
            day = datetime.date(year=today.year, month=today.month, day=today.day + 5 - today.weekday())
            l = test_auth.unix_time(day)
            if l != 'Не удалось':
                e = test_auth.analization(l)
                i = 0
                while i < len(e) - 1:
                    pr = ''
                    pr += e[i] + '\n'
                    pr += e[i + 1]
                    bot.send_message(message.chat.id, pr)
                    i += 2
            else:
                bot.send_message(message.chat.id, 'Что-то не фартовый ты! Пробуй еще раз')

    elif message.text == 'Назад, на улице холодно!':
        bot.send_message(message.chat.id, 'Да, согласен, на улице слишком холодно!')
        message.text = '/start'
        start(bot, update)


start_handler = CommandHandler('start', start)
answer_handler = MessageHandler(Filters.text, answer)
dispatcher.add_handler(start_handler)
dispatcher.add_handler(answer_handler)
updater.start_polling(clean=True, timeout=5 )
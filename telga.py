import math
import json
import os
import random
import telebot
from telebot import types
import requests


bot = telebot.TeleBot("5344951057:AAG3PXM6GfJW_EOzHoLP0V38fc-QUACdI9A")



def log(message, answer):
    print("\n ------------")

    from datetime import datetime

    print(datetime.now())

    print("Сообщение от {0} {1}. (id = {2}) \n Текст - {3}".format(message.from_user.first_name,

                                                                   message.from_user.last_name,

                                                                   str(message.from_user.id),

                                                                   message.text))


@bot.message_handler(commands=["start"])
def handle_start(message):
    user_markup = telebot.types.ReplyKeyboardMarkup(True, False)  # переменная, которая хранит разметку нашей клавиатуры
    markup = telebot.types.ReplyKeyboardMarkup(True,False)
    # 1 - True - для того,чтобы сделать размер клавиатуры поменьше, False - побольше

    # 2 - True - убрать клавиатуру после одного раза пользования

    # user_markup.row('/start', '/stop')  # добавляем команды
    itembtan1=types.KeyboardButton('Я понял, где находится кнопка «Меню кнопок»')
    # user_markup.row('фото', 'аудио', 'документы')  # и ограничиваем размер клавиатуры 3х4
    markup.add(itembtan1)
    mess=f'Добро пожаловать, <b>{message.from_user.first_name}-<u>{message.from_user.last_name}</u></b>'

    mess1='Важно❗\nПри работе с ботом Вы можете закрывать меню с кнопками.\nДля того, чтобы заново открыть «Меню кнопок», нажмите на кнопку, которая находится в поле ввода текста с правой стороны.'

    video=open('C:/Users/Dauletdiyar/Desktop/telegram_bot/gif/gif1.mp4','rb')

    # перед тем, как показать клавиатуру пользователю бот должен отправить сообщение вроде приветствия

    bot.send_message(message.chat.id, mess,parse_mode='html')
    bot.send_video(message.chat.id, video)
    bot.send_message(message.chat.id,mess1,reply_markup=markup)

@bot.message_handler(commands=["stop"])
def handle_start(message):  # функция, которая убирает нашу клавиатуру

    hide_markup = telebot.types.ReplyKeyboardRemove()

    bot.send_message(message.chat.id, '...чтобы начать заново напишите /start...', reply_markup=hide_markup)


@bot.message_handler(content_types=["text"])
def handle_text(message):
    if message.text == 'Я понял, где находится кнопка «Меню кнопок»':
        markup = telebot.types.ReplyKeyboardMarkup(True,False)
        itembtna2 = types.KeyboardButton('🛒 Корзина')
        itembtna3 = types.KeyboardButton('📋 Меню')
        itembtna4 = types.KeyboardButton('🚘 Оформить заказ')
        itembtna5 = types.KeyboardButton('💬 О нас')
        itembtna6 = types.KeyboardButton('📝 Мои заказы')
        itembtna7 = types.KeyboardButton('👩‍💻 Связаться с менеджером')
        markup.row(itembtna3)
        markup.row(itembtna2,itembtna4)
        markup.row(itembtna5)
        markup.row(itembtna6)
        markup.row(itembtna7)
        bot.send_message(message.chat.id,'Отлично! Приятного пользования!',reply_markup=markup)

    elif message.text=='📋 Меню':
        markup = telebot.types.ReplyKeyboardMarkup(True,False)
        itembtna1 = types.KeyboardButton('Бургеры 🍔')
        itembtna2 = types.KeyboardButton('Хот-доги 🌭')
        itembtna3 = types.KeyboardButton('Картофель фри 🍟')
        itembtna4 = types.KeyboardButton('Напитки 🥤')
        itembtna5 = types.KeyboardButton('Соусы 🥫')
        itembtna6 = types.KeyboardButton('Добавки 🧀')
        itembtna7 = types.KeyboardButton('ДАБРО бургер❤')
        itembtna8 = types.KeyboardButton('Комбо🎁')
        itembtna9 = types.KeyboardButton('🚘 Оформить заказ')
        itembtna10 = types.KeyboardButton('📋 Вернуться в меню')
        itembtna11 = types.KeyboardButton('🛒 Корзина')
        markup.row(itembtna1,itembtna2)
        markup.row(itembtna3,itembtna4)
        markup.row(itembtna5,itembtna6)
        markup.row(itembtna7,itembtna8)
        markup.row(itembtna9)
        markup.row(itembtna10,itembtna11)
        bot.send_message(message.chat.id,'Выберите категорию:',reply_markup=markup)
    elif message.text=='Бургеры 🍔':
        photo = open('C:/Users/Dauletdiyar/Desktop/telegram_bot/бургеры фото/1 Гамбургер куриный.jpg', 'rb')
        mess = 'Гамбургер куриный\n''\n''Цена: 890 ₸'
        markup = types.InlineKeyboardMarkup(row_width=1)
        item1=types.InlineKeyboardButton("🔘Добавить",callback_data='question_1')
        markup.add(item1)
        bot.send_photo(message.chat.id, photo,mess,reply_markup=markup)

        photo1 = open('C:/Users/Dauletdiyar/Desktop/telegram_bot/бургеры фото/2 Спать Бургер.jpg', 'rb')
        mess = 'Спать Бургер\n''\n''Цена: 1590 ₸'
        markup = types.InlineKeyboardMarkup(row_width=1)
        item1 = types.InlineKeyboardButton("🔘Добавить", callback_data='question_2')
        markup.add(item1)
        bot.send_photo(message.chat.id, photo1, mess, reply_markup=markup)

        photo2 = open('C:/Users/Dauletdiyar/Desktop/telegram_bot/бургеры фото/3 Гамбургер говяжий.jpg', 'rb')
        mess = 'Гамбургер говяжий\n''\n''Цена: 890 ₸'
        markup = types.InlineKeyboardMarkup(row_width=1)
        item1 = types.InlineKeyboardButton("🔘Добавить", callback_data='question_3')
        markup.add(item1)
        bot.send_photo(message.chat.id, photo2, mess, reply_markup=markup)

        photo3 = open('C:/Users/Dauletdiyar/Desktop/telegram_bot/бургеры фото/4 Чизбургер куриный.jpg', 'rb')
        mess = 'Чизбургер куриный\n''\n''Цена: 990 ₸'
        markup = types.InlineKeyboardMarkup(row_width=1)
        item1 = types.InlineKeyboardButton("🔘Добавить", callback_data='question_4')
        markup.add(item1)
        bot.send_photo(message.chat.id, photo3, mess, reply_markup=markup)

        photo4 = open('C:/Users/Dauletdiyar/Desktop/telegram_bot/бургеры фото/5 Чизбургер говяжий.jpg', 'rb')
        mess = 'Чизбургер говяжий\n''\n''Цена: 990 ₸'
        markup = types.InlineKeyboardMarkup(row_width=1)
        item1 = types.InlineKeyboardButton("🔘Добавить", callback_data='question_5')
        markup.add(item1)
        bot.send_photo(message.chat.id, photo4, mess, reply_markup=markup)

        photo5 = open('C:/Users/Dauletdiyar/Desktop/telegram_bot/бургеры фото/6 Гамбургер куриный двойной.jpg', 'rb')
        mess = 'Гамбургер куриный двойной\n''\n''Цена: 1190 ₸'
        markup = types.InlineKeyboardMarkup(row_width=1)
        item1 = types.InlineKeyboardButton("🔘Добавить", callback_data='question_6')
        markup.add(item1)
        bot.send_photo(message.chat.id, photo5, mess, reply_markup=markup)

        photo6 = open('C:/Users/Dauletdiyar/Desktop/telegram_bot/бургеры фото/7 Чизбургер куриный двойной.jpg', 'rb')
        mess = 'Чизбургер куриный двойной\n''\n''Цена: 1290 ₸'
        markup = types.InlineKeyboardMarkup(row_width=1)
        item1 = types.InlineKeyboardButton("🔘Добавить", callback_data='question_7')
        markup.add(item1)
        bot.send_photo(message.chat.id, photo6, mess, reply_markup=markup)

        photo7 = open('C:/Users/Dauletdiyar/Desktop/telegram_bot/бургеры фото/8 Чизбургер говяжий двойной.jpg', 'rb')
        mess = 'Чизбургер говяжий двойной\n''\n''Цена: 1290 ₸'
        markup = types.InlineKeyboardMarkup(row_width=1)
        item1 = types.InlineKeyboardButton("🔘Добавить", callback_data='question_8')
        markup.add(item1)
        bot.send_photo(message.chat.id, photo7, mess, reply_markup=markup)

        photo8 = open('C:/Users/Dauletdiyar/Desktop/telegram_bot/бургеры фото/9 Гамбургер микс.jpg', 'rb')
        mess = 'Гамбургер микс\n''\n''Цена: 1190 ₸'
        markup = types.InlineKeyboardMarkup(row_width=1)
        item1 = types.InlineKeyboardButton("🔘Добавить", callback_data='question_9')
        markup.add(item1)
        bot.send_photo(message.chat.id, photo8, mess, reply_markup=markup)

        photo9 = open('C:/Users/Dauletdiyar/Desktop/telegram_bot/бургеры фото/10 Чизбургер микс.jpg', 'rb')
        mess = 'Чизбургер микс\n''\n''Цена: 1290 ₸'
        markup = types.InlineKeyboardMarkup(row_width=1)
        item1 = types.InlineKeyboardButton("🔘Добавить", callback_data='question_10')
        markup.add(item1)
        bot.send_photo(message.chat.id, photo9, mess, reply_markup=markup)

        photo10 = open('C:/Users/Dauletdiyar/Desktop/telegram_bot/бургеры фото/11 Гамбургер говяжий двойной.jpg', 'rb')
        mess = 'Гамбургер говяжий двойной\n''\n''Цена: 1190 ₸'
        markup = types.InlineKeyboardMarkup(row_width=1)
        item1 = types.InlineKeyboardButton("🔘Добавить", callback_data='question_11')
        markup.add(item1)
        bot.send_photo(message.chat.id, photo10, mess, reply_markup=markup)

    elif message.text=='Хот-доги 🌭':

        photo1 = open('C:/Users/Dauletdiyar/Desktop/telegram_bot/хот-дог/1 хотдог.jpg', 'rb')
        mess = 'Хот-дог(острый)\n''\n''Цена: 790 ₸'
        markup = types.InlineKeyboardMarkup(row_width=1)
        item1 = types.InlineKeyboardButton("🔘Добавить", callback_data='question_hot1')
        markup.add(item1)
        bot.send_photo(message.chat.id, photo1, mess, reply_markup=markup)

        photo1 = open('C:/Users/Dauletdiyar/Desktop/telegram_bot/хот-дог/1 хотдог.jpg', 'rb')
        mess = 'Хот-дог\n''\n''Цена: 790 ₸'
        markup = types.InlineKeyboardMarkup(row_width=1)
        item1 = types.InlineKeyboardButton("🔘Добавить", callback_data='question_hot2')
        markup.add(item1)
        bot.send_photo(message.chat.id, photo1, mess, reply_markup=markup)

    elif message.text=='Картофель фри 🍟':
        photo1 = open('C:/Users/Dauletdiyar/Desktop/telegram_bot/фри/1 фри.jpg', 'rb')
        mess = 'Картофель фри\n''\n''Цена: 550 ₸'
        markup = types.InlineKeyboardMarkup(row_width=1)
        item1 = types.InlineKeyboardButton("🔘Добавить", callback_data='question_fri1')
        markup.add(item1)
        bot.send_photo(message.chat.id, photo1, mess, reply_markup=markup)

    elif message.text=='Напитки 🥤':
        photo1 = open('C:/Users/Dauletdiyar/Desktop/telegram_bot/напитки/1.jpg', 'rb')
        mess = 'Coca-cola 0.5\n''\n''Цена: 390 ₸'
        markup = types.InlineKeyboardMarkup(row_width=1)
        item1 = types.InlineKeyboardButton("🔘Добавить", callback_data='question_drink1')
        markup.add(item1)
        bot.send_photo(message.chat.id, photo1, mess, reply_markup=markup)

        photo2 = open('C:/Users/Dauletdiyar/Desktop/telegram_bot/напитки/2.jpg', 'rb')
        mess = 'Fanta 0.5\n''\n''Цена: 390 ₸'
        markup = types.InlineKeyboardMarkup(row_width=1)
        item1 = types.InlineKeyboardButton("🔘Добавить", callback_data='question_drink2')
        markup.add(item1)
        bot.send_photo(message.chat.id, photo2, mess, reply_markup=markup)

        photo3 = open('C:/Users/Dauletdiyar/Desktop/telegram_bot/напитки/3.jpg', 'rb')
        mess = 'Sprite 0.5\n''\n''Цена: 390 ₸'
        markup = types.InlineKeyboardMarkup(row_width=1)
        item1 = types.InlineKeyboardButton("🔘Добавить", callback_data='question_drink3')
        markup.add(item1)
        bot.send_photo(message.chat.id, photo3, mess, reply_markup=markup)

        photo4 = open('C:/Users/Dauletdiyar/Desktop/telegram_bot/напитки/4.jpg', 'rb')
        mess = 'Fuse tea 0.5\n''\n''Цена: 390 ₸'
        markup = types.InlineKeyboardMarkup(row_width=1)
        item1 = types.InlineKeyboardButton("🔘Добавить", callback_data='question_drink4')
        markup.add(item1)
        bot.send_photo(message.chat.id, photo4, mess, reply_markup=markup)

        mess='Bon Aqua 0.5\n''\n''Цена: 290 ₸'
        markup = types.InlineKeyboardMarkup(row_width=1)
        item1 = types.InlineKeyboardButton("🔘Добавить", callback_data='question_drink5')
        markup.add(item1)
        bot.send_message(message.chat.id, mess,reply_markup=markup)

        photo5 = open('C:/Users/Dauletdiyar/Desktop/telegram_bot/напитки/5.jpg', 'rb')
        mess = 'Малиновый компот\n''\n''Цена: 290 ₸'
        markup = types.InlineKeyboardMarkup(row_width=1)
        item1 = types.InlineKeyboardButton("🔘Добавить", callback_data='question_drink6')
        markup.add(item1)
        bot.send_photo(message.chat.id, photo5, mess, reply_markup=markup)

        photo6 = open('C:/Users/Dauletdiyar/Desktop/telegram_bot/напитки/6.jpg', 'rb')
        mess = 'Компот из смородины\n''Вкусный Домашний Компот со свежими ягодами смородины''\n''Цена: 290 ₸'
        markup = types.InlineKeyboardMarkup(row_width=1)
        item1 = types.InlineKeyboardButton("🔘Добавить", callback_data='question_drink7')
        markup.add(item1)
        bot.send_photo(message.chat.id, photo6, mess, reply_markup=markup)

        photo7 = open('C:/Users/Dauletdiyar/Desktop/telegram_bot/напитки/7.jpg', 'rb')
        mess = 'Piko pulpy 0.5\n''\n''Цена: 450 ₸'
        markup = types.InlineKeyboardMarkup(row_width=1)
        item1 = types.InlineKeyboardButton("🔘Добавить", callback_data='question_drink8')
        markup.add(item1)
        bot.send_photo(message.chat.id, photo7, mess, reply_markup=markup)

    elif message.text=='Соусы 🥫':
        photo1 = open('C:/Users/Dauletdiyar/Desktop/telegram_bot/соусы/1.jpg', 'rb')
        mess = 'Кетчуп\n''\n''Цена: 150 ₸'
        markup = types.InlineKeyboardMarkup(row_width=1)
        item1 = types.InlineKeyboardButton("🔘Добавить", callback_data='question_sauce1')
        markup.add(item1)
        bot.send_photo(message.chat.id, photo1, mess, reply_markup=markup)

        photo2 = open('C:/Users/Dauletdiyar/Desktop/telegram_bot/соусы/2.jpg', 'rb')
        mess = 'Соус сырный\n''\n''Цена: 150 ₸'
        markup = types.InlineKeyboardMarkup(row_width=1)
        item1 = types.InlineKeyboardButton("🔘Добавить", callback_data='question_sauce2')
        markup.add(item1)
        bot.send_photo(message.chat.id, photo2, mess, reply_markup=markup)

        photo3 = open('C:/Users/Dauletdiyar/Desktop/telegram_bot/соусы/3.jpg', 'rb')
        mess = 'Соус BBQ\n''\n''Цена: 150 ₸'
        markup = types.InlineKeyboardMarkup(row_width=1)
        item1 = types.InlineKeyboardButton("🔘Добавить", callback_data='question_sauce3')
        markup.add(item1)
        bot.send_photo(message.chat.id, photo3, mess, reply_markup=markup)

        photo4 = open('C:/Users/Dauletdiyar/Desktop/telegram_bot/соусы/4.jpg', 'rb')
        mess = 'Соус острый\n''\n''Цена: 100 ₸'
        markup = types.InlineKeyboardMarkup(row_width=1)
        item1 = types.InlineKeyboardButton("🔘Добавить", callback_data='question_sauce4')
        markup.add(item1)
        bot.send_photo(message.chat.id, photo4, mess, reply_markup=markup)

        photo5 = open('C:/Users/Dauletdiyar/Desktop/telegram_bot/соусы/5.jpg', 'rb')
        mess = 'Соус горчичный\n''\n''Цена: 150 ₸'
        markup = types.InlineKeyboardMarkup(row_width=1)
        item1 = types.InlineKeyboardButton("🔘Добавить", callback_data='question_sauce5')
        markup.add(item1)
        bot.send_photo(message.chat.id, photo5, mess, reply_markup=markup)

    elif message.text=='Добавки 🧀':

        photo1 = open('C:/Users/Dauletdiyar/Desktop/telegram_bot/add/1.jpg', 'rb')
        mess = 'Халапеньо\n''\n''Цена: 150 ₸'
        markup = types.InlineKeyboardMarkup(row_width=1)
        item1 = types.InlineKeyboardButton("🔘Добавить", callback_data='question_add1')
        markup.add(item1)
        bot.send_photo(message.chat.id, photo1, mess, reply_markup=markup)

        photo2 = open('C:/Users/Dauletdiyar/Desktop/telegram_bot/add/2.jpg', 'rb')
        mess = 'Сыр\n''\n''Цена: 150 ₸'
        markup = types.InlineKeyboardMarkup(row_width=1)
        item1 = types.InlineKeyboardButton("🔘Добавить", callback_data='question_add2')
        markup.add(item1)
        bot.send_photo(message.chat.id, photo2, mess, reply_markup=markup)

    elif message.text=='ДАБРО бургер❤':

        photo1 = open('C:/Users/Dauletdiyar/Desktop/telegram_bot/love/1.jpg', 'rb')
        mess = 'ДАБРО бургер\n''\n''Ваши 200 тенге помогут семье обрести новый дом!\n''\n''Цена: 200 ₸'
        markup = types.InlineKeyboardMarkup(row_width=1)
        item1 = types.InlineKeyboardButton("🔘Добавить", callback_data='question_love1')
        markup.add(item1)
        bot.send_photo(message.chat.id, photo1, mess, reply_markup=markup)

    elif message.text=='Комбо🎁':

        photo1 = open('C:/Users/Dauletdiyar/Desktop/telegram_bot/kombo/1.jpg', 'rb')
        mess = 'Комбо для двоих №1\n''\n''Чизбургер куриный + Чизбургер говяжий + 2 фри + 2 напитка ассортименте\n''\n''Цена: 2790 ₸'
        markup = types.InlineKeyboardMarkup(row_width=1)
        item1 = types.InlineKeyboardButton("🔘Добавить", callback_data='question_kombo1')
        markup.add(item1)
        bot.send_photo(message.chat.id, photo1, mess, reply_markup=markup)

        photo2 = open('C:/Users/Dauletdiyar/Desktop/telegram_bot/kombo/2.jpg', 'rb')
        mess = 'Спать комбо для двоих\n''\n''Спать бургер говяжий + Спать бургер говяжий + 2 фри + 2 напитка ассортименте\n''\n''Цена: 3990 ₸'
        markup = types.InlineKeyboardMarkup(row_width=1)
        item1 = types.InlineKeyboardButton("🔘Добавить", callback_data='question_kombo2')
        markup.add(item1)
        bot.send_photo(message.chat.id, photo2, mess, reply_markup=markup)

        photo3 = open('C:/Users/Dauletdiyar/Desktop/telegram_bot/kombo/3.jpg', 'rb')
        mess = 'Спать комбо\n''\n''Спать бургер + картофель фри + напиток в ассортименте\n''\n''Цена: 2090 ₸'
        markup = types.InlineKeyboardMarkup(row_width=1)
        item1 = types.InlineKeyboardButton("🔘Добавить", callback_data='question_kombo3')
        markup.add(item1)
        bot.send_photo(message.chat.id, photo3, mess, reply_markup=markup)

        photo4 = open('C:/Users/Dauletdiyar/Desktop/telegram_bot/kombo/4.jpg', 'rb')
        mess = 'Чизбургер Комбо (куриный)\n''\n''Чизбургер куриный + напиток + фри в ассортименте\n''\n''Цена: 1590 ₸'
        markup = types.InlineKeyboardMarkup(row_width=1)
        item1 = types.InlineKeyboardButton("🔘Добавить", callback_data='question_kombo4')
        markup.add(item1)
        bot.send_photo(message.chat.id, photo4, mess, reply_markup=markup)

        photo5 = open('C:/Users/Dauletdiyar/Desktop/telegram_bot/kombo/5.jpg', 'rb')
        mess = 'Чизбургер Комбо (говяжий)\n''\n''Чизбургер говяжий + фри + напиток в ассортименте\n''\n''Цена: 1590 ₸'
        markup = types.InlineKeyboardMarkup(row_width=1)
        item1 = types.InlineKeyboardButton("🔘Добавить", callback_data='question_kombo5')
        markup.add(item1)
        bot.send_photo(message.chat.id, photo5, mess, reply_markup=markup)

        photo6 = open('C:/Users/Dauletdiyar/Desktop/telegram_bot/kombo/6.jpg', 'rb')
        mess = 'Комбо для двоих №2\n''\n''2 Чизбургера говяжий + 2 фри + 2 напитка в ассортименте\n''\n''Цена: 2790 ₸'
        markup = types.InlineKeyboardMarkup(row_width=1)
        item1 = types.InlineKeyboardButton("🔘Добавить", callback_data='question_kombo6')
        markup.add(item1)
        bot.send_photo(message.chat.id, photo6, mess, reply_markup=markup)

        photo7 = open('C:/Users/Dauletdiyar/Desktop/telegram_bot/kombo/7.jpg', 'rb')
        mess = 'Комбо для двоих №3\n''\n''2 Чизбургера куриных + 2 фри + 2 напитка в ассортименте\n''\n''Цена: 2790 ₸'
        markup = types.InlineKeyboardMarkup(row_width=1)
        item1 = types.InlineKeyboardButton("🔘Добавить", callback_data='question_kombo7')
        markup.add(item1)
        bot.send_photo(message.chat.id, photo7, mess, reply_markup=markup)

    elif message.text=='📋 Вернуться в меню':

        markup = telebot.types.ReplyKeyboardMarkup(True, False)
        itembtna2 = types.KeyboardButton('🛒 Корзина')
        itembtna3 = types.KeyboardButton('📋 Меню')
        itembtna4 = types.KeyboardButton('🚘 Оформить заказ')
        itembtna5 = types.KeyboardButton('💬 О нас')
        itembtna6 = types.KeyboardButton('📝 Мои заказы')
        itembtna7 = types.KeyboardButton('👩‍💻 Связаться с менеджером')
        markup.row(itembtna3)
        markup.row(itembtna2, itembtna4)
        markup.row(itembtna5)
        markup.row(itembtna6)
        markup.row(itembtna7)
        mess='Чат-бот службы доставки SALAM BRO (Алматы)\nДоставка по городу Тараз и Астана не осуществляется\nМы работаем только в Алматы\n''\n''Минимальная сумма заказа 2000 тенге\n''\n''Стоимость доставки 600 тенге до вашего адреса\nСтоимость доставки (22:00-10:00) 800 тенге до вашего адреса'
        bot.send_message(message.chat.id, mess,reply_markup=markup)

    elif message.text=='💬 О нас':

        mess='SALAM BRO - это сеть местных, народных бургеров и хот-догов, быстро набравшая популярность, за счет уникального рецепта, качественных продуктов и доступных цен.'
        bot.send_message(message.chat.id,mess)

    elif message.text=='🚘 Оформить заказ':
        mess1='Ваша корзина пуста:'
        bot.send_message(message.chat.id, mess1)

    elif message.text=='👩‍💻 Связаться с менеджером':
        mess2='С вами свяжется менеджер в ближайшие время'
        bot.send_message(message.chat.id, mess2)

    elif message.text=='📝 Мои заказы':
        mess='У вас нет заказов'
        bot.send_message(message.chat.id,mess)

    elif message.text=='🚘 Оформить заказ':
        mess='Ваша корзина пуста:'
        bot.send_message(message.chat.id, mess)

    else:
        mess='я не могу понять вас'
        bot.send_message(message.chat.id,mess)

# @bot.callback_query_handler(func=lambda call:True)
# def callback(call):
#     if call.message:
#         if call.data == 'question_love1':
#             hide_markup=telebot.types.ReplyKeyboardRemove()
#             markup = types.InlineKeyboardMarkup(True,False)
#             item1=types.InlineKeyboardButton('1',callback_data='question_love1n')
#             item2 = types.InlineKeyboardButton('2', callback_data='question_love2n')
#             item3 = types.InlineKeyboardButton('3', callback_data='question_love3n')
#             item4 = types.InlineKeyboardButton('4', callback_data='question_love4n')
#             item5 = types.InlineKeyboardButton('5', callback_data='question_love5n')
#             item6 = types.InlineKeyboardButton('<', callback_data='question_love6n')
#             item7 = types.InlineKeyboardButton('>', callback_data='question_love7n')
#             item8 = types.InlineKeyboardButton('назад', callback_data='question_love8n')
#             markup.row(item1,item2)
#             markup.row(item3,item4,item5)
#             markup.row(item6,item7)
#             markup.row(item8)
#             mess='kek'
#             bot.send_message(call.message.chat.id,'kek',reply_markup=markup)




bot.polling(none_stop=True, interval=0)



# @bot.message_handler(commands=['start'])
# def start(message):
#     mess=f'Hello, <b>{message.from_user.first_name}-<u>{message.from_user.last_name}</u></b>'
#     bot.send_message(message.chat.id,mess,parse_mode='html')
#
#
# @bot.message_handler(content_types=['photo'])
# def get_user_photo(message):
#     bot.send_message(message.chat.id,'Wow,why do I need this Im a bot!')
#
# @bot.message_handler(commands=['website'])
# def website(message):
#     markup=types.InlineKeyboardMarkup()
#     markup.add(types.InlineKeyboardButton("join site",url="https://dnd.su"))
#     bot.send_message(message.chat.id, 'go site',reply_markup=markup)
#
# @bot.message_handler(commands=['help'])
# def website(message):
#     markup=types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
#     websyte=types.KeyboardButton('Web site')
#     start=types.KeyboardButton('Start')
#     markup.add(websyte,start)
#     bot.send_message(message.chat.id, 'what hapend?',reply_markup=markup)
#
# @bot.message_handler(commands=["stop"])
# def handle_start(message):  # функция, которая убирает нашу клавиатуру
#     hide_markup = telebot.types.ReplyKeyboardRemove()
#     bot.send_message(message.chat.id, '...', reply_markup=hide_markup)
#
#
# @bot.message_handler(content_types=['text'])
# def get_user_text(message):
#     if message.text=="Hello":
#         bot.send_message(message.chat.id,"Hello ther!",parse_mode='html')
#     elif message.text=="Web site":
#         markup = types.InlineKeyboardMarkup()
#         markup.add(types.InlineKeyboardButton("join site", url="https://dnd.su"))
#         bot.send_message(message.chat.id, 'go site', reply_markup=markup)
#     elif message.text=="id":
#         bot.send_message(message.chat.id,f"You ID:{message.from_user.id}",parse_mode='html')
#     elif message.text=="photo":
#         photo=open('C:/Users/Dauletdiyar/PycharmProjects/telegramBot/ChillHouse.jpg','rb')
#         bot.send_photo(message.chat.id,photo)
#     elif message.text=="overwatch":
#         video =open('C:/Users/Dauletdiyar/Documents/Overwatch/videos/overwatch/lol.mp4','rb')
#         bot.send_video(message.chat.id, video)
#     elif message.text == 'аудио':
#         directory = 'C:/Users/Dauletdiyar/Desktop/telegram_bot/аудио'
#         all_files_in_directory = os.listdir(directory)
#         random_file = random.choice(all_files_in_directory)
#         img = open(directory + '/' + random_file, 'rb')
#         bot.send_chat_action(message.from_user.id, 'upload_audio')
#         bot.send_audio(message.chat.id, img)
#         img.close()
#     elif  message.text == 'фото':
#         directory = 'C:/Users/Dauletdiyar/Pictures/фртк'
#         all_files_in_directory = os.listdir(directory)
#         random_file = random.choice(all_files_in_directory)
#         img = open(directory + '/' + random_file, 'rb')
#         bot.send_chat_action(message.from_user.id, 'upload_photo')
#         bot.send_photo(message.chat.id, img)
#         img.close()
#     elif message.text.lower() == "привет":
#         answer = f'Приветствую,<b>{message.from_user.first_name}</b>'
#         bot.send_message(message.chat.id, answer,parse_mode='html')
#     else:
#         bot.send_message(message.chat.id,"WTF",parse_mode='html')
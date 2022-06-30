import telebot
from telebot import types

tokenTxt = open('sgu_bot_token.txt', 'r')
bot = telebot.TeleBot(tokenTxt.read())

# Start Message
@bot.message_handler(commands = ['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
    startMessage = f'Привет, <b>{message.from_user.first_name} {message.from_user.last_name}</b>!'

    button1 = types.KeyboardButton('Каталог 🎓')
    button2 = types.KeyboardButton('Помощь ❔')

    markup.add(button1, button2)

    bot.send_message(message.chat.id, startMessage, parse_mode = 'html', reply_markup = markup)


# Reply For Buttons
@bot.message_handler(content_types = ['text'])
def reply(message):
    if message.chat.type == 'private':

    # ---------------------- Основная навигация -------------------------------

        # Каталог (выбор семестра)
        if (message.text == 'Каталог 🎓') or (message.text == '⬅ Выбор семестра'):
            changeSemestr(message)

        # Помощь
        elif message.text == 'Помощь ❔':
            help(message)

        # Меню
        elif message.text == '⬅ Назад':
            menu(message)


    # ---------------------- 1 Семестр -------------------------------

        # 1 Семестр
        elif (message.text == '1 Семестр 🍁') or (message.text == '⬅ 1 Семестр'):
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)

            button1 = types.KeyboardButton('Матан 😡')
            button2 = types.KeyboardButton('Прога 👨‍💻')
            button3 = types.KeyboardButton('Алгем 📐')
            button4 = types.KeyboardButton('Физра 🏃')
            button5 = types.KeyboardButton('Русский 📝')
            button6 = types.KeyboardButton('История 🏛')
            button7 = types.KeyboardButton('ТИ 🧮')
            button8 = types.KeyboardButton('Английский 🇬🇧')
            buttonBack = types.KeyboardButton('⬅ Выбор семестра')

            markup.add(button1, button2, button3, button4, button5, button6, button7, button8, buttonBack)

            bot.send_message(message.chat.id, 'Выбери предмет 📚', reply_markup=markup)


        # Прога 1
        elif message.text == 'Прога 👨‍💻':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)

            button1 = types.KeyboardButton('Базовые эл-ты языка')
            button2 = types.KeyboardButton('Базовые операторы')
            button3 = types.KeyboardButton('Задачи на ряды')
            button4 = types.KeyboardButton('Массивы')
            button5 = types.KeyboardButton('Функции')
            button6 = types.KeyboardButton('Сложные типы данных')
            button7 = types.KeyboardButton('Факультатив')
            button8 = types.KeyboardButton('Контрольная работа')
            buttonBack = types.KeyboardButton('⬅ 1 Семестр')

            markup.add(button1, button2, button3, button4, button5, button6, button7, button8, buttonBack)

            bot.send_message(message.chat.id, 'Выбери задание 📚', reply_markup=markup)

        # Прога 1 (задания)
        elif message.text == 'Базовые эл-ты языка':
            markup = types.InlineKeyboardMarkup()
            markup.add(types.InlineKeyboardButton("Оплатить 💵", url="https://google.com"))
            bot.send_message(message.chat.id, 'Стоимость: <b>200₽</b> \nПримечание: задания 1, 2, 3', parse_mode='html', reply_markup=markup)
        elif message.text == 'Базовые операторы':
            markup = types.InlineKeyboardMarkup()
            markup.add(types.InlineKeyboardButton("Оплатить 💵", url="https://google.com"))
            bot.send_message(message.chat.id, 'Стоимость: <b>200₽</b> \nПримечание: задания 1, 2, 3', parse_mode='html', reply_markup=markup)
        elif message.text == 'Задачи на ряды':
            markup = types.InlineKeyboardMarkup()
            markup.add(types.InlineKeyboardButton("Оплатить 💵", url="https://google.com"))
            bot.send_message(message.chat.id, 'Стоимость: <b>300₽</b> \nПримечание: задания 1, 2, 3', parse_mode='html', reply_markup=markup)
        elif message.text == 'Массивы':
            markup = types.InlineKeyboardMarkup()
            markup.add(types.InlineKeyboardButton("Оплатить 💵", url="https://google.com"))
            bot.send_message(message.chat.id, 'Стоимость: <b>300₽</b> \nПримечание: задания 1, 2, 3', parse_mode='html', reply_markup=markup)
        elif message.text == 'Функции':
            markup = types.InlineKeyboardMarkup()
            markup.add(types.InlineKeyboardButton("Оплатить 💵", url="https://google.com"))
            bot.send_message(message.chat.id, 'Стоимость: <b>300₽</b> \nПримечание: задания 1, 2, 3', parse_mode='html', reply_markup=markup)
        elif message.text == 'Сложные типы данных':
            markup = types.InlineKeyboardMarkup()
            markup.add(types.InlineKeyboardButton("Оплатить 💵", url="https://google.com"))
            bot.send_message(message.chat.id, 'Стоимость: <b>300₽</b> \nПримечание: задания 1, 2, 3', parse_mode='html', reply_markup=markup)
        elif message.text == 'Факультатив':
            markup = types.InlineKeyboardMarkup()
            markup.add(types.InlineKeyboardButton("Оплатить 💵", url="https://google.com"))
            bot.send_message(message.chat.id, 'Стоимость: <b>300₽</b> \nПримечание: задания 1, 2, 3', parse_mode='html', reply_markup=markup)
        elif message.text == 'Контрольная работа':
            markup = types.InlineKeyboardMarkup()
            markup.add(types.InlineKeyboardButton("Оплатить 💵", url="https://google.com"))
            bot.send_message(message.chat.id, 'Стоимость: <b>800₽</b> \nПримечание: задания 1, 2, 3', parse_mode='html', reply_markup=markup)


        # Физра 1
        elif message.text == 'Физра 🏃':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)

            button1 = types.KeyboardButton('Реферат 🏋️‍♂️')
            buttonBack = types.KeyboardButton('⬅ 1 Семестр')

            markup.add(button1, buttonBack)

            bot.send_message(message.chat.id, 'Выбери задание 📚', reply_markup=markup)


        # ТИ 1
        elif message.text == 'ТИ 🧮':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)

            button1 = types.KeyboardButton('КР 📟')
            button2 = types.KeyboardButton('Экзамен 💾')
            buttonBack = types.KeyboardButton('⬅ 1 Семестр')

            markup.add(button1, button2, buttonBack)

            bot.send_message(message.chat.id, 'Выбери задание 📚', reply_markup=markup)


        # История 1
        elif message.text == 'История 🏛':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)

            button1 = types.KeyboardButton('Реферат 📜')
            button2 = types.KeyboardButton('Тест 🏟')
            button3 = types.KeyboardButton('Конспекты 🗿')
            buttonBack = types.KeyboardButton('⬅ 1 Семестр')

            markup.add(button1, button2, button3, buttonBack)

            bot.send_message(message.chat.id, 'Выбери задание 📚', reply_markup=markup)


    # ---------------------- 2 Семестр -------------------------------

        # 2 Семестр
        elif (message.text == '2 Семестр 🌷') or (message.text == '⬅ 2 Семестр'):
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)

            button1 = types.KeyboardButton('Матан 🔢')
            button2 = types.KeyboardButton('Прога ‍🧑‍💻')
            button3 = types.KeyboardButton('Алгем 📏')
            button4 = types.KeyboardButton('Физра 🏃‍♂️')
            button5 = types.KeyboardButton('Матлог 🔣')
            button6 = types.KeyboardButton('ВВС 🗣')
            button7 = types.KeyboardButton('Физика 💡')
            button8 = types.KeyboardButton('СИТ 💻')
            button9 = types.KeyboardButton('Английский 🔤')
            buttonBack = types.KeyboardButton('⬅ Выбор семестра')

            markup.add(button1, button2, button3, button4, button5, button6, button7, button8, button9, buttonBack)

            bot.send_message(message.chat.id, 'Выбери предмет 📚', reply_markup=markup)


        # Прога 2
        elif message.text == 'Прога ‍🧑‍💻':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)

            button1 = types.KeyboardButton('Работа с STL')
            button2 = types.KeyboardButton('Сортировки')
            button3 = types.KeyboardButton('Динамические структуры')
            button4 = types.KeyboardButton('Деревья')
            button5 = types.KeyboardButton('Графы')
            button6 = types.KeyboardButton('Хэширование')
            button7 = types.KeyboardButton('Алгоритмы')
            button8 = types.KeyboardButton('КР 📄')
            buttonBack = types.KeyboardButton('⬅ 2 Семестр')

            markup.add(button1, button2, button3, button4, button5, button6, button7, button8, buttonBack)

            bot.send_message(message.chat.id, 'Выбери задание 📚', reply_markup=markup)


        # Физра 2
        elif message.text == 'Физра 🏃‍♂️':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)

            button1 = types.KeyboardButton('Тест ⛷')
            button2 = types.KeyboardButton('Реферат 🏋️‍♀️')
            buttonBack = types.KeyboardButton('⬅ 2 Семестр')

            markup.add(button1, button2, buttonBack)

            bot.send_message(message.chat.id, 'Выбери задание 📚', reply_markup=markup)


        # ВВС 2
        elif message.text == 'ВВС 🗣':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)

            button1 = types.KeyboardButton('Словарь 📕')
            buttonBack = types.KeyboardButton('⬅ 2 Семестр')

            markup.add(button1, buttonBack)

            bot.send_message(message.chat.id, 'Выбери задание 📚', reply_markup=markup)

        # ВВС 2 (задания)
        elif message.text == 'Словарь 📕':
            markup = types.InlineKeyboardMarkup()
            markup.add(types.InlineKeyboardButton("Оплатить 💵", url="https://google.com"))
            bot.send_message(message.chat.id, 'Стоимость: <b>300₽</b> \nПримечание: 2 примера, оцененные на макс. балл', parse_mode='html', reply_markup=markup)


        # СИТ 2
        elif message.text == 'СИТ 💻':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)

            button1 = types.KeyboardButton('Терминал')
            button2 = types.KeyboardButton('Ветки и форки')
            button3 = types.KeyboardButton('Работа с Git')
            button4 = types.KeyboardButton('Создание текста в LaTeX')
            button5 = types.KeyboardButton('Форматирование текста в LaTeX')
            button6 = types.KeyboardButton('Формулы в LaTeX')
            buttonBack = types.KeyboardButton('⬅ 2 Семестр')

            markup.add(button1, button2, button3, button4, button5, button6, buttonBack)

            bot.send_message(message.chat.id, 'Выбери задание 📚', reply_markup=markup)


def changeSemestr(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)

    button1 = types.KeyboardButton('1 Семестр 🍁')
    button2 = types.KeyboardButton('2 Семестр 🌷')
    buttonBack = types.KeyboardButton('⬅ Назад')

    markup.add(button1, button2, buttonBack)

    bot.send_message(message.chat.id, 'Выбери семестр 📅', reply_markup=markup)

def menu(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)

    button1 = types.KeyboardButton('Каталог 🎓')
    button2 = types.KeyboardButton('Помощь ❔')

    markup.add(button1, button2)

    bot.send_message(message.chat.id, 'Меню 📋', reply_markup=markup)

def help(message):
    bot.send_message(message.chat.id, 'Помощь')

bot.polling(none_stop = True)
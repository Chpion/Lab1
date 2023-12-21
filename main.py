import telebot
from telebot import types

bot = telebot.TeleBot('6563748370:AAGtx-zv_TmlUqCsmBbZEfHFabwJvl3Spnc')

count = 0

def rise_count():
    global count
    count += 1

@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup()
    btn1 = types.KeyboardButton('Начать тест')
    markup.row(btn1)
    bot.send_message(message.chat.id, 'Хотите начать прохождение теста?',reply_markup=markup)
    bot.register_next_step_handler(message, test1)

@bot.message_handler()
def test1(message):
    if message.text == 'Начать тест' or message.text == 'Попробовать заново':
        global count
        count = 0
        bot.register_next_step_handler(message, test1)
        markup = types.ReplyKeyboardMarkup()
        btn1 = types.KeyboardButton('Любой числовой результат эксперимента со случайными исходами')
        btn2 = types.KeyboardButton('Величина, принимающая любое значение некоторого промежутка [x1;x2)')
        btn3 = types.KeyboardButton('Величина, множество значений которой конечно или счётно')
        markup.row(btn1)
        markup.row(btn2)
        markup.row(btn3)
        bot.send_message(message.chat.id, 'Вопрос№1\nЧто такое дискретная случайная величиниа?', reply_markup=markup)
        bot.register_next_step_handler(message, test2)
    elif message.text == 'Закончить':
        bot.send_message(message.chat.id, 'Спасибо, что прошли наш тест!')


@bot.message_handler()
def test2(message):
    if message.text == 'Величина, множество значений которой конечно или счётно':
        bot.send_message(message.chat.id, 'Правильно!')
        rise_count()
    else:
        bot.send_message(message.chat.id, 'Неравильно!')
    markup = types.ReplyKeyboardMarkup()
    btn1 = types.KeyboardButton('Вероятность того что случайная величина Х откажется меньше некоторой некоторого х')
    btn2 = types.KeyboardButton('Ломанная, соединяющая точки с координатами (xi, рi  )')
    btn3 = types.KeyboardButton('Таблица, 1 строка = возможные значение xi , а другая - вероятности  рi  события, состоящего в том, что случайная величина примет значение  xi')
    markup.row(btn1)
    markup.row(btn2)
    markup.row(btn3)
    bot.send_message(message.chat.id, 'Вопрос№2\nЧто такое Функция распределения?', reply_markup=markup)
    bot.register_next_step_handler(message, test3)

@bot.message_handler()
def test3(message):
    if message.text == 'Вероятность того что случайная величина Х откажется меньше некоторой некоторого х':
        bot.send_message(message.chat.id, 'Правильно!')
        rise_count()
    else:
        bot.send_message(message.chat.id, 'Неравильно!')
    markup = types.ReplyKeyboardMarkup()
    btn1 = types.KeyboardButton('Значения функции лежат в промежутке от 0 до 1')
    btn2 = types.KeyboardButton('Функция F(x)- монотонно неубывающая')
    btn3 = types.KeyboardButton('График-кривая распределения(колокол)')
    markup.row(btn1)
    markup.row(btn2)
    markup.row(btn3)
    bot.send_message(message.chat.id, 'Вопрос№3\nВыберите неверное свойство функции распределения', reply_markup=markup)
    bot.register_next_step_handler(message, test4)


@bot.message_handler()
def test4(message):
    if message.text == 'График-кривая распределения(колокол)':
        bot.send_message(message.chat.id, 'Правильно!')
        rise_count()
    else:
        bot.send_message(message.chat.id, 'Неравильно!')
    markup = types.ReplyKeyboardMarkup()
    btn1 = types.KeyboardButton('Абсцисса кривой распределения, в которой площадь под кривой делится пополам')
    btn2 = types.KeyboardButton('Координата (абсцисса) максимума кривой распределения')
    btn3 = types.KeyboardButton('Среднее значение, около которого группируются все значения случайной величины')
    markup.row(btn1)
    markup.row(btn2)
    markup.row(btn3)
    bot.send_message(message.chat.id, 'Вопрос№4\nВыберите верное определение математического ожидания', reply_markup=markup)
    bot.register_next_step_handler(message, test5)

@bot.message_handler()
def test5(message):
    if message.text == 'Среднее значение, около которого группируются все значения случайной величины':
        bot.send_message(message.chat.id, 'Правильно!')
        rise_count()
    else:
        bot.send_message(message.chat.id, 'Неравильно!')
    markup = types.ReplyKeyboardMarkup()
    btn1 = types.KeyboardButton('Мат.ожидание постоянной равно этой постоянной')
    btn2 = types.KeyboardButton('Постоянный множитель можно вынести из-под знака мат. ожидания')
    btn3 = types.KeyboardButton('Мат. ожидание суммы случайных величин равно произведению их мат. ожиданий')
    markup.row(btn1)
    markup.row(btn2)
    markup.row(btn3)
    bot.send_message(message.chat.id, 'Вопрос№5\nВыберите неверное своёство математического ожидания', reply_markup=markup)
    bot.register_next_step_handler(message, test6)

@bot.message_handler()
def test6(message):
    if message.text == 'Мат. ожидание суммы случайных величин равно произведению их мат. ожиданий':
        bot.send_message(message.chat.id, 'Правильно!')
        rise_count()
    else:
        bot.send_message(message.chat.id, 'Неравильно!')
    markup = types.ReplyKeyboardMarkup()
    btn1 = types.KeyboardButton('Математическое ожидание квадрата разности случайной величины и ее мат. ожидания')
    btn2 = types.KeyboardButton('Наиболее вероятное значение случайной величины')
    btn3 = types.KeyboardButton('Абсцисса кривой распределения, в которой площадь под кривой делится пополам')
    markup.row(btn1)
    markup.row(btn2)
    markup.row(btn3)
    bot.send_message(message.chat.id, 'Вопрос№6\nВыберите верное определение дисперсии', reply_markup=markup)
    bot.register_next_step_handler(message, test7)

@bot.message_handler()
def test7(message):
    if message.text == 'Математическое ожидание квадрата разности случайной величины и ее мат. ожидания':
        bot.send_message(message.chat.id, 'Правильно!')
        rise_count()
    else:
        bot.send_message(message.chat.id, 'Неравильно!')
    markup = types.ReplyKeyboardMarkup()
    btn1 = types.KeyboardButton('Постоянный множитель можно вынести из-под знака дисперсии')
    btn2 = types.KeyboardButton('Дисперсия постоянной равна нулю')
    btn3 = types.KeyboardButton('Для независимых случайных величин дисперсия суммы равна сумме их мат. ожиданий')
    markup.row(btn1)
    markup.row(btn2)
    markup.row(btn3)
    bot.send_message(message.chat.id, 'Вопрос№7\nВыберите верное свойство дисперсии', reply_markup=markup)
    bot.register_next_step_handler(message, test8)

@bot.message_handler()
def test8(message):
    if message.text == 'Дисперсия постоянной равна нулю':
        bot.send_message(message.chat.id, 'Правильно!')
        rise_count()
    else:
        bot.send_message(message.chat.id, 'Неравильно!')
    markup = types.ReplyKeyboardMarkup()
    btn1 = types.KeyboardButton('Количество элементов n попавших в i-й интервал')
    btn2 = types.KeyboardButton('Совокупность отобранных объектов')
    btn3 = types.KeyboardButton('Разница между min и max элементами выборки')
    markup.row(btn1)
    markup.row(btn2)
    markup.row(btn3)
    bot.send_message(message.chat.id, 'Вопрос№8\nВыберите верное определение размаха R', reply_markup=markup)
    bot.register_next_step_handler(message, test9)

@bot.message_handler()
def test9(message):
    if message.text == 'Разница между min и max элементами выборки':
        bot.send_message(message.chat.id, 'Правильно!')
        rise_count()
    else:
        bot.send_message(message.chat.id, 'Неравильно!')
    markup = types.ReplyKeyboardMarkup()
    btn1 = types.KeyboardButton('парной линейной регрессией')
    btn2 = types.KeyboardButton('ковариацией')
    btn3 = types.KeyboardButton('коэффициентом корреляции')
    markup.row(btn1)
    markup.row(btn2)
    markup.row(btn3)
    bot.send_message(message.chat.id, 'Вопрос№9\nВыберите верное продолжение определения:\nДля анализа степени тесноты связи между двумя случайными величинами X и Yвводится специальная характеристика, называемая', reply_markup=markup)
    bot.register_next_step_handler(message, test10)

@bot.message_handler()
def test10(message):
    if message.text == 'ковариацией':
        bot.send_message(message.chat.id, 'Правильно!')
        rise_count()
    else:
        bot.send_message(message.chat.id, 'Неравильно!')
    markup = types.ReplyKeyboardMarkup()
    btn1 = types.KeyboardButton('Р(а)+Р(б)')
    btn2 = types.KeyboardButton('Р(а)Р(б)')
    btn3 = types.KeyboardButton('Р(а)+Р(б)-Р(аб)')
    markup.row(btn1)
    markup.row(btn2)
    markup.row(btn3)
    bot.send_message(message.chat.id, 'Вопрос№10\nВероятность суммы совместных событий: Р(а+б) = ', reply_markup=markup)
    bot.register_next_step_handler(message, final)

@bot.message_handler()
def final(message):
    if message.text == 'Р(а)+Р(б)-Р(аб)':
        bot.send_message(message.chat.id, 'Правильно!')
        rise_count()
    else:
        bot.send_message(message.chat.id, 'Неравильно!')
    global count
    result = str(count)
    markup = types.ReplyKeyboardMarkup()
    btn1 = types.KeyboardButton('Попробовать заново')
    btn2 = types.KeyboardButton('Закончить')
    markup.row(btn1)
    markup.row(btn2)
    bot.send_message(message.chat.id, 'Ваш результат:' + result + ' из 10', reply_markup=markup)
    bot.register_next_step_handler(message, test1)

bot.polling(none_stop=True)

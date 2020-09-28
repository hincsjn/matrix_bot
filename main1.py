import telebot
import config
import numpy as np
from telebot import types

bot = telebot.TeleBot(config.token)
user_mx = []  # матрица, введенная пользователем
chat = ''  # в этой переменной будет храниться message.chat.id
operation = 0


@bot.message_handler(commands=['start'])  # хендлер, начинающий программу после команды /start
def say_welcome(message):
    global chat
    msg = bot.send_message(message.chat.id, '''Привет! 
    Я провожу операции над матрицами
    Введи матрицу в формате 1 2 3; 4 5 6''')
    chat = message.chat.id
    bot.register_next_step_handler(msg, print_mx)


def print_mx(message):
    global user_mx

    if user_mx == []:
        user_mx = np.matrix(message.text)
    else:
        pass

    bot.send_message(chat, 'Полученная матрица: ')
    for i in user_mx:
        bot.send_message(chat, i)
    msg = bot.send_message(chat, 'Выберете одно из действий:\n'
          '1: операция сложения элементов матрицы и числа\n'
          '2: операция умножения элементов матрицы и числа\n'
          '3: операция транспонирования матрицы\n'
          '4: операция возведения элементов матрицы в неотрицательную степень (в разработке)\n'
          '5: операция нахождения определителя матрицы\n'
          '6: операция нахождения союзной матрицы (в разработке)\n'
          '7: операция нахождения прикрепленной матрицы (в разработке)\n'
          '8: операция нахождения обратной матрицы (в разработке)\n')
    bot.register_next_step_handler(msg, choose_operation)


def choose_operation(message):
    global operation

    operation = int(message.text)
    if operation == 1:
        msg = bot.send_message(chat, 'Введите число, с которым требуется сложить элементы матрицы: ')
        bot.register_next_step_handler(msg, mx_add)
    elif operation == 2:
        msg = bot.send_message(chat, 'Введите число, с которым требуется перемножить элементы матрицы: ')
        bot.register_next_step_handler(msg, mx_mult)
    elif operation == 3:
        msg = bot.send_message(chat, 'Отправь 1 для продолжения')
        bot.register_next_step_handler(msg, mx_transp)
    elif operation == 4:
        msg = bot.send_message(chat, 'Введите степень, в которую требуется возвести элементы матрицы: ')
        bot.register_next_step_handler(msg, mx_exp)
    elif operation == 5:
        msg = bot.send_message(chat, 'Отправь 1 для продолжения')
        bot.register_next_step_handler(msg, mx_det)
    elif operation == 6:
        msg = bot.send_message(chat, 'Отправь 1 для продолжения')
        bot.register_next_step_handler(msg, mx_transp)
    elif operation == 7:
        msg = bot.send_message(chat, 'Отправь 1 для продолжения')
        bot.register_next_step_handler(msg, mx_transp)
    elif operation == 8:
        msg = bot.send_message(chat, 'Отправь 1 для продолжения')
        bot.register_next_step_handler(msg, mx_transp)
    else:
        bot.send_message(chat, 'Да иди нахуй, просил же нормально ввести')


def mx_add(message):
    global user_mx

    num = int(message.text)
    for i in user_mx:
        for j in i:
            j += num

    result = user_mx

    for i in result:
        bot.send_message(chat, i)

    bot.send_message(chat, result)

    msg = bot.send_message(chat, 'Если желаете продолжить работу с данной матрицей, нажмите 1')
    if message.text == '1':
        user_mx = result
        bot.register_next_step_handler(msg, print_mx)
# убрать последнюю строку из принта


def mx_mult(message):
    global user_mx

    num = int(message.text)
    for i in user_mx:
        for j in i:
            j *= num

    result = user_mx

    for i in result:
        bot.send_message(chat, i)

    bot.send_message(chat, result)

    msg = bot.send_message(chat, 'Если желаете продолжить работу с данной матрицей, нажмите 1')
    if message.text == '1':
        user_mx = result
        bot.register_next_step_handler(msg, print_mx)
# убрать последнюю строку из принта        


def mx_transp(message):
    global user_mx
    matrix = user_mx
    result = np.matrix(matrix).transpose()

    for i in result:
        bot.send_message(chat, i)

    msg = bot.send_message(chat, 'Если желаете продолжить работу с данной матрицей, нажмите 1')
    if message.text == '1':
        user_mx = result
        bot.register_next_step_handler(msg, print_mx)


def mx_exp(message):
    global user_mx

    num = int(message.text)
    for i in user_mx:
        for j in i:
            j **= num

    result = user_mx

    for i in result:
        bot.send_message(chat, i)

    bot.send_message(chat, result)

    msg = bot.send_message(chat, 'Если желаете продолжить работу с данной матрицей, нажмите 1')
    if message.text == '1':
        user_mx = result
        bot.register_next_step_handler(msg, print_mx)
# придумать др использование


def mx_det(message):
    global user_mx

    bot.send_message(chat, np.linalg.det(user_mx))
    result = user_mx
    msg = bot.send_message(chat, 'Если желаете продолжить работу с данной матрицей, нажмите 1')

    if message.text == '1':
        user_mx = result
        bot.register_next_step_handler(msg, print_mx)


def union(message):
    pass
# написать функцию


def attached(message):
    pass
# написать функцию


def inverse(message):
    global user_mx

    bot.send_message(chat, np.linalg.inv(user_mx))
    result = user_mx
    msg = bot.send_message(chat, 'Если желаете продолжить работу с данной матрицей, нажмите 1')

    if message.text == '1':
        user_mx = result
        bot.register_next_step_handler(msg, print_mx) #
# написать функцию


bot.polling()

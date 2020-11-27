from config import bot
import telebot

# ToDo Добавить генерацию кнопок и общую логику для старта чата с покупателем
# Добавление кнопок для перемещения по меню
keyboard1 = telebot.types.ReplyKeyboardMarkup()
keyboard1.row('Привет', 'Пока')


@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id,
                     f'Привет {message.chat.first_name}, помотрим список товара? Или уже знаешь чего хочеш?',
                     reply_markup=keyboard1)


@bot.message_handler(content_types=['text'])
def send_text(message):
    if message.text.lower() == 'привет':
        bot.send_message(message.chat.id, 'Привет, пуэрчику)?')
    elif message.text.lower() == 'пока':
        bot.send_message(message.chat.id, 'Пока, пока!')


@bot.message_handler(content_types=['sticker'])
def id_sticker(message):
    print(message)


# Запуск бота
bot.polling()

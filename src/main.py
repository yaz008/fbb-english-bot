from bot import bot
from telebot.types import Message, CallbackQuery, InlineKeyboardMarkup as Markup
from words import random_pair
from markup import next_markup, answer_markup

@bot.message_handler(commands=['start'])
def on_start(message: Message) -> None:
    with open(file='assets\\start.txt', mode='r', encoding='UTF-8') as start_text:
        bot.send_message(chat_id=message.from_user.id,
                        text=start_text.read())

@bot.message_handler(commands=['random'])
def on_random(message: Message) -> None:
    word, antonym = random_pair()
    bot.send_message(chat_id=message.from_user.id,
                     text=word,
                     reply_markup=answer_markup(antonym=antonym))
    
@bot.callback_query_handler(func=lambda *_: True)
def on_callback(callback: CallbackQuery) -> None:
    message: Message = callback.message
    match callback.data.split(sep=':'):
        case ['next', current_word]:
            word, antonym = random_pair(exclude_word=current_word)
            markup: Markup = answer_markup(antonym=antonym)
            bot.edit_message_text(text=f'{word}',
                                  chat_id=message.chat.id,
                                  message_id=message.id,
                                  reply_markup=markup)
        case ['answer', antonym]:
            current_word: str = message.text
            markup: Markup = next_markup(word=current_word)
            bot.edit_message_text(text=f'{current_word}: {antonym}',
                                  chat_id=message.chat.id,
                                  message_id=message.id,
                                  reply_markup=markup)

if __name__ == '__main__':
    bot.infinity_polling()
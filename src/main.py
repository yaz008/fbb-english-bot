from bot import bot
from telebot.types import Message, CallbackQuery
from words import random_pair
from markup import on_random_markup

@bot.message_handler(commands=['start'])
def on_start(message: Message) -> None:
    start_text: str = 'Welcome to *FBB English Bot*\\!\n\n'
    start_text += 'Send /random to start practicing'
    bot.send_message(chat_id=message.from_user.id,
                     text=start_text)

@bot.message_handler(commands=['random'])
def on_random(message: Message) -> None:
    word, antonym = random_pair()
    bot.send_message(chat_id=message.from_user.id,
                     text=f'{word}: ||{antonym}||',
                     reply_markup=on_random_markup(word=word))
    
@bot.callback_query_handler(func=lambda *_: True)
def on_callback(callback: CallbackQuery) -> None:
    match callback.data.split(sep=':'):
        case ['next', current_word]:
            message: Message = callback.message
            word, antonym = random_pair(exclude_word=current_word)
            bot.edit_message_text(text=f'{word}: ||{antonym}||',
                                  chat_id=message.chat.id,
                                  message_id=message.id,
                                  reply_markup=on_random_markup(word=current_word))

if __name__ == '__main__':
    bot.infinity_polling()
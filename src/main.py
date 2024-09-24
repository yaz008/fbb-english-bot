from bot import bot
from telebot.types import Message
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
    bot.send_message(chat_id=message.from_user.id,
                     text=random_pair(),
                     reply_markup=on_random_markup())

if __name__ == '__main__':
    bot.infinity_polling()
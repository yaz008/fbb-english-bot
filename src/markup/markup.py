from telebot.types import InlineKeyboardMarkup as Markup, InlineKeyboardButton as Button

def on_random_markup() -> Markup:
    markup: Markup = Markup()
    markup.add(Button(text='Next', callback_data='next'))
    return markup
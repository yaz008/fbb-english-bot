from telebot.types import InlineKeyboardMarkup as Markup, InlineKeyboardButton as Button

def on_random_markup(word: str) -> Markup:
    markup: Markup = Markup()
    markup.add(Button(text='Next', callback_data=f'next:{word}'))
    return markup
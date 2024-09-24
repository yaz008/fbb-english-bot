from telebot.types import InlineKeyboardMarkup as Markup, InlineKeyboardButton as Button

def next_markup(word: str) -> Markup:
    markup: Markup = Markup()
    markup.add(Button(text='Next', callback_data=f'next:{word}'))
    return markup

def answer_markup(antonym: str) -> Markup:
    markup: Markup = Markup()
    markup.add(Button(text='Answer', callback_data=f'answer:{antonym}'))
    return markup
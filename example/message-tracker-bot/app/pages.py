from telekey import Page, InlineKeyboardButton, KeyboardButton, ReplyKeyboardRemove

main_page = Page(
    'hi this is main page',
    botton_list=[
        InlineKeyboardButton('ok', callback_data='saidok'),
        InlineKeyboardButton('no', callback_data='saidno')
    ]
)

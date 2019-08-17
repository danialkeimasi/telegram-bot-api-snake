from snake import Page, InlineKeyboardButton, KeyboardButton, ReplyKeyboardRemove

main_page = Page(
    'hi this is main page',
    botton_list=[
        InlineKeyboardButton('ok', callback_data='kir'),
        InlineKeyboardButton('ra', callback_data='bokhor')
    ]
)

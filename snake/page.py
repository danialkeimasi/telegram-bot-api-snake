import telegram
from telegram import KeyboardButton, InlineKeyboardButton

def build_menu(buttons, n_cols, header_buttons, footer_buttons):

    menu = [buttons[i:i + n_cols] for i in range(0, len(buttons), n_cols)]

    if header_buttons:
        menu.insert(0, header_buttons)
    if footer_buttons:
        menu.append(footer_buttons)

    return menu


class Page:

    def __init__(self, text,
                    botton_list=None, header_buttons=None, footer_buttons=None,
                    page_type='simple', n_cols=2): # 'simple' or 'inline'
        self.text = text
        self.botton_list = botton_list
        self.header_buttons = header_buttons
        self.footer_buttons = footer_buttons
        self.type = page_type
        self.n_cols = n_cols

    @property
    def markup(self):
        if self.type == 'simple':
            return telegram.ReplyKeyboardMarkup(build_menu(self.botton_list, self.n_cols, self.header_buttons, self.footer_buttons))
        else:
            return telegram.InlineKeyboardMarkup(build_menu(self.botton_list, self.n_cols, self.header_buttons, self.footer_buttons))


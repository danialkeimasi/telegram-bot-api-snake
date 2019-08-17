import telegram
from telegram import KeyboardButton, InlineKeyboardButton, ReplyKeyboardRemove


def build_menu(buttons, n_cols, header_buttons, footer_buttons):
    menu = [buttons[i:i + n_cols] for i in range(0, len(buttons), n_cols)]

    if header_buttons:
        menu.insert(0, header_buttons)
    if footer_buttons:
        menu.append(footer_buttons)

    return menu


class Page:

    def __init__(self, text, botton_list=[], header_buttons=[], footer_buttons=[], n_cols=2):

        self.text = text
        self.botton_list = botton_list
        self.header_buttons = header_buttons
        self.footer_buttons = footer_buttons
        self.n_cols = n_cols

    @property
    def markup(self):

        full_list = self.botton_list + self.header_buttons + self.footer_buttons
        menu = build_menu(self.botton_list, self.n_cols, self.header_buttons, self.footer_buttons)

        if full_list == []:
            return None

        if all([isinstance(i, KeyboardButton) for i in full_list]):
            return telegram.ReplyKeyboardMarkup(menu)
        if all([isinstance(i, InlineKeyboardButton) for i in full_list]):
            return telegram.InlineKeyboardMarkup(menu)

        return None

    @property
    def text_remove_keyboard(self):
        return {
            'text': self.text,
            'reply_markup': ReplyKeyboardRemove()
        }

    @property
    def caption_remove_keyboard(self):
        return {
            'text': self.text,
            'reply_markup': ReplyKeyboardRemove()
        }

    @property
    def text_markup(self):
        return {
            'text': self.text,
            'reply_markup': self.markup
        }

    @property
    def caption_markup(self):
        return {
            'caption': self.text,
            'reply_markup': self.markup
        }

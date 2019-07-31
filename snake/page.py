

class Botton:

    def __init__(self, text, action = None):
        self.text = text
        self.action = action


class Page:

    def __init__(self, text, bottons = []):
        self.text = text
        self.bottons = bottons

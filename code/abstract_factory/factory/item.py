from abc import ABCMeta, abstractmethod

class Item(metaclass=abstactmethod):
    def __init__(self, caption):
        self.caption = caption

    @abstractmethod
    def make_html(self):
        pass

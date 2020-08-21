from abc import ABCMeta, abstractmethod

class Item(metaclass=ABCMeta):
    def __init__(self, caption:str):
        self.caption = caption

    @abstractmethod
    def make_html(self):
        pass

from abc import ABCMeta, abstractmethod

class Link(Item, metaclass=ABCMeta):
    def __init__(self, caption: str, url: str):
        super().__init__(caption)
        self.url = url

from abc import ABCMeta, abstractmethod
from .item import Item

class Tray(Item, metaclass=ABCMeta):
    def __init__(self, caption):
        super().__init__(caption)
        self._tray = []

    def add(self, item: Item):
        self._tray.append(item)

from abc import ABCMeta, abstractmethod

class Tray(Item, metaclass=ABCMeta):
    def add(self, item):
        tray = []
        tray.append(item)

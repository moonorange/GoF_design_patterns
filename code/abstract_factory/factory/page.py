from abc import ABCMeta, abstractmethod
from .item import Item

class Page(metaclass=ABCMeta):
    def __init__(self, title: str, author: str):
        self.title = title
        self.author = author
        self._content = []

    def add(self, item: Item):
        self._content.append(item)

    def output(self):
        try:
            filename = self.title + ".htmll"
            with open(filename) as f:
                f.write(self.make_html())
            print("{}を作成しました。".format(filename))
        except Exception as e:
            print(e)

    @abstractmethod
    def make_html(self):
        pass

from abc import ABCMeta, abstractmethod
import sys

class Factory(metaclass=ABCMeta):
    @classmethod
    def get_factory(cls, classname: str):
        try:
            module, cla = classname.split('.')
            return getattr(__import__(module), cla)()
        except ModuleNotFoundError:
            print("Can't find class {}".format(classname))
            sys.exit(1)
        except Exception as e:
            print(e)
            sys.exit(1)

    @abstractmethod
    def create_link(self, caption: str, url: str):
        pass

    @abstractmethod
    def create_tray(self, caption: str):
        pass

    @abstractmethod
    def create_page(self, title: str, author: str):
        pass


class Item(metaclass=ABCMeta):
    def __init__(self, caption):
        self.caption = caption

    @abstractmethod
    def make_html(self):
        pass


class Link(Item, metaclass=ABCMeta):
    def __init__(self, caption: str, url: str):
        super().__init__(caption)
        self.url = url


class Tray(Item, metaclass=ABCMeta):
    def __init__(self, caption):
        super().__init__(caption)
        self._tray = []

    def add(self, item: Item):
        self._tray.append(item)


class Page(metaclass=ABCMeta):
    def __init__(self, title: str, author: str):
        self.title = title
        self.author = author
        self._content = []

    def add(self, item: Item):
        self._content.append(item)

    def output(self):
        try:
            filename = self.title + ".html"
            writer = open("code/abstract_factory/output/" + filename, 'w')
            writer.write(self.make_html())
            writer.close()
            print(filename + 'を作成しました。')
        except Exception as e:
            print(e)

    @abstractmethod
    def make_html(self):
        pass

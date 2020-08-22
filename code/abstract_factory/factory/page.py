from abc import ABCMeta, abstractmethod

class Page(metaclass=ABCMeta):
    def __init__(self, title, author):
        this.title = title
        this.author = author

    def add(self, item):
        content = []
        content.append(item)

    def output(self):
        try:
            filename = this.title + ".htmll"
            with open(filename) as f:
                f.write(self.make_html())
            print("{}を作成しました。".format(filename))
        except Exception as e:
            print(e)

    @abstractmethod
    def make_html(self):
        pass

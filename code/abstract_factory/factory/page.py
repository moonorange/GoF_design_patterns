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
            with open()

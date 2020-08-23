from ..factory import *

class ListFactory(Factory):
    def create_link(self, caption: str, url: str):
        return ListLink(caption, url)

    def create_tray(self, caption: str):
        return ListTray(caption)

    def create_page(self, title: str, author: str):
        return ListPage(title, author)

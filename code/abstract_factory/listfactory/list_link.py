from ..factory import *

class ListLink(Link):
    def __init__(self, caption: str, url: str):
        super().__init__(caption, url)

    def make_html(self):
        return " <li><a href={url}>{caption}</a><li>\n".format(self.url, self.caption)

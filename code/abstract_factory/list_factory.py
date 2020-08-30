import abstract_factory

class ListFactory(abstract_factory.Factory):
    def create_link(self, caption: str, url: str):
        return ListLink(caption, url)

    def create_tray(self, caption: str):
        return ListTray(caption)

    def create_page(self, title: str, author: str):
        return ListPage(title, author)


class ListLink(abstract_factory.Link):
    def __init__(self, caption: str, url: str):
        super().__init__(caption, url)

    def make_html(self):
        return " <li><a href={}>{}</a><li>\n".format(self.url, self.caption)


class ListTray(abstract_factory.Tray):
    def make_html(self):
        buffer = []
        buffer.append("<li>\n")
        buffer.append("{}\n".format(self.caption))
        buffer.append("<ul>\n")
        for item in self._tray:
            buffer.append(item.make_html())
        buffer.append("</ul>\n")
        buffer.append("</li>\n")

        return "".join(buffer)


class ListPage(abstract_factory.Page):
    def __init__(self, title: str, author: str):
        super().__init__(title, author)

    def make_html(self):
        buffer = []
        buffer.append("<html><head><title>{}</title></head></html>\n".format(self.title))
        buffer.append("<body>\n")
        buffer.append("<h1>{}</h1>\n".format(self.title))
        buffer.append("<ul>\n")
        for con in self._content:
            buffer.append(con.make_html())
        buffer.append("</ul>\n")
        buffer.append("<hr><address>{}</address>".format(self.author))
        buffer.append("</body></html>\n")

        return "".join(buffer)

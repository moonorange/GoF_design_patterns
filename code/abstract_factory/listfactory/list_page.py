class ListPage(Page):
    def __init__(self, title: str, author: str):
        super().__init__(title, author)

    def make_html(self):
        buffer = []
        buffer.append("<html><head><title>{}</title></head></html>\n".format(self.title))
        buffer.append("<body>\n")
        buffer.append("<h1>{}</h1>\n".format(title))
        buffer.append("<ul>\n")
        for con in self._content:
            buffer.append(con.make_html())
        buffer.append("</ul>\n")
        buffer.append("<hr><address>{}</address>".format(author))
        buffer.append("</bod></html>\n")

        return "".join(buffer)

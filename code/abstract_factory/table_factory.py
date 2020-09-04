
import abstract_factory


class TableFactory(abstract_factory.Factory):
    def create_link(self, caption, url):
        return TableLink(caption, url)

    def create_tray(self, caption):
        return TableTray(caption)

    def create_page(self, title, author):
        return TablePage(title, author)


class TableLink(abstract_factory.Link):
    def __init__(self, caption, url):
        super().__init__(caption, url)

    def make_html(self):
        return '<td><a href={}>{}</a></td>'.format(self.url, self.caption)


class TableTray(abstract_factory.Tray):
    def __init__(self, caption):
        super().__init__(caption)

    def make_html(self):
        buf = []
        buf.append('<td>')
        buf.append('<table width="100%" border="1"><tr>')
        buf.append('<td bgcolor="#cccccc" algin="center" colsapn="{}"><b>{}</b></td>'.format(len(self._tray), self.caption))
        buf.append('</tr>\n')
        buf.append('<tr>\n')

        for item in self._tray:
            buf.append(item.make_html())

        buf.append('</tr></table>')
        buf.append('</td>')
        return ''.join(buf)


class TablePage(abstract_factory.Page):
    def __init__(self, title, author):
        super().__init__(title, author)

    def make_html(self):
        buf = []
        buf.append("<html><head><title>{}</title></head>".format(self.title))
        buf.append('<body>\n')
        buf.append('<h1>{}</h1>'.format(self.title))
        buf.append('<table width="80%" border="3">\n')

        for item in self._content:
            buf.append('<tr>{}</tr>'.format(item.make_html()))

        buf.append('</table>')
        buf.append('<hr><adress>{}</adress>'.format(self.author))
        buf.append('</body>\n</html>\n')
        return ''.join(buf)

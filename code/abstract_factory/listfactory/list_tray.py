from ..factory import *

class ListTray(Tray):
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

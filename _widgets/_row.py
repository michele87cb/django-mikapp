from flask import Markup


class Row(object):

    def __init__(self):
        self.custom_class = ''
        self.custom_style = ''

    def begin(self):

        if len(self.custom_class) > 0:
            self.custom_class = ' ' + self.custom_class
        if len(self.custom_style) > 0:
            self.custom_style = 'style="' + self.custom_style + '"'
        return Markup('<div class="row%s"%s>' % (self.custom_class, self.custom_style))

    def end(self):
        return Markup('</div>')
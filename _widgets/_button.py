from flask import Markup


class Button(object):

    def __init__(self, name):
        self.name = name
        self.custom_class = ''
        self.custom_style = ''
        self.pull = 'left'
        self.type = 'button'
        self.bootstrap_class = 'default'
        self.bootstrap_width = ''
        self.label = ''
        self.submit = False
        self.target = '_self'
        self.onclick = ''
        self.href = ''
        self.tag_type = ButtonType.button()

    def show(self):

        if len(self.custom_class) > 0:
            self.custom_class = ' ' + self.custom_class
        if len(self.custom_style) > 0:
            self.custom_style = 'style="' + self.custom_style + '"'
        onclicktx = ''
        if len(self.onclick) > 0:
            onclicktx += ' onclick="' + self.onclick + '"'
        hreftx = ''
        if len(self.href) > 0:
            hreftx += ' href="' + self.href + '" target="' + self.target + '"'
        if len(self.pull) > 0:
            self.custom_class += ' pull-' + self.pull
        if len(self.bootstrap_class) > 0:
            self.bootstrap_class = 'btn btn-' + self.bootstrap_class
        if self.submit:
            return Markup('<div class="' + self.bootstrap_width + '"><input id="' + self.name + '" type="submit"' + onclicktx + hreftx +
                      ' value="%s" class="%s%s"%s/>' % (self.label, self.bootstrap_class, self.custom_class, self.custom_style))
        return Markup('<div class="' + self.bootstrap_width + '"><' + self.tag_type + ' id="' + self.name + '" type="' + self.type + '"' + onclicktx + hreftx +
                      ' class="%s%s"%s>' % (self.bootstrap_class, self.custom_class, self.custom_style) +
                      self.label + '</' + self.tag_type + '></div>')

class ButtonType(object):

    @staticmethod
    def button():
        return 'button'

    @staticmethod
    def a():
        return 'a'

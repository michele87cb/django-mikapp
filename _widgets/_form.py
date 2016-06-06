from flask import Markup
from _widgets import _row
from _libs import pages_lib


class Form(object):

    def __init__(self, req, name):
        self.name = name
        self.id = name
        self.form_tag = True
        self.url_rewrite = ''
        self.form_action = ''
        self.form_method = 'POST'
        self.form_role = 'form'
        self.form_class = 'form-horizontal'
        self.form_showed = False
        self.items = []
        self.buttons = []
        self.bootstrap_width = 'col-sm-12'
        self.title = ''
        self.script_manual = ''
        self.script_file = ''
        self.script_onload = ''
        self.wizard = False
        self.req = req
        self.config = pages_lib.Config()
        req.miconf = self.config

    def show(self):
        row1 = _row.Row()
        valshow = Markup('<div class="' + self.bootstrap_width + '">')
        if self.form_tag == True:
            valshow += Markup('<form action="' + self.form_action + '" method="' + self.form_method + '" role="' + self.form_role + '" class="' + self.form_class + '">')
        valshow += row1.begin()
        try:
            for it in self.items:
                if it == '_widgets.row':
                    valshow += row1.end() + row1.begin()
                else:
                    try:
                        valshow += it.show()
                    except Exception:
                        try:
                            valshow += str(it)
                        except Exception:
                            pass
        except Exception:
            pass
        valshow += row1.end()
        valshow += row1.begin()
        for it in self.buttons:
            try:
                valshow += it.show()
            except Exception:
                try:
                    valshow += str(it)
                except Exception:
                    pass
        valshow += row1.end()
        if self.form_tag:
            valshow += Markup('</form>')
        valshow += Markup('</div>')
        if self.url_rewrite != '':
            self.script_onload = 'window.history.pushState("' + self.name + '", "' + self.title + '", "' + self.url_rewrite + '"); ' + \
                                 self.script_onload
        if len(self.script_onload) > 0 and "$(document).ready(function" not in self.script_onload:
            self.script_onload = '$(document).ready(function() { ' + self.script_onload + ' });'
        self.form_showed = True
        return Markup(valshow)

    def show_js(self):
        valshow = ''
        if self.form_showed == True:
            if len(self.script_file) > 0:
                valshow += '<script src="" type="text/javascript"></script>\n'
            valshow += '<script type="text/javascript">\n'
            valshow += '\n'
            valshow += self.script_onload + '\n'
            valshow += '\n'
            valshow += '</script>\n'
            valshow += '<script type="text/javascript">\n'
            valshow += '\n'
            valshow += self.script_manual + '\n'
            valshow += '\n'
            valshow += '</script>\n'

        return Markup(valshow)
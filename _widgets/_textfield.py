from flask import Markup


class Textfield(object):

    def __init__(self, name):
        self.name = name
        self.id = name
        self.value = ''
        self.bootstrap_width = 'col-sm-12'
        self.label = ''
        self.onchange = ''
        self.hasfocus = False
        self.type = TextfieldType.text()
    
    def show(self):
        attributes = ''
        if len(self.onchange) > 0:
            attributes = ' onchange="' + self.onchange + '"'
        if len(attributes) > 0:
            attributes += ' '
        valshow = '''<div class="%s">
    <div class="form-group  required">
        <label class="control-label" for="%s">%s</label>
        <input class="form-control" id="%s" name="%s" required="" type="%s" value="%s"%s>
    </div>
</div>''' % (self.bootstrap_width, self.id, self.label, self.id, self.id, self.type, self.value, attributes)

        if self.hasfocus == True:
            valshow += '''
<div class="jscript_to_execute" style="display: none">$('#%s').focus();</div>
            ''' % self.name
        # <input class="btn btn-primary" id="submit_button" name="submit_button" type="submit" value="Submit Form">
        return Markup(valshow)


# Tipo di textfield
class TextfieldType(object):
    '''
    Tipo Textfield
    '''

    @staticmethod
    def text():
        return 'text'

    @staticmethod
    def date():
        return 'date'

    @staticmethod
    def password():
        return 'password'

    def __init__(self, v):
        self.val = v
        self.methods = (TextfieldType.text,
                        TextfieldType.date,
                        TextfieldType.password)

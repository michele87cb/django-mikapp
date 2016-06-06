from flask import url_for
import _widgets


class FormLogin(object):

    def __init__(self, request, name, username='', form_action='login', redto=''):
        form = _widgets.Form(request, name)
        form.form_action = url_for(form_action)
        if redto != '':
            form.form_action = url_for(form_action, redto=redto)
        form.bootstrap_width = 'col-sm-2 col-sm-offset-5'
        txtuser = _widgets.Textfield('txt_username_login')
        txtuser.label = 'Username'
        txtuser.hasfocus = True
        if username != '':
            txtuser.value = username
        txtpwd = _widgets.Textfield('txt_password_login')
        txtpwd.label = 'Password'
        txtpwd.type = 'password'
        btnsubmit = _widgets.Button('btnsubmit')
        btnsubmit.label = 'Login'
        btnsubmit.submit = True
        btnsubmit.pull = 'right'
        btnsubmit.bootstrap_class = 'primary'

        form.items = [txtuser, '_widgets.row', txtpwd]
        form.buttons = [btnsubmit]
        self.__dict__ = form.__dict__
        self.__class__ = form.__class__


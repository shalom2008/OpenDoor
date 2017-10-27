from django import forms


class LoginForm(forms.Form):
    username = forms.CharField(required=True, label='用户名', max_length=8)
    password = forms.PasswordInput()

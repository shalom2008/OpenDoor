from django import forms


class LoginForm(forms.Form):
    username = forms.CharField(required=True, label='用户名', max_length=8)
    password = forms.CharField(required=True, label='密码', min_length=8, widget=forms.PasswordInput)

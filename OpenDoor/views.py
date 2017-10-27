from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.views.generic import View

from .forms import LoginForm


class UserLoginView(View):
    def get(self, request):
        login_form = LoginForm()
        return render(request, 'login.html', {'form': login_form})

    def post(self, request):
        try:
            login_form = LoginForm(request.POST)
            if login_form.is_valid():
                username = login_form.cleaned_data.get('username', '')
                password = login_form.cleaned_data.get('password', '')
                user = User.objects.filter(username=username)
                if not user:
                    raise Exception('该用户不存在！')

                user = authenticate(request, username=username, password=password)
                if user:
                    login(request, user)
                else:
                    raise Exception('密码错误！')
                return redirect('/')
            else:
                raise Exception('填写有误！')

        except Exception as e:
            error_message = str(e)
            return render(request, 'login.html', {'error_message': error_message, 'form': login_form})

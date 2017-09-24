from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User


@login_required(login_url='/login')
def index(request):
    return render(request, 'index.html')


def user_login(request):
    if request.method == "POST":
        try:
            username = request.POST.get('username', '')
            password = request.POST.get('password', '')
            user = User.objects.filter(username=username)
            if not user:
                raise Exception('该用户不存在！')

            user = authenticate(request, username=username, password=password)
            if user:
                login(request, user)
            else:
                raise Exception('密码错误！')
            return redirect('/')
        except Exception as e:
            error_message = str(e)
            return render(request, 'login.html', {'error_message': error_message})
    else:
        return render(request, 'login.html')

from django.shortcuts import render


def home(request):
    return render(request, 'base.html')


def reset_password(request):
    return render(request, 'password_reset.html')


def handler404(request, exception):
    return render(request, '404.html')

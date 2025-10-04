from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'main/pages/index.html')

def userLogin(request):
    return render(request, 'main/auth/login.html')
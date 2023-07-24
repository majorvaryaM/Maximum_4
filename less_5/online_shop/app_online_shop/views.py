from django.shortcuts import render
# подключаем объект для выполнения http-запросов
from django.http import HttpResponse

# Create your views here.

# Функция, отображающая файл index.html
def index (request):
    return render (request, 'index.html')

# Функция, отображающая файл top_sellers.html
def top_sellers (request):
    return render (request, 'top-sellers.html')

# Функция, отображающая файл advertisement-post.html
def advertisement_post (request):
    return render (request, 'advertisement-post.html')

# Функция, отображающая файл login.html
def login (request):
    return render (request, 'login.html')

# Функция, отображающая файл register.html
def register (request):
    return render (request, 'register.html')

# Функция, отображающая файл profile.html
def profile (request):
    return render (request, 'profile.html')

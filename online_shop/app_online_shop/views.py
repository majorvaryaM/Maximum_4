from django.shortcuts import render
# подключаем объект для выполнения http-запросов
from django.http import HttpResponse

# Create your views here.

# Функция, отображающая файл index.html
def index(request):
    return render(request, 'index.html') 
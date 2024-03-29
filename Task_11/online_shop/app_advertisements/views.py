from django.shortcuts import render, redirect
# подключаем объект для выполнения http-запросов
from django.http import HttpResponse
from django.urls import reverse, reverse_lazy
from.models import Advertisement
from .forms import AdvertisementForm
from django.contrib.auth.decorators import login_required

# Create your views here.

# Функция, отображающая файл index.html
def index (request):
    title = request.GET.get('query')
    if title:
        online_shops = Advertisement.objects.filter(title=title)
    else:
        #выгружаем все объекты из нашей БД
        online_shops = Advertisement.objects.all()
    # создаем контекст шаблона
    context = {'online_shops':online_shops} 
    return render (request, 'app_advertisements/index.html', context)

# Функция, отображающая файл top_sellers.html
def top_sellers (request):
    return render (request, 'app_advertisements/top-sellers.html')

@login_required(login_url=reverse_lazy('login'))
# Функция, отображающая файл advertisement-post.html
def advertisement_post (request):
    # проверка, что обрабатывается Post-запрос
    if request.method == 'POST':
        form = AdvertisementForm (request.POST, request.FILES)
        # проверка на валидность объекта форм
        if form.is_valid():
            # advertisement = Advertisement(**form.cleaned_data)
            advertisement = form.save(commit=False)
            advertisement.user = request.user
            advertisement.save()
            url = reverse('main-page')
            return redirect(url)
    else:
        form = AdvertisementForm ()
    context = {'form': form}
    return render (request, 'app_advertisements/advertisement-post.html', context)

# # Функция, отображающая файл login.html
# def login (request):
#     return render (request, 'login.html')

# Функция, отображающая файл register.html
# def register (request):
#     return render (request, 'app_auth/register.html')

# # Функция, отображающая файл profile.html
# def profile (request):
#     return render (request, 'profile.html')

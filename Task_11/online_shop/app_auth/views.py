from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required(login_url=reverse_lazy('login'))
# Создаем отображения профиля
def profile_view(request):
    return render (request, 'app_auth/profile.html')

# создаём аутентификацию пользователя
def login_view(request):
    redirect_url = reverse('profile')
    if request.method == 'GET':
        if request.user.is_authenticated:
            return redirect(redirect_url)
        else:
            return render(request, 'app_auth/login.html')      
    username = request.POST.get('username','')
    password = request.POST.get('password','')
    user = authenticate(request)
    # проверка что нашлась комбинация логина и пароля
    if user is not None:
        login(request, user)
        return redirect('/')
    # комбинация не нашлась - пользователь не найден
    return render(request,'app_auth/login.html', {'error': 'Пользователь не найден'})

# создаем выход из профиля
def logout_view(request):
    logout(request)
    return redirect (reverse ('login'))

# создаем форму регистрации пользователя
def register(request):
    if request.method == 'POST':
        newuser_form = UserCreationForm(request.POST)
        if newuser_form.is_valid():            
            newuser_form.save()
            new_user = authenticate(request, username=newuser_form.cleaned_data['username'], password=newuser_form.cleaned_data['password2'])
            login(request, new_user)              
            return render(request, 'app_auth/profile.html')
    else:
        newuser_form = UserCreationForm()
    return render(request, 'app_auth/register.html', {'user_form': newuser_form})

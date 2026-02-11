from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy

def MainFunc(request):
    return render(request, 'main.html')

def RegFunc(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('main')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('main')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

def logout_view(request):
    from django.contrib.auth import logout
    logout(request)
    return redirect('main')

def MainFunc(request):
    # Пример данных для каталога
    desktop_pcs = [
        {'name': 'DELL Vostro 3681 SFF', 'specs': 'Intel Core i5, 8 ГБ RAM, Intel UHD Graphics 630', 'price': '45 990'},
        {'name': 'Lenovo IdeaCentre 3 07ADA05', 'specs': 'AMD Ryzen 5, 8 ГБ RAM, 512 ГБ SSD', 'price': '39 990'},
        {'name': 'ASUS ExpertCenter D5', 'specs': 'Intel Core i7, 16 ГБ RAM, 1 ТБ HDD + 256 ГБ SSD', 'price': '67 490'},
        {'name': 'HP M01 Mini-Tower', 'specs': 'Intel Core i3, 8 ГБ RAM, 256 ГБ SSD', 'price': '34 990'},
        {'name': 'Lenovo Legion T5 26IOB6', 'specs': 'Intel Core i7, RTX 3070, 16 ГБ RAM', 'price': '129 990'},
        {'name': 'Fujitsu ESPRIMO Q5010 MT', 'specs': 'Intel Core i3, 8 ГБ RAM, 256 ГБ SSD', 'price': '32 490'},
    ]
    
    context = {
        'desktop_pcs': desktop_pcs,
    }
    return render(request, 'main.html', context)
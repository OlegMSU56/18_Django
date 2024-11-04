from django.shortcuts import render

# Create your views here.

def platform(request):
    title = 'Главная страница'
    context = {
        'title': title
    }
    return render(request, 'third_task/platform.html', context)

def games(request):
    title = 'Игры'
    context = {
        'title': title
    }
    return render(request, 'third_task/games.html', context)

def cart(request):
    title = 'Корзина'
    context = {
        'title': title
    }
    return render(request, 'third_task/cart.html', context)
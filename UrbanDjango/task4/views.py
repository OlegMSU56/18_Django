from django.shortcuts import render

# Create your views here.

def platform(request):
    title = 'Главная страница'
    context = {
        'title': title
    }
    return render(request, 'fourth_task/platform.html', context)

def games(request):
    games = ['Atomic Heart', 'Cyberpunk 2077', 'GTA']
    return render(request, 'fourth_task/games.html', {'games': games})

def cart(request):
    title = 'Корзина'
    context = {
        'title': title
    }
    return render(request, 'fourth_task/cart.html', context)

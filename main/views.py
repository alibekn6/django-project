from django.shortcuts import render
from goods.models import Categories, Products


def index(request):

    categories = Categories.objects.all()

    context = {
        'title': 'Home - Главная',
        'content': 'Магазин мебели HOME',
        'categories': categories
    }
    return render(request, 'main/index.html', context)


def about(request):
    context = {
        'title': 'Home - О нас',
        'content': 'О нас',
        'text_on_page': 'Lorem ipsum, dolor sit amet consectetur adipisicing elit. Beatae, reiciendis.'
    }
    return render(request, 'main/about.html', context)
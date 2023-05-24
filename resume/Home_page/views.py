#Импортируем системную функцию для рендеринга страницы.
from django.shortcuts import render 

def show(request):
    """Загружаем домашнюю страницу."""
    return render(request, 'home_page/home_page.html') 

def contact(request):
    """Страница с контактами."""
    return render(request, 'home_page/contact.html')

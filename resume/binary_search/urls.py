#Импортируем системную функцию.
from django.urls import path

#Импортируем views из этой же директории.
from . import views

urlpatterns = [
    path('search', views.start, name = 'start_binary'),  #Начальная страница.
    path('result/', views.result, name = 'result_binary') #Страница с результатом.
]
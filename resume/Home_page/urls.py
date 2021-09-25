#Импортируем системную функцию.
from django.urls import path, include

#Импортируем views из этой же директории.
from . import views

urlpatterns = [
    path('', views.show, name='home'),              #Домашняя страница.
    path('contact', views.contact, name='contact')  #Контаты.
]


#Импортируем системную функцию.
from django.urls import path

#Импортируем views из этой же директории.
from . import views

urlpatterns = [
    path('start', views.start, name="start_urlshortner"), #Сократитель ссылок.
    path('urlshort/', views.urlkeep, name="short")                      #Результат сокращения.
]

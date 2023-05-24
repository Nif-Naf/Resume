#Импортируем системную библиотеку - Административную панель.
from django.contrib import admin

#Импортируем системные функции.
from django.urls import path, include
#from django.conf.urls import url

urlpatterns = [
    path('admin/', admin.site.urls),                      #Панель администратора.
    path (r'', include('Home_page.urls')),                #Домашняя страница.
    path ('urlshortner/', include('urlshortner.urls')),   #Сократитель ссылок.
    path('poll/', include('poll.urls')),                  #Опрос.
    path('binary_search/', include('binary_search.urls')) #Бинарный поиск.
]

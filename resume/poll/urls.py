#Импортируем системную функцию.
from django.urls import path

#Импортируем views из этой же директории.
from . import views

urlpatterns = [
    path('start', views.start, name = 'start_poll'),    #Начало проса.
    path('result', views.result, name = 'result_poll')  #Результаты опроса.   
]

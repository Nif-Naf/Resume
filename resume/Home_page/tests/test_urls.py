#Импортируем системный класс теста.
from django.test import SimpleTestCase

#Импортруем сиситемные функции.
from django.urls import reverse, resolve

#Импортируем представления.
from Home_page.views import show, contact

class TestUrls(SimpleTestCase):
    """Проверка файла urls.py"""

    def test_url_is_resolves_start(self):
        """Обращаемся к ссылке по ее имени и проверяем является ли имя и ссылка одним обьектом."""   
        
        #Преобразуем url в имя ссылки.
        url = reverse('home')

        #Проверяет является ли имя ссылки и сама ссылка одним и тем же обьектом.
        self.assertEqual(resolve(url).func, show)
       
    def test_url_is_resolves_result(self):
        """Обращаемся к ссылке по ее имени и проверяем является ли имя и ссылка одним обьектом."""   
        
        #Преобразуем url в имя ссылки.
        url = reverse('contact')
        
        #Проверяет является ли имя ссылки и сама ссылка одним и тем же обьектом.
        self.assertEqual(resolve(url).func, contact)    
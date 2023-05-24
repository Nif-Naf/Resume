#Импортруем сиситемные функции.
from django.test import TestCase, Client
from django.urls import reverse


#Импортируем модель.
from poll.models import Question_poll


class TestViews(TestCase):
    """Проверка файла views.py"""

    def setUp(self) -> None:
        """Инициализировать переменные/обьекты для теста."""
        
        self.client = Client()
        self.start_url = reverse('start_poll')

        return super().setUp()
 
    def test_project_POST(self):
        """Отсылаем запрос в представление. Ожидаем переадресацию на другую страницу."""

        #Отправляем запрос. Данные в виде словаря.
        response = self.client.post(self.start_url, {
            'name_db': 'Test Test Test',
            'professional_db': 'QA tester',
            'sex_db': 'Женский',
            'it_db': 'Негативное'
        })

        #Получаем статус-код и сверяем его с эталонным.
        self.assertEqual(response.status_code, 302)
        
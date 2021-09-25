#Импортируем системный класс теста.
from django.test import SimpleTestCase

#Импортируем форму.
from poll.forms import Question_pollForm

class TestForms(SimpleTestCase):
    """Проверка файла forms.py"""

    def test_form_valid(self):
        """Проверка формы на валидность."""
        form = Question_pollForm(data = {
            'name_db': 'Test',
            'professional_db': 'QA tester',
            'sex_db': 'Мужской',
            'it_db': 'Нейтральное'
        })

        self.assertTrue(form.is_valid())

    def test_form_no_data(self):
        """Проверка если форма пуста."""
        form = Question_pollForm(data = {})

        #Если форма пустая то форма не валидна и == False.
        self.assertFalse(form.is_valid())

        #Количетство ошибок == количество пустых форм.
        self.assertEqual(len(form.errors), 4)
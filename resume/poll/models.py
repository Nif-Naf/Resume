#Импортируем системную функцию для создания модели.
from django.db import models

class Question_poll(models.Model):
    """Таблица."""
    name_db = models.CharField('ФИО', max_length = 100)
    professional_db = models.CharField('Профессия', max_length = 100)
    
    sex = (('Мужской', "муж"),
        ('Женский', "жен"))
        
    sex_db = models.CharField('Пол', max_length = 10, choices = sex, default= 'Мужской')
    
    it  =(('Положительное', "Положительно. За ним будущее."),
        ('Нейтральное', "Мне все равно. Будь как будет."),
        ('Негативное', "Я считаю что эти компуктеры погубят мир."))

    it_db = models.CharField('Отношение к IT', max_length = 50, choices = it, default = 'Нейтральное')

    def __str__(self):
        """Для корректного выведения навания обьекта в shell."""
        return self.name_db
    
    class Meta:
        """Для корректного выведения названия модели/таблицы в панели администратора."""
        verbose_name = 'Опрос'
        verbose_name_plural = 'Опросы'
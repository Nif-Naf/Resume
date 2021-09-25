#Импортируем системную функцию для регистрации модели в панеле администратора.
from django.contrib import admin

#Импортируем модель из этой же директории в файле models.
from .models import Question_poll

#Регистрируем модель.
admin.site.register(Question_poll)
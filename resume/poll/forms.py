#Импортируем модель.
from django.forms.widgets import RadioSelect
from poll.models import Question_poll

#Импортируем нужный нам класс. На основе которого будет работать модель.
from django.forms import ModelForm, TextInput

class Question_pollForm(ModelForm):
    """Создаем форму."""
    class Meta:
        """pass"""
        
        #Указываем с какой моделью мы работаем.
        model = Question_poll
        
        #Указываем какие поля выводить.
        exclude = ()
        field = ['name_db', 'professional_db', 'sex_db', 'it_db']
        
        #Задаем свойства форме. Такие как class, placeholder  и тд.
        widgets = {
            "name_db": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'ФИО',
                'type': 'text'
            }),

            "professional_db": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ваша профессия',
                'type': 'text'
            }),

            "sex_db": RadioSelect(attrs={
                'class': 'radio-checkmark'
            }),

            "it_db": RadioSelect(attrs={
                'class':'radio-checkmark'
            })
            }
#Импортируем системную функцию для рендеринга страницы.
from django.shortcuts import render, redirect

#Импортируем модель.
from poll.models import Question_poll

#Импортируем форму.
from poll.forms import Question_pollForm

def start(request):
    """Загрузка страницы/получение/обработка информации."""
    
    #Пустая строка для ошибок.
    error = ''

    if request.method == 'POST':
        """Если метод POST."""

        #Входные данные от клиента.
        form = Question_pollForm(request.POST)

        if form.is_valid:
            """Если данные валидны сохраняем их в БД и переходим к результатам."""
                
            #ФИО человека от клиета.
            name_form = request.POST['name_db']
            
            #Удостоверяемся есть ли человека с такой же фамилией из модели.
            #Если есть то получим список с именами.
            name_model = Question_poll.objects.filter(name_db = name_form)

            if len(name_model) > 0:  #Если список не пустой значит человек с таким именем проходил опрос. Если пустой значит запись считаем уникальной.
                """Если данные повторяются."""
                
                error = 'Человек с таким именем уже прошел опрос.'
                data = {
                    'form': form,
                    'error': error
                }   
                return render(request, 'poll/start_poll.html', data)

            #Сохраняем данные в модели.
            form.save()

            #Переходим на страницу с результатами опроса.
            return redirect('result_poll')
        
        else:
            """Если данные не валидны."""
            
            error = 'Введенные данные не корректны.'
            data = {
                'form': form,
                'error': error
            }   
            return render(request, 'poll/start_poll.html', data)

    #Определяем какая нам нужна форма.
    form = Question_pollForm

    #Создаем словарь для вывода формы на стартовую страницу.
    data = {
        'form': form,
        'error': error
    }

    #Загружаем форму и шаблон для стартовой страницы.
    return render(request, 'poll/start_poll.html', data)





def result(request):
    """Просмотр результатов теста."""
    q = Question_poll.objects.all()
    return render(request, 'poll/result_poll.html', context = {'result': q})
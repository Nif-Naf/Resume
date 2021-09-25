#Импортируем системную функцию для рендеринга страницы.
from django.shortcuts import render

#Импортируем библиотеку math.
import math


def start(request):
    """Загружаем стартовую страницу."""
    return render(request, 'binary_search/binary_search.html')

def result(request):
    """Обработчик."""
   
    #Пустая строка для ошибок.
    error = ''

    if request.method == "POST":
        """Проверяем метод."""
        
        #Получение данных для генерации.
        start = int(request.POST['one'])
        end = int(request.POST['two']) 
        choice = int(request.POST['three'])

        #Проверяем входные данные.
        if start >= end or choice == end or choice == start:
            """Если одни и те же значения в данных."""
            
            error = 'Некорректный ввод.'
            result = {
                'error': error
            }
            return render(request, 'binary_search/binary_search.html', result)


        elif abs(start + end) >= 5000 or abs(start + end) <= 3:
            """Максимально/Минимально элементов."""
            
            error = 'Максимально/Минимально элементов.'
            result = {
                'error': error
            }
            return render(request, 'binary_search/binary_search.html', result)

        elif start == 0 or end == 0 or choice == 0:
            """Исключаем ноль из последовательности."""
            
            error =  'Ноль не может быть элементом.'
            result = {
                'error': error
            }
            return render(request, 'binary_search/binary_search.html', result)

        elif end <= choice:
            """Местоположение искомого элемента."""
            
            error =  'Некорректный искомый элемент.'
            result = {
                'error': error
            }
            return render(request, 'binary_search/binary_search.html', result)

        #Пустая последовательность.
        numbers = []

        #Генерация последовательности.
        for i in range(start, end):
            numbers.append(i)
        
        #Количество элементов последовательности.
        num = len(numbers) 
        
        #Обьявление переменных для алгоритма.
        score = 0
        low = 0
        high = len(numbers) - 1

        #Алгоритм.
        while low <= high:
            """Цикл выполнения алгоритма."""
            mid = int((low + high)/2)
            guess = numbers[mid]

            score += 1

            if guess == choice:
                """Верно."""
                break

            elif guess > choice:
                """Много."""
                high = mid - 1

            elif guess < choice:
                """Мало."""
                low = mid + 1

            else:
                """Неизвестная ошибка в цикле."""
                
                error = 'Неизвестная ошибка.'
                result = {
                    'error': error,
                }
                return render(request, 'binary_search/binary_search.html', result)

        #Расчет попыток поиска для алгоритма.
        log = int(math.log(num,2))
        
        #Обработанные данные для клиента.
        result = {
            'one': start,
            'two': end,
            'three': choice,
            'score': score,
            'find': guess,
            'numbers': num,
            'loga': log
        }

        return render(request, 'binary_search/binary_search_result.html', result)

    else:
        """Если не корректный метод запроса."""
        
        error = 'Некорректный метод запроса.'
        result = {
            'error': error
        }
        return render(request, 'binary_search/binary_search.html', result)
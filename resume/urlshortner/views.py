#Импортируем системную функцию для рендеринга страницы.   
from django.shortcuts import render

#Импортируем функцию для сокращения ссылок.
from pyshorteners import Shortener

def start(request):
     """Загружаем основную страницу."""
     return render(request, 'urlshortner/urlshortner.html')


def urlkeep(request):  
     """Обработчик."""
     
     #Пустая строка для ошибок.
     error = ''

     if request.method == "POST":
          """Проверяем метод и подготавливаем обьект к проверке на корректность."""    
          url_obj = request.POST['link_short'] #Получаем обьект. Это строка.
          url_split = url_obj.split('.') #Разбиваем строку на элементы. Получам список.
          url_str = url_split[0] #Выбираем первый элемент из списка. Это будет строка.

          
          if url_str == 'www':
               """Проверка обьекта на корректность, сокращение обьекта."""

               sho = Shortener()

               result = {                              
                    'URL': sho.chilpit.short(url_obj)
               }
               return render(request, 'urlshortner/urlshortner_end.html', result) 
          
          else:
               """Если ссылка не корректна."""

               error = 'Некорректная ссылка.'
               result = {                              
                    'error': error
               }
               return render(request, 'urlshortner/urlshortner.html', result)
          
     else:
          """Если не корректный метод запроса."""
          
          erorr = 'Некорректный метод запроса.'
          result = {
              'erorr': error
          }
          return render(request, 'urlshortner/urlshortner.html', result)

     

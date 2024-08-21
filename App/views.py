from django.shortcuts import render
from django.http import HttpResponse
import random

# Представление для игры
def game_view(request):
    numbers = [random.randint(0, 3) for _ in range(3)]
    
    if numbers[0] == numbers[1] == numbers[2]:
        message = f"{numbers} Победа, все 3 числа равны!"
    elif len(set(numbers)) == 3:
        message = f"{numbers} Повезет в следующий раз!"
    else:
        message = f"{numbers} Не все числа равны, но есть совпадения."
    
    return HttpResponse(message)

# Представление для первой страницы
def index_view(request):
    return render(request, 'App/index.html')

# Представление для второй страницы
def page2_view(request):
    return render(request, 'App/page2.html')

# Представление для ссылки
def link_view(request):
    return render(request, 'App/link.html')

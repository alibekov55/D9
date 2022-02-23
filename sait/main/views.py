from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    date = {
        'title': 'Главная страница',
        'values': ['Some', 'Hello', '123'],
        'obj':{
            'car': 'BMW',
            'age': 18,
            'hobby': 'Football'
        }
    }
    return render(request, 'main/index.html', date )

def about(request):
    return render(request, 'main/about.html')

def contact(request):
    return render(request, 'main/contact.html')

def newsportal(request):
    return render(request, 'main/newsportal.html')
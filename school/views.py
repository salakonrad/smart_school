from django.shortcuts import render
from django.http import HttpResponse


posts = [
    {
        'author': 'Dyrektor',
        'title': 'Pierwsze Zebranie',
        'content': 'Zebranie pierwsze bedzie we wrzesniu',
        'date_posted': '20 Sierpnia 2020'
    },
    {
        'author': 'Nauczyciel',
        'title': 'Wycieczka szkolna',
        'content': 'Wycieczka do Wawy',
        'date_posted': '27 Kwietnia 2021'
    }
]


def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'school/home.html', context)


def about(request):
    return render(request, 'school/about.html')

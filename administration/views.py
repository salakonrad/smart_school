# Create your views here.
from django.shortcuts import render, redirect
from .forms import *
from .models import *
from administration.models import ClassRegistration


def add_class(request):
    forms = ClassForm()
    if request.method == 'POST':
        forms = ClassForm(request.POST)
        if forms.is_valid():
            forms.save()
            return redirect('create-class')
    class_obj = ClassInfo.objects.all()
    context = {
        'forms': forms,
        'class_obj': class_obj
    }
    return render(request, 'administration/create-class.html', context)


def class_registration(request):
    forms = ClassRegistrationForm()
    if request.method == 'POST':
        forms = ClassRegistrationForm(request.POST)
        if forms.is_valid():
            forms.save()
            return redirect('class-list')
    context = {'forms': forms}
    return render(request, 'administration/class-registration.html', context)


def class_list(request):
    register_class = ClassRegistration.objects.all()
    context = {'register_class': register_class}
    return render(request, 'administration/class-list.html', context)


def administration_menu(request):
    return render(request, 'administration/administration-menu.html')

from django.urls import path

from . import views

urlpatterns = [
    path('create-class', views.add_class, name='create-class'),
    path('class-registration', views.class_registration, name='class-registration'),
    path('class-list', views.class_list, name='class-list'),
]

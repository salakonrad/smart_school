from django.urls import path
from . import views
from .views import PostListView

urlpatterns = [
    path('', views.home, name='school-home'),
    # path('', PostListView.as_view(), name='school-home'),
    path('about', views.about, name='school-about'),
]

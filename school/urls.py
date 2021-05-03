from django.urls import path
from . import views
from .views import PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView, UserPostListView

urlpatterns = [
    # path('', views.home, name='school-home'),
    path('', PostListView.as_view(), name='school-home'),
    path('user/<str:username>', UserPostListView.as_view(), name='user-posts'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='school-detail'),
    path('post/create/', PostCreateView.as_view(), name='school-create'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='school-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='school-delete'),
    path('about', views.about, name='school-about'),
]

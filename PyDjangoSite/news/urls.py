from django.urls import path
from . import views



urlpatterns = [
    path('', views.NewsHome, name = 'news'),
    path('create', views.CreateNews),
    path('<int:pk>', views.NewsDetailView.as_view(), name='news-detail'),
    path('<int:pk>/update', views.NewsUpdateView.as_view(), name='news-update'),
    path('<int:pk>/delete', views.NewsDeleteView.as_view(), name='news-delete'),
]
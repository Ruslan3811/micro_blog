from django.urls import path
from .views import ArticleListView, ArticleDetailView, ArticleCreateView

urlpatterns = [
    path('', ArticleListView.as_view(), name = 'list'),
    path('article/detail/<int:pk>/', ArticleDetailView.as_view(), name = 'detail'),
    path('article/new/', ArticleCreateView.as_view(), name='create'),
]

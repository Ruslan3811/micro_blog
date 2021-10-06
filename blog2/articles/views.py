from django.shortcuts import render
from .models import Article
from django.views.generic import ListView, DetailView, CreateView
# Create your views here.
class ArticleListView(ListView):
    model = Article
    template_name = 'home.html'

class ArticleDetailView(DetailView):
    model = Article
    template_name = 'detail.html'

class ArticleCreateView(CreateView):
    model = Article
    template_name = 'create.html'
    fields = ['author', 'title', 'body']
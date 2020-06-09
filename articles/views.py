from django.shortcuts import render
from django.urls import reverse_lazy

from django.views.generic import ListView, DetailView, UpdateView, DeleteView
from .models import Article

# Create your views here.
class ArticleListView(ListView):
    model =  Article
    template_name = 'article_list.html'

class ArticleDetailView(DetailView): # new
    model = Article
    template_name = 'article_detail.html'

class ArticleUpdateView(UpdateView): # new
    model = Article
    fields = ('title', 'body',)
    template_name = 'article_edit.html'

class ArticleDeleteView(DeleteView): # new
    model = Article
    template_name = 'article_delete.html'
    success_url = reverse_lazy('article_list')

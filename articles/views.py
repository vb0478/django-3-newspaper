from django.shortcuts import render
from django.urls import reverse_lazy

from django.views.generic import ListView, DetailView, UpdateView, DeleteView, CreateView
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

class ArticleNewView(CreateView):
    model = Article
    template_name = 'article_new.html'

    #fields = ('title','body','author')
    fields = ('title','body')
    # remove author from the fields and instead
    # set it automatically via the form_valid method
    # I looked at the source code and used Google,

    # Generic class-based views are amazing for starting new projects
    # but when you want to customize them, it is necessary roll up your sleeves
    # and start to understand what’s going on under the hood.
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

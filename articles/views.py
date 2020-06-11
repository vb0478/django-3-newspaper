from django.shortcuts import render
from django.urls import reverse_lazy

from django.views.generic import ListView, DetailView, UpdateView, DeleteView, CreateView
from .models import Article, Category

from django.core.exceptions import PermissionDenied
from django.contrib.auth.mixins import LoginRequiredMixin # new

# The base View class used in Django has an internal dispatch() method
# We will check if the author of the article is indeed the same user
# who is currently logged-in and trying to make a change.
# At the top of our articles/views.py file add a line importing PermissionDenied.
# Then add a dispatch method for both ArticleUpdateView and ArticleDeleteView.
class CategoryListView(ListView):
    model =  Category
    template_name = 'category_list.html'

class CategoryDetailView(DetailView): # new
    model = Category
    template_name = 'category_detail.html'

class ArticleListView(ListView):
    model =  Article
    template_name = 'article_list.html'

class ArticleDetailView(DetailView): # new
    model = Article
    template_name = 'article_detail.html'

class ArticleUpdateView(LoginRequiredMixin, UpdateView): # new
    model = Article
    fields = ('title', 'body',)
    template_name = 'article_edit.html'
    login_url = 'login'

    def dispatch(self, request, *args, **kwargs):
        obj = self.get_object()
        if obj.author != self.request.user:
            raise PermissionDenied
        return super().dispatch(request, *args, **kwargs)

class ArticleDeleteView(LoginRequiredMixin, DeleteView): # new
    model = Article
    template_name = 'article_delete.html'
    success_url = reverse_lazy('article_list')
    login_url = 'login'

    def dispatch(self, request, *args, **kwargs):
        obj = self.get_object()
        if obj.author != self.request.user:
            raise PermissionDenied
        return super().dispatch(request, *args, **kwargs)

class ArticleNewView(LoginRequiredMixin, CreateView):
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

# To restrict view access to only logged in users,
# Django has a LoginRequired mixin
# The documentation for the LoginRequired mixin tells us the answer.
# We can add a login_url to override the default parameter.
# We’re using the named URL of our login route here, login.
    login_url = 'login'
# Nowwe see that restricting view access is just a matter of adding
# LoginRequiredMixin at the beginning of all existing views and
# specifying the correct login_url.

from django.contrib import admin

# Register your models here.
from .models import Article, Category, Comment

# wouldn’t it be better to just see all Comment models
# related to a single Post model?
# It turns out we can with a Django admin feature called
# inlines which displays foreign key relationships in a nice, visual way.

class CommentInline(admin.StackedInline): # new
    model = Comment
# or:
# class CommentInline(admin.TabularInline): model = Comment

class ArticleAdmin(admin.ModelAdmin):
    inlines = [CommentInline, ]

admin.site.register(Article, ArticleAdmin)
admin.site.register(Category)
admin.site.register(Comment)

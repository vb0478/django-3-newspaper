from django.db import models

from django.conf import settings
from django.contrib.auth import get_user_model
from django.urls import reverse

# Create your models here.
class Category(models.Model):
     title = models.CharField(max_length=150, blank=True, verbose_name='Nazwa Kategorii')

     def __str__(self):
         return self.title

     def get_absolute_url(self):
         return reverse('category_detail', kwargs={'category_id':self.pk})

     class Meta:
         verbose_name = 'Kategoria'
         verbose_name_plural = 'Kategorii'
         ordering = ['title']

class Article(models.Model):
    title = models.CharField(max_length=150)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    edited_at = models.DateTimeField(auto_now=True)
     #image = models.ImageField()
    author = models.ForeignKey(
        get_user_model(), on_delete = models.PROTECT
    )
    category = models.ForeignKey(Category, on_delete=models.PROTECT, blank=True, null=True)

    def __str__(self):
        return self.title

#????
    def get_absolute_url(self):
        return reverse('article_detail', args=[str(self.id)])

    class Meta:
        pass

# Authorization restricts access;
# authentication enables a user sign up and log in flow.

class Comment(models.Model):
    comment = models.CharField(max_length=250)
    author = models.ForeignKey(get_user_model(), on_delete = models.PROTECT,)
    article = models.ForeignKey(Article,
                                on_delete=models.CASCADE,
                                related_name='comments',)

    def __str__(self):
        return self.comment[:60]

    def get_absolute_url(self):
         return reverse('article_list')

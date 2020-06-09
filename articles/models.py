from django.db import models

from django.conf import settings
from django.contrib.auth import get_user_model
from django.urls import reverse

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=150)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    edited_at = models.DateTimeField(auto_now=True)
     #image = models.ImageField()
    author = models.ForeignKey(
        get_user_model(), on_delete = models.PROTECT
    )

    def __str__(self):
        return self.title

#????
    def get_absolute_url(self):
        return reverse('article_detail', args=[str(self.id)])

    class Meta:
        pass


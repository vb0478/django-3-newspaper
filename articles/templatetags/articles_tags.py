from django import template
from articles.models import Category

register = template.Library()

@register.simple_tag() # name='new_name'
def get_categories():
    return Category.objects.all()

@register.inclusion_tag(filename='articles/templates/articles/category_list.html') # +path to template
def show_categories(self):
    categories = Category.objects.all()
    return {'categories': categories}


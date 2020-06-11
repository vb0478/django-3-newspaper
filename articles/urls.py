from django.urls import path

from .views import ( ArticleListView,
                     ArticleUpdateView,
                     ArticleDetailView,
                     ArticleDeleteView, ArticleNewView,
    CategoryListView, CategoryDetailView # new
)

urlpatterns = [
    path('<int:pk>/edit/', ArticleUpdateView.as_view(), name='article_edit'), # new
    path('<int:pk>/delete/', ArticleDeleteView.as_view(), name='article_delete'),
    path('<int:pk>/', ArticleDetailView.as_view(), name='article_detail'), # new

    path('new/', ArticleNewView.as_view(), name='article_new'),
    path('cat/', CategoryListView.as_view(), name='category_list'),
    path('cat/<int:pk>/', CategoryDetailView.as_view(), name='category_detail'),
    path('', ArticleListView.as_view(), name='article_list'),
]

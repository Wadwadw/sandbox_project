from django.urls import path
from .views import ArticleList

app_name = 'blog'

urlpatterns = [
    path('article-list/', ArticleList.as_view())
]
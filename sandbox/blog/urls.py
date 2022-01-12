from django.urls import path
from .views import ArticleListView, ArticleDetailView

app_name = 'blog'

urlpatterns = [
    path('article-list/', ArticleListView.as_view()),
    path('article-detail/<int:pk>', ArticleDetailView.as_view())
]
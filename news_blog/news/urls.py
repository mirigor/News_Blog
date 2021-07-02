from django.urls import path
from .views import *

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('news/<slug:news_slug>/', ViewNews.as_view(), name='view_news'),
    path('tag/<slug:slug>/', NewsByTag.as_view(), name='tag'),
    path('statistics/', StatisticsView.as_view(), name='statistics'),
]
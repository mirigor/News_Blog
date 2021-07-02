from .models import *
from django.views import generic
from django.db.models import F


class HomeView(generic.ListView):
    """Главная страница новостей"""

    model = News
    template_name = 'news/index.html'
    context_object_name = 'news'


class ViewNews(generic.DetailView):
    """Страница конкретной новости"""

    model = News
    template_name = 'news/single.html'
    context_object_name = 'news'
    slug_url_kwarg = 'news_slug'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        self.object.views = F('views') + 1
        self.object.save()
        self.object.refresh_from_db()
        return context


class NewsByTag(generic.ListView):
    """Новости по тэгу"""

    template_name = 'news/index.html'
    context_object_name = 'news'

    def get_queryset(self):
        return News.objects.filter(tags__slug=self.kwargs['slug'])


class StatisticsView(generic.ListView):
    """Страница статистики по просмотрам"""

    model = News
    template_name = 'news/statistics.html'
    context_object_name = 'news'

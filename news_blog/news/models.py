from django.db import models
from django.urls import reverse


class Tag(models.Model):
    class Meta:
        verbose_name = 'Тэг'
        verbose_name_plural = 'Тэги'
        ordering = ['title']

    title = models.CharField(max_length=50, unique=True, verbose_name='Название тэга')
    slug = models.SlugField(max_length=50, unique=True, verbose_name='URL')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('tag', kwargs={'slug': self.slug})


class News(models.Model):
    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'
        ordering = ['title']

    title = models.CharField(max_length=150, unique=True, verbose_name='Название новости')
    slug = models.SlugField(max_length=150, unique=True, verbose_name='URL')
    text = models.TextField(verbose_name='Текст новости')
    picture = models.ImageField(upload_to='photos/%Y/%m/%d/', verbose_name='Картинка', blank=True, null=True)
    views = models.IntegerField(verbose_name='К-во просмотров', default=0)
    tags = models.ManyToManyField('Tag', related_name='news', verbose_name='Тэги')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('view_news', kwargs={'news_slug': self.slug})



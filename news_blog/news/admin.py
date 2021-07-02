from django.contrib import admin
from django.utils.safestring import mark_safe
from .models import *


class TagAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    list_display_links = ('id', 'title')
    prepopulated_fields = {'slug': ('title',)}
    fields = ('title', 'slug',)


class NewsAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'views', )
    list_display_links = ('id', 'title')
    prepopulated_fields = {'slug': ('title',)}
    fields = ('title', 'slug', 'text', 'picture', 'tags', 'views')
    readonly_fields = ('views',)



admin.site.register(Tag, TagAdmin)
admin.site.register(News, NewsAdmin)
admin.site.site_title = 'Управление новостями'
admin.site.site_header = 'Управление новостями'

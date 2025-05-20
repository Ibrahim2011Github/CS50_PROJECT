from django.contrib import admin
from .models import *
# Register your models here.
class ItalyAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'time_create', 'is_published')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'content')
    list_editable = ('is_published',)
    list_filter = ('is_published', 'time_create')
    # list_filter = ('time_create', 'is_published')
    # prepopulated_fields = {'slug': ('title',)}
    # save_on_top = True
    # fields = ('title', 'content', 'photo', 'time_create', 'time_update', 'is_published', 'cat')
    
admin.site.register(Italy, ItalyAdmin)

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')
    search_fields = ('name',)
    # list_editable = ('is_published',)
    # list_filter = ('is_published', 'time_create')
    # prepopulated_fields = {'slug': ('name',)}
    # save_on_top = True
    
admin.site.register(Category, CategoryAdmin)


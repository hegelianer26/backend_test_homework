from django.contrib import admin
# из файла models импортируем модель Post
from .models import Post, Group

class PostAdmin(admin.ModelAdmin):
    list_display = ("pk", "text", "pub_date", "author") 
    list_display_links = ("pk", "text") 
    search_fields = ("text",) 
    list_filter = ("pub_date",) 
    empty_value_display = "-пусто-" # это свойство сработает для всех колонок: где пусто - там будет эта строка 

class GroupAdmin(admin.ModelAdmin):
    list_display = ("pk", "title", "description") 
    list_display_links = ("pk", "title") 
    prepopulated_fields = {'slug': ('title',)}
    search_fields = ("title",) 
    list_filter = ("title",) 



admin.site.register(Post, PostAdmin) 
admin.site.register(Group, GroupAdmin) 
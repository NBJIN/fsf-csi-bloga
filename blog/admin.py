from django.contrib import admin
from .models import Create
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Create)
class CreateAdmin(SummernoteModelAdmin):
    list_display = ('name', 'slug', 'contributor_create', 'date_of_post', 'update_post', 'image', 'content', 'no_of_likes', 'excerpt', 'status')
    list_filter = ('status', 'name', 'contributor_create', 'date_of_post', 'content')
    search_fields = ['name', 'content']
    prepopulated_fields = {'slug': ('name',)}
    summernote_fields = ('content')

# @admin.register(Comments)

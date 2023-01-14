from django.contrib import admin
from .models import Create, Comment
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Create)
class CreateAdmin(SummernoteModelAdmin):

    list_display = ('name', 'slug', 'contributor_create', 'date_of_post')
    list_filter = ('status', 'name', 'contributor_create', 'date_of_post',)
    search_fields = ['name', 'content']
    prepopulated_fields = {'slug': ('name',)}
    summernote_fields = ('content')

# @admin.register(Comments)

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):

    list_display = ('contributor_comment', 'email', 'date_of_comment', 'content')
    list_filter = ('contributor_comment', 'date_of_comment', 'email', 'content', 'approved')
    search_fields = ['contributor_comment', 'content', 'approved']
    actions = ['approve_comment']

    def approve_comment(self, request, queryset):
        queryset.update(approved=True)
    


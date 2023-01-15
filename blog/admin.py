from django.contrib import admin
from .models import Create, Comment, Update, Delete
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
    list_filter = ('contributor_comment', 'date_of_comment', 'email', 'approved')
    search_fields = ['contributor_comment', 'content', 'approved']
    actions = ['approve_comment']

    def approve_comment(self, request, queryset):
        queryset.update(approved=True)


@admin.register(Update)
class UpdateAdmin(admin.ModelAdmin):

    list_display = ('contributor', 'email', 'date_updated', 'content', 'approved')
    list_filter = ('contributor', 'email', 'date_updated', 'content', 'approved')
    search_fields = ['contributor', 'content']
    actions = ['approve_update']


    def approve_update(self, request, queryset):
        queryset.update(approved=True)


@admin.register(Delete)
class DeleteAdmin(admin.ModelAdmin):
    list_display = ('contributor', 'email', 'date_deleted', 'approved')
    list_filter = ('contributor', 'email', 'date_deleted', 'approved')
    search_fields = ['contributor', 'date_deleted']
    actions = ['approve_delete']


    def approve_delete(self, request, queryset):
        queryset.delete(approved=True)

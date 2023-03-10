# standard
from django.contrib import admin
# added models from models.py file
from .models import Create, Comment, Update, Delete, CloudinaryField, Register_User, login
# added models for adding summer note
from django_summernote.admin import SummernoteModelAdmin

#  added create admin model


@admin.register(Create)
class CreateAdmin(SummernoteModelAdmin):
    # list that will be displayed in admin page
    list_display = ('name', 'slug', 'contributor_create', 'date_of_post', 'status')
    # fields that you can filter by
    list_filter = ('status', 'name', 'contributor_create', 'date_of_post')
    search_fields = ['name', 'content']
    # name field will be generated automatically by slug
    prepopulated_fields = {'slug': ('name',)}
    # field that summernote will be applied to
    summernote_fields = ('content')

# @admin.register(Comments)

#  added comment admin model


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):

    list_display = ('contributor_comment', 'email', 'date_of_comment', 'content', 'approved')
    list_filter = ('contributor_comment', 'date_of_comment', 'email', 'approved')
    search_fields = ['contributor_comment', 'approved']
    actions = ['approve_comment']
    # approve comments

    def approve_comment(self, request, queryset):
        queryset.update(approved=True)


@admin.register(Update)
class UpdateAdmin(admin.ModelAdmin):

    list_display = ('contributor', 'email', 'date_updated', 'content', 'approved')
    list_filter = ('contributor', 'email', 'date_updated', 'approved')
    search_fields = ['contributor', 'approved']
    actions = ['approve_update']

    def approve_update(self, request, queryset):
        queryset.update(approved=True)


@admin.register(Delete)
class DeleteAdmin(admin.ModelAdmin):
    list_display = ('contributor', 'email', 'date_deleted', 'approved')
    list_filter = ('contributor', 'email', 'date_deleted', 'approved')
    search_fields = ['contributor', 'date_deleted']
    actions = ['approve_delete']

    # admin.site.register(login)

    # admin.site.register(Register_User)

    # def approve_delete(self, request, queryset):
    #     queryset.delete(approved=True)

# @admin.register(Image)
# class ImageAdmin(admin.ModelAdmin):
#     image = CloudinaryField(null=True, blank=True, upload_to="images/")

# #     def __str__(self):
#         return self.caption if self.caption != "" else "No caption"


#         @admin.register(Photo)
#     image = CloudinaryField('image')
#     caption = models.CharField(max_length=100, blank=True)

#     def __str__(self):
#         return self.caption if self.caption != "" else "No caption"

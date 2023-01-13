from django.contrib import admin
from .models import Create 
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Create)
class CreateAdmin(SummernoteModelAdmin):

    summernote_fields = ('content')



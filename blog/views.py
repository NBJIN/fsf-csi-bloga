from django.shortcuts import render
from django.views import generic
from .models import Create
from django.http import HttpResponse


# Create your views here


# class CreateList(generic.ListView):
    # queryset = Create.objects.filter(status=1).order_by('-date_of_comment')
    # template_name =

from django.shortcuts import render
from django.views import generic
from django.http import HttpResponse
from .models import Create
from django.template import loader


class CreateList(generic.ListView):
    model = Create
    queryset = Create.objects.filter(status=1).order_by('-date_of_post')
    template_name = 'Create.html'
    paginate_by = 6


# def csibloga(request):
    # return HttpResponse('Hello')


# def csibloga(request):
    # template = loader.get_template('base.html')
    # return HttpResponse(template.render())


# Create your views here


# class CreateList(generic.ListView):
    # queryset = Create.objects.filter(status=1).order_by('-date_of_comment')
    # template_name =

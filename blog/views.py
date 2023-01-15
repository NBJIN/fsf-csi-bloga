from django.shortcuts import render
from django.views import generic
from django.http import HttpResponse
from django.template import loader


def csibloga(request):
    return HttpResponse('Hello')


def csibloga(request):
    template = loader.get_template('base.html')
    return HttpResponse(template.render())


# Create your views here


# class CreateList(generic.ListView):
    # queryset = Create.objects.filter(status=1).order_by('-date_of_comment')
    # template_name =

# standard
from django.shortcuts import render
# added import generic library
from django.views import generic
# added import create model
from .models import Create


# added Create List class which is going to inherit from generic.listview
class CreateList(generic.ListView):
    model = Create
    # added want only published posts to be visible to the user
    queryset = Create.objects.filter(status=1).order_by('-date_of_post')
    # added name of html file
    template_name = 'Index.html'
    # added only want to see 6 post at at time on page
    paginate_by = 6

# from django.http import HttpResponse
# from models import views
# from models import Create
# from django import forms

# from .forms import ImageForm
# from django.template import loader


# def base(request):
    # return render(request, 'base.html', {})


# def CreateList(request):
    # return render(request, 'Create.html', {})


# class CreateList(generic.ListView):
#     model = Create
#     queryset = Create.objects.filter(status=1).order_by('-date_of_post')
#     template_name = 'Create.html'
#     paginate_by = 6


# def upload(request):
#     context = dict(backend_form=ImageForm())

#     if request.method == 'Image':
#         form = ImageForm(request.Image, request.FILES)
#         context['Image'] = form.instance
#     if form.is_valid():
#         form.save()

#         return render(request, 'blog-image', context)

#     if request.method == 'blog-image'

    # def base(request):
    # return render(request, 'base.html')

# def csibloga(request):
    # return HttpResponse('Hello')


# def csibloga(request):
    # template = loader.get_template('base.html')
    # return HttpResponse(template.render())


# class CreateList(generic.ListView):
    # queryset = Create.objects.filter(status=1).order_by('-date_of_comment')
    # template_name = "Create.html"
# Create your views here

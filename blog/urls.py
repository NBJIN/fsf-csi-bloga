from . import views
from django.urls import path


urlpatterns = [
    path('', views.CreateList.as_view(), name='home')
]

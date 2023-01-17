from . import views
from django.url import path

urlpatterns = [
    path('', views.CreateList.as_view(), name='home')
]

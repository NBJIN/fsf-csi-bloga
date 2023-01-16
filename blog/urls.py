from . import views
from django.contrib import admin
from django.urls import path, include, base
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('summernote/', include('django_summernote.urls')),
    # path('', include('blog.urls'), name='blog_urls'),
   
]

urlpatterns = [
    # path('admin/', admin.site.urls),
    # path('', include('csibloga.urls')),
    # path('', views.CreateList.as_view(), name='base')
]

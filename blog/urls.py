from . import views
# standard
from django.contrib import admin
# standard to path , include allowss to include urls for other files
from django.urls import path, include, base
from django.contrib.auth import views as auth_views


urlpatterns = [
    # standard
    path('admin/', admin.site.urls),
    # added url for summernote
    path('summernote/', include('django_summernote.urls')),
    # path('', include('blog.urls'), name='blog_urls'),
]

# urlpatterns = [
#     # path('admin/', admin.site.urls),
#     # path('', include('csibloga.urls')),
#     # path('', views.CreateList.as_view(), name='base')
# ]

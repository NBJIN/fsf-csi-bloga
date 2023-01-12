from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

STATUS = ((0, "Draft"), (1, "Published"))

# Create your models here.


class Create(models.Model):
    name = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_lenght=200, unique=True)
    contributor = models.ForeignKey(User, on_delete=models.CASCADE, related_name='contributor') 
    date_of_post = models.DateTimeField(auto_created=True)
    update_post = models.DateTimeField(auto_created=True)
    image = Clouinary.models.CloudinaryField('image', default='placeholder')
    content = models.TextField()
    no_of_likes = models.ManyToManyField(User, related_name="likes")
    comment = models.TextField()
    excerpt
    status = models.IntegerField(choices=STATUS, default=0)



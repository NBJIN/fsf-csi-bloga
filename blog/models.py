from django.db import models
from django.contrib.auth.models import User, timezone
from cloudinary.models import CloudinaryField

STATUS = (
    (0, "Draft"),
    (1, "Published")
    )

# Create your models here.


class Create(models.Model):
    name = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    contributor_create = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_create')
    date_of_post = models.DateTimeField(auto_created=True)
    update_post = models.DateTimeField(auto_now_add=True)
    image = CloudinaryField('image', default='placeholder')
    content = models.TextField()
    no_of_likes = models.ManyToManyField(User, related_name="blog_likes")
    excerpt = models.TextField()
    status = models.IntegerField(choices=STATUS, default=0)

    class Meta:
        ordering = ['-date_of_post']

    def __str__(self):
        return self.name

    def no_of_likes(self):
        return self.likes.count()


class Comment(models.Model):
    contributor_comment = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_comment')
    email = models.EmailField()
    date_of_comment = models.DateTimeField(auto_created=True)
    image = CloudinaryField('image', default='placeholder')
    content = models.TextField()
    no_of_comments = models.ManyToManyField(User, related_name="blog_comment")
    approved = models.BooleanField(default='false')

    class Meta:
        ordering = ['-date_of_comment']

    def __str__(self):
        return self.contributor_comment

    def no_of_comments(self):
        return self.comments.count()


class update(models.Model):
    contributor = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_update')
    email = models.EmailField()
    date_updated = models.DateTimeField(auto_created=True)
    content = models.TextField()
    approved = models.BooleanField(default='false')

    class Meta:
        ordering = ['-date_updated']

    def __str__(self):
        return self.contributor


class delete(models.Model):
    contributor = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_delete')
    email = models.EmailField()
    date_deleted = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default='false')

    def __str__(self):
        return self.contributor

# standard import
from django.db import models
# added user model
from django.contrib.auth.models import User, timezone
#  added cloudinary field for featured image
from cloudinary.models import CloudinaryField


# added tupple status to show wheather our post is draft or published
STATUS = (
    (0, "Draft"),
    (1, "Published")
    )

# models below

# Create a post model


class Create(models.Model):
    name = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    contributor_create = models.ForeignKey(User, on_delete=models.CASCADE, related_name='create')
    date_of_post = models.DateTimeField(auto_created=True)
    update_post = models.DateTimeField(auto_now_add=True)
    image = CloudinaryField('image', default='placeholder')
    content = models.TextField()
    no_of_likes = models.ManyToManyField(User, related_name="blog_no_of_likes")
    excerpt = models.TextField()
    status = models.IntegerField(choices=STATUS, default=0)

# added show descending order of posts
    class Meta:
        ordering = ['-date_of_post']

# On admin page allow user to see name and author
    def __str__(self):
        return self.name + ' | ' + slef.contributor_create

# added show total no of likes on a post
    def no_of_likes(self):
        return self.no_of_likes.count()

# added Comment on a post model


class Comment(models.Model):
    contributor_comment = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comment')
    email = models.EmailField()
    date_of_comment = models.DateTimeField(auto_created=True)
    image = CloudinaryField('image', default='placeholder')
    content = models.TextField()
    no_of_comments = models.ManyToManyField(User, related_name="blog_comment")
    approved = models.BooleanField(default='false')


# added show descending order of comments

class Meta:
    ordering = ['-date_of_comment']

# added on admin page allow auther to see contributor
    def __str__(self):
        return self.contributor_comment()

# added show total number of comments
    def no_of_comments(self):
        return self.no_of_comments.count()

    def __str__(self):
        return f"comment {self.body} by {self.contributor_comment}"

# added Update Comment model


class Update(models.Model):
    contributor = models.ForeignKey(User, on_delete=models.CASCADE, related_name='update')
    email = models.EmailField()
    date_updated = models.DateTimeField(auto_created=True)
    content = models.TextField()
    approved = models.BooleanField(default='false')

# added on admin page allow auther to see contributor
    def __str__(self):
        return self.contributor

# added Delete Comment model


class Delete(models.Model):
    contributor = models.ForeignKey(User, on_delete=models.CASCADE, related_name='delete')
    email = models.EmailField()
    date_deleted = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default='false')

# added on admin page allow auther to see contributor
    def __str__(self):
        return self.contributor

# added Register Comment model


class Register_User(models.Model):
    contributor = models.CharField(max_length=100)
    email = models.EmailField()
    username = models.CharField(max_length=30)
    password = models.CharField(max_length=30)

# added on admin page allow auther to see contributor
    def __str__(self):
        return self.contributor

# added Register Comment model


class login(models.Model):
    username = models.CharField(max_length=30)
    password = models.CharField(max_length=30)


# class Image(models.Model):
#     # image field
#     image = CloudinaryField(null=True, blank=True, upload_to="images/")
#     # title field for image
#     caption = models.CharField(max_length=100, blank=True)

#     def __str__(self):
#         return self.caption if self.caption != "" else "No caption"

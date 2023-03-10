# Generated by Django 3.2.16 on 2023-01-12 23:21

import cloudinary.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Create',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('update_post', models.DateTimeField(auto_created=True)),
                ('date_of_post', models.DateTimeField(auto_created=True)),
                ('name', models.CharField(max_length=200, unique=True)),
                ('slug', models.SlugField(max_length=200, unique=True)),
                ('image', cloudinary.models.CloudinaryField(default='placeholder', max_length=255, verbose_name='image')),
                ('content', models.TextField()),
                ('comment_create', models.TextField()),
                ('excerpt', models.TextField()),
                ('status', models.IntegerField(choices=[(0, 'Draft'), (1, 'Published')], default=0)),
                ('contributor_create', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='blog_create', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-date_of_post'],
            },
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_of_comment', models.DateTimeField(auto_created=True)),
                ('email', models.EmailField(max_length=254)),
                ('image', cloudinary.models.CloudinaryField(default='placeholder', max_length=255, verbose_name='image')),
                ('content', models.TextField()),
                ('approved', models.BooleanField(default='false')),
                ('contributor_comment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='blog_comment', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-date_of_comment'],
            },
        ),
    ]

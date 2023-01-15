# Generated by Django 3.2.16 on 2023-01-15 00:08

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0002_auto_20230114_2121'),
    ]

    operations = [
        migrations.CreateModel(
            name='update',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_updated', models.DateTimeField(auto_created=True)),
                ('email', models.EmailField(max_length=254)),
                ('content', models.TextField()),
                ('approved', models.BooleanField(default='false')),
                ('contributor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='blog_update', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-date_updated'],
            },
        ),
        migrations.CreateModel(
            name='delete',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
                ('date_deleted', models.DateTimeField(auto_now_add=True)),
                ('approved', models.BooleanField(default='false')),
                ('contributor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='blog_delete', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
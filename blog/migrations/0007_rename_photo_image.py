# Generated by Django 3.2.16 on 2023-01-16 12:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_photo'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Photo',
            new_name='Image',
        ),
    ]

# Generated by Django 3.2.16 on 2023-01-15 16:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_login_register_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='login',
            name='password',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='login',
            name='username',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='register_user',
            name='password',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='register_user',
            name='username',
            field=models.CharField(max_length=30),
        ),
    ]
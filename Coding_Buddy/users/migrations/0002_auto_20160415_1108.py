# -*- coding: utf-8 -*-

"""Alert User's model."""

from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    """Migration's class."""

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='user',
            options={'ordering': ['username'], 'verbose_name': 'user', 'verbose_name_plural': 'users'},
        ),
        migrations.RemoveField(
            model_name='user',
            name='name',
        ),
        migrations.AddField(
            model_name='user',
            name='about_me',
            field=models.TextField(null=True, verbose_name='about me', blank=True),
        ),
        migrations.AddField(
            model_name='user',
            name='my_project_experience',
            field=models.URLField(null=True, verbose_name='URL for project', blank=True),
        ),
        migrations.AddField(
            model_name='user',
            name='my_technology',
            field=models.CharField(max_length=1000, null=True, verbose_name='my technology', blank=True),
        ),
        migrations.AddField(
            model_name='user',
            name='phone',
            field=models.CharField(max_length=50, null=True, verbose_name='phone', blank=True),
        ),
        migrations.AddField(
            model_name='user',
            name='avatar',
            field=models.ImageField(upload_to='avatar', null=True, verbose_name='My avatar', blank=True),
        ),
    ]

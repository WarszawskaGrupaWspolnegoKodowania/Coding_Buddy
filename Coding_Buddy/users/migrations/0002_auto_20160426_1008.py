# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Skill',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('programming_lang', models.CharField(verbose_name='language', max_length=255)),
                ('level', models.PositiveSmallIntegerField(verbose_name='level', validators=[django.core.validators.MaxValueValidator(5)])),
            ],
            options={
                'verbose_name': 'skill',
                'ordering': ['programming_lang'],
                'verbose_name_plural': 'skills',
            },
        ),
        migrations.RemoveField(
            model_name='user',
            name='my_technology',
        ),
        migrations.AddField(
            model_name='skill',
            name='user',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL),
        ),
    ]

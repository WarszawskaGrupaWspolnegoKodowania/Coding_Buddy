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
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('programming_lang', models.CharField(max_length=255, verbose_name='language')),
            ],
            options={
                'verbose_name': 'skill',
                'verbose_name_plural': 'skills',
            },
        ),
        migrations.CreateModel(
            name='SkillUser',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('level', models.PositiveSmallIntegerField(verbose_name='level', validators=[django.core.validators.MaxValueValidator(5)])),
                ('skill', models.ForeignKey(to='users.Skill')),
            ],
            options={
                'verbose_name': 'skill_user',
                'verbose_name_plural': 'skills_users',
            },
        ),
        migrations.RemoveField(
            model_name='user',
            name='my_technology',
        ),
        migrations.AddField(
            model_name='skilluser',
            name='user',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='skill',
            name='skills',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL, through='users.SkillUser'),
        ),
    ]

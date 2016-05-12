# -*- coding: utf-8 -*-
from __future__ import unicode_literals, absolute_import

from django.contrib.auth.models import AbstractUser
from django.core.urlresolvers import reverse
from django.core.validators import MaxValueValidator
from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.utils.translation import ugettext_lazy as _
from django.core.validators import MaxValueValidator

# from taggit.managers import TaggableManager
from tagging.fields import TagField
from tagging_autocomplete.models import TagAutocompleteField

# from taggit.managers import TaggableManager
from tagging.fields import TagField
from tagging_autocomplete.models import TagAutocompleteField

# from taggit.managers import TaggableManager
from tagging.fields import TagField
from tagging_autocomplete.models import TagAutocompleteField


@python_2_unicode_compatible
class User(AbstractUser):

    # First Name and Last Name do not cover name patterns
    # around the globe.
    about_me = models.TextField(_("about me"), null=True, blank=True)
    avatar = models.ImageField(upload_to='avatars', blank=True, null=True)
    my_project_experience = models.URLField(_("URL for project"), null=True, blank=True)
    phone = models.CharField(_("phone"), max_length=50, null=True, blank=True)

    def __str__(self):
        return '%s %s' % (self.username, self.about_me)

    def get_absolute_url(self):
        return reverse('users:detail', kwargs={'username': self.username})

    class Meta:
        verbose_name = 'user'
        verbose_name_plural = 'users'
        ordering = ['username', ]


class Skill(models.Model):

    programming_lang = models.CharField(_("language"), max_length=255)
    skills = models.ManyToManyField(User, through='SkillUser')

    def __str__(self):
        return self.programming_lang

    class Meta:
        verbose_name = 'skill'
        verbose_name_plural = 'skills'


class SkillUser(models.Model):

    user = models.ForeignKey(User)
    skill = models.ForeignKey(Skill)
    level = models.PositiveSmallIntegerField(_("level"), validators=[MaxValueValidator(5)])

    class Meta:
        verbose_name = 'skill_user'
        verbose_name_plural = 'skills_users'

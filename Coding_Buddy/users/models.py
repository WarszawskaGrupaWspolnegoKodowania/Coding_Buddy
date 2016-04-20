# -*- coding: utf-8 -*-
from __future__ import unicode_literals, absolute_import

from django.contrib.auth.models import AbstractUser
from django.core.urlresolvers import reverse
from django.db import models
from django.utils.encoding import python_2_unicode_compatible, force_bytes
from django.utils.translation import ugettext_lazy as _


@python_2_unicode_compatible
class User(AbstractUser):

    # First Name and Last Name do not cover name patterns
    # around the globe.
    my_technology = models.CharField(_("my technology"), null=True, blank=True, max_length=1000)
    about_me = models.TextField(_("about me"), null=True, blank=True)
    avatar = models.ImageField(upload_to='avatars', null=True)
    my_project_experience = models.URLField(_("URL for project"), null=True, blank=True)
    phone = models.CharField(_("phone"), max_length=50, null=True, blank=True)

    def __str__(self):
        return force_bytes('%s %s'  % (self.username, self.about_me))

    def get_absolute_url(self):
        return reverse('users:detail', kwargs={'username': self.username})

    class Meta:
        verbose_name = 'user'
        verbose_name_plural = 'users'
        ordering = ['username', ]

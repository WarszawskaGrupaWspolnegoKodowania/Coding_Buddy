from django.db import models
from django.utils.translation import ugettext_lazy as _
from ..users.models import User
from ..users.models import Skill

class Project(models.Model):

	users = models.ManyToManyField(User)

	skills = models.ManyToManyField(Skill)

	name = models.CharField(_("Name of the project"), max_length=255)

	description = models.TextField()

	expiration_date = models.DateField()

	number_of_users_required = models.IntegerField()
	
	opensource = models.BooleanField()

	url = models.URLField()

	def __str__(self):
        	return self.name

 #   def get_absolute_url(self):
 #       return reverse('users:detail', kwargs={'username': self.username})

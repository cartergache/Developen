from django.db import models
from django.contrib.auth.models import User

class Project(models.Model):
	name = models.CharField(max_length=100)
	user = models.ForeignKey(User, models.CASCADE, blank=True, null=True)

	def __str__(self):
		return self.name

class Task(models.Model):
	name = models.CharField(max_length=100)
	project = models.ForeignKey(Project, models.CASCADE, blank=True, null=True)

	def __str__(self):
		return self.name

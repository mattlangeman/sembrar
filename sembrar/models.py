from django.db import models

# Create your models here.
class Project(models.Model):
	location = models.CharField(max_length=50)
	latitude = models.DecimalField(max_digits=12,decimal_places=8)
	longitude = models.DecimalField(max_digits=12,decimal_places=8)
	#photo = models.ImageField()
	photo = models.URLField(max_length=200)
	description = models.CharField(max_length=8000)

	category=models.CharField(max_length=50)
	organization=models.CharField(max_length=50)
	tools_used = models.CharField(max_length=400)
	link = models.URLField(max_length=200)

	def __unicode__(self):
		return self.location

from django.contrib import admin
admin.site.register(Project)

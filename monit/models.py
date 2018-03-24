from django.db import models
from django.utils import timezone

class LogDataMonit(models.Model):
	dbLogTime      = models.DateTimeField(auto_now_add=True)
	dbTrafficState = models.IntegerField(default=0)
	dbTrafficText  = models.CharField(max_length=500,default="")
	dbUSState      = models.IntegerField(default=0)

	def __str__(self):
		return str(self.dbUSState)

class LogErrorMonit(models.Model):
	dbErrorMonit     = models.CharField(max_length=500)
	dbErrorTimeMonit = models.DateTimeField(auto_now_add=True)
	dbErrorCodeMonit = models.CharField(max_length=500)

	def __str__(self):
		return str(self.dbErrorMonit)

 
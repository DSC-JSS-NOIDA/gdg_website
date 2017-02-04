from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Event(models.Model):
	event_name=models.CharField(max_length=120)
	date_from=models.DateTimeField(auto_now=True,auto_now_add=False)
	date_to=models.DateTimeField(auto_now=True,auto_now_add=False)
	venue=models.CharField(max_length=120)
	speaker=models.CharField(max_length=120)
	event_type=models.CharField(max_length=120)
	registration_link=models.URLField(max_length=120)
	facebook_link=models.URLField(max_length=120)
	image=models.ImageField(upload_to="static/img/Event",null=True,blank=True)
	description=models.TextField()
	contact=models.IntegerField()
	view_count=models.IntegerField(default=0)
	

	def __unicode__(self):
		return self.event_name


class Team(models.Model):
	member_name=models.CharField(max_length=120)
	status=models.CharField(max_length=120)
	email_ID=models.EmailField(max_length=200)
	facebook_link=models.URLField(max_length=120)
	github_link=models.URLField(max_length=120)
	twitter_link=models.URLField(max_length=120)
	linkedin_link=models.URLField(max_length=120)
	image=models.ImageField(upload_to="static/img/Team",null=True,blank=True)
	position=models.CharField(max_length=120)

	def __unicode__(self):
		return self.member_name


class Project(models.Model):
	project_name=models.CharField(max_length=120)
	image=models.ImageField(upload_to="static/img/Project",null=True,blank=True)
	description=models.TextField()
	host_link=models.URLField(max_length=120)
	github_link=models.URLField(max_length=120)

	def __unicode__(self):
		return self.project_name


class Subscriber(models.Model):
	email_ID=models.EmailField(max_length=120)

	def __unicode__(self):
		return self.email_ID



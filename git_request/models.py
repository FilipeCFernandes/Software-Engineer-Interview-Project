from django.db import models

# Create your models here.
class Venue(models.Model):
    git_account = models.CharField(max_length=200)

class Data_git(models.Model):
    name = models.CharField(max_length=200)
    html_url = models.CharField(max_length=200)
    description = models.CharField(max_length=1000)
    language = models.CharField(max_length=200)
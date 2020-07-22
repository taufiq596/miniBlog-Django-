from django.db import models

# Create your models here.
#blog post model
class Post(models.Model):
    title = models.CharField(max_length=200)
    desc = models.TextField()

#user contact model

class UserContact(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    phone = models.IntegerField()
    desc = models.TextField()

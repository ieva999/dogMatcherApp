from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class UserProfile(models.Model):
    user=models.OneToOneField(User)
    grooming=models.IntegerField()
    family=models.BooleanField()
    homesize=models.IntegerField()
    dogsize=models.IntegerField()
    beingalone=models.IntegerField()
    exercise=models.IntegerField()



class Dog(models.Model):
    name = models.CharField(max_length=64, unique=True)
    #views = models.IntegerField(default=0)
    likes = models.IntegerField(default=0)
    slug = models.SlugField(unique=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Dog, self).save(*args, **kwargs)

    class Meta:
        verbose_name_plural = 'Dog'

    def __str__ (self):
        return self.name
    def __unicode__(self):
        return self.name

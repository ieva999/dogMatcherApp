from __future__ import unicode_literals
from django.db import models

# Create your models here.

class UserProfile(models.Model):
    user = models.OneToOneField(User)
    name = models.CharField(max_length=64, unique=True)
    email = models.EmailField()

    def __str__(self):
        return self.user.username
    def __unicode__(self):
        return self.user.username

class Dog(models.Model):
    name = models.CharField(max_length=64, unique=True)
    #views = models.IntegerField(default=0)
    likes = models.IntegerField(default=0)
    slug = models.SlugField(unique=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Category, self).save(*args, **kwargs)

    class Meta:
        verbose_name_plural = 'Dog'

    def __str__ (self):
        return self.name
    def __unicode__(self):
        return self.name

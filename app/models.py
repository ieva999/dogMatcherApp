from __future__ import unicode_literals
from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class UserProfile(models.Model):
    #profile information gathered from the survey
    user=models.OneToOneField(User)
    grooming=models.IntegerField(default=0)
    family=models.IntegerField(default=0)
    homesize=models.IntegerField(default=0)
    dogsize=models.IntegerField(default=0)
    beingalone=models.IntegerField(default=0)
    exercise=models.IntegerField(default=0)


    def makeMatches(self):
        matchMeasure=0
        # loop through all the dogs
        for currentdog in Dog.objects.all():
            #calculate the matching metric in the following code
            matchMeasure=(currentdog.grooming-self.grooming)**2+\
                         (currentdog.family-self.family)**2+\
                         (currentdog.homesize-self.homesize)**2+\
                         (currentdog.dogsize-self.dogsize)**2+\
                         (currentdog.beingalone-self.beingalone)**2+\
                         (currentdog.exercise-self.exercise)**2
            #create a new matchingmetric object for this iteration of the loop
            print self.user.username
            #self.createMatch(currentdog, self, matchMeasure)

            self.createMatch(dog=currentdog, user=self, matchmetric=matchMeasure)
            #set the associated dog and user of this model along with the metric for that association
            #save the new object created in this iteration of the loop

    @staticmethod
    def createMatch(dog, user, matchmetric):
        newdog=MatchingMetric.objects.create(dog=dog, user=user, matchMetric=matchmetric)
        print dog


class Dog(models.Model):
    #Dog basic attributes which correspond to the userprofile attributes gathered from the survey
    name = models.CharField(max_length=64)
    dogImageUrl=models.URLField()
    #views = models.IntegerField(default=0)
    likes = models.IntegerField(default=0)

    #numerical attributes for the dogs which form the basis of the matching algorithm
    grooming = models.IntegerField(default=0)
    family = models.IntegerField(default=0)
    homesize = models.IntegerField(default=0)
    dogsize = models.IntegerField(default=0)
    beingalone = models.IntegerField(default=0)
    exercise = models.IntegerField(default=0)



    class Meta:
        verbose_name_plural = 'Dog'

    def __str__ (self):
        return self.name
    def __unicode__(self):
        return self.name


class MatchingMetric(models.Model):
    #this attribute stores the metric we use to perform the matching
    #the basis for the algorithm is to find a minimum value for this metric
    #this indicates that the corresonding attributes of the dog and users are closely correlated
    matchMetric=models.IntegerField(default=0)
    dog=models.ForeignKey(Dog)
    user=models.ForeignKey(UserProfile)

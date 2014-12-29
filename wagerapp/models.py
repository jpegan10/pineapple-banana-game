from django.db import models
from django.utils.encoding import smart_unicode
# Create your models here.
from django.contrib.auth.models import User
import os

class Bettor(models.Model):
    #first_name =models.CharField(max_length=120, null= True, blank=True)
    #last_name =models.CharField(max_length=120)
    #email=models.EmailField(null= True, blank=True)
    #username =models.CharField(max_length=120)
    #password=models.CharField(max_length=120,null= True, blank=True)
    #timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    user=models.OneToOneField(User)
    #Replace all ofthe above with the user field
    
    balance=models.FloatField(  null=True, blank =True)
    projected=models.FloatField( null=True, blank=True)
        
    def __unicode__(self):
        return self.user.username
    

    
    
class Game(models.Model):
    gametime=models.DateTimeField(auto_now_add = False, auto_now=False)

    home_team=models.CharField(max_length=120)
    away_team=models.CharField(max_length=120)
    started = models.BooleanField(default = False)
    completed = models.BooleanField(default = False)
    
    tied = models.BooleanField(default=False)
    home_win=models.NullBooleanField(null=True)
    home_margin=models.IntegerField(null=True, blank=True)
    
    
    def __unicode__(self):
       # if self.completed:
        gamename = self.away_team + " at " + self.home_team  
        return gamename
    

class AvailableLine(models.Model):
    team=models.CharField(max_length=120)
    game= models.ForeignKey(Game)
    spread=models.FloatField(default=0)
    pays=models.FloatField()
    
    def __unicode__(self):
        return self.team + str(self.spread) + str(self.pays)
    
    
class Wager(models.Model):
   
    bettor=models.ForeignKey(Bettor)
    line=models.ForeignKey(AvailableLine)
    
    submitted=models.DateTimeField(auto_now_add=True)
    wageramount=models.FloatField()
    
    #did you win, did you push, did we pay you
    won=models.BooleanField(default=False)
    pushed= models.BooleanField(default=False)
    paid=models.BooleanField(default =False)
    
    def __unicode__(self):
        return (self.line.team+" " + str(self.line.spread)+ " " + str(self.wageramount)+ " " + str(self.line.pays))
    
    

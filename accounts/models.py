from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify
# Create your models here.

class Team(models.Model):
    
    name = models.CharField(max_length=30,)
    nickname =models.CharField(max_length=30, null=True, blank=True)
    def __unicode__(self):
        return self.name
    
class Game(models.Model):
    away_team=models.ForeignKey(Team, related_name='away_team')
    home_team=models.ForeignKey(Team, related_name='home_team')
    gametime=models.DateTimeField(auto_now_add = False, auto_now=False)

    started = models.BooleanField(default = False)
    completed = models.BooleanField(default = False)
    
    home_score=models.IntegerField(null=True, blank=True)
    away_score=models.IntegerField(null=True, blank=True)
    
    # we can do def in manager to get things like wins, i think.
    
    def __unicode__(self):
       # if self.completed:
        gamename = self.away_team.name + " at " + self.home_team.name  
        return gamename
    
    @property
    def home_margin(self):
        margin = self.home_score - self.away_score
        return margin

class Account(models.Model):
    name=models.CharField(max_length=30, verbose_name='Gambling Team Name', default='accountname')
    holder=models.OneToOneField(User)

    balance= models.DecimalField(max_digits=12, decimal_places=2, default=10000)
    modified = models.DateTimeField(auto_now=True, editable=False)
    created = models.DateTimeField(auto_now_add=True, editable=False)
    
    
  
    def __unicode__(self):
        return self.name + "   Balance   " + str(self.balance)

class Transaction(models.Model): 
    TRANSACTION_TYPE= (
        ('Debit', 'Debit Transaction'),
        ('Credit', 'Credit Transaction')
    )
    account =models.ForeignKey(Account)
    submitted = models.DateTimeField(auto_now_add=True)
    
    previous_balance=models.DecimalField(max_digits=12, decimal_places=2)
    forward_balance=models.DecimalField(max_digits=12, decimal_places=2)
        
    amount = models.DecimalField(max_digits=12, decimal_places=2)
    t_type = models.CharField(max_length=6, choices=TRANSACTION_TYPE, default='Debit')
    public = models.BooleanField(default =False)
    
    def __unicode__(self):
        
        return self.account.name + self.account.holder.username + str(self.amount) + self.t_type


class AvailableLine(models.Model):
    RESULTS = (
        ('Won','Wager Won'),
         ('Lost','Wager Lost'),
         ('Pushed','Wager Pushed')

    )
    team=models.ForeignKey(Team)
    game= models.ForeignKey(Game)
    spread=models.DecimalField(max_digits=12, decimal_places=1, default=0)
    pays=models.DecimalField(max_digits=12, decimal_places=3, default=1.909)
    created= models.DateTimeField(auto_now_add=True)
    available=models.BooleanField(default=True)
    result=models.CharField(null=True, blank =True,max_length=20, choices=RESULTS)
    paidout=models.NullBooleanField()
    slug=models.SlugField(unique= True)
    
    def save(self, *args, **kwargs):
                self.slug = slugify(self.team.name + str(self.spread)+ str(self.pays) )
                super(AvailableLine, self).save(*args, **kwargs)
    
    def __unicode__(self):
        return self.team.name + "       "  +str(self.spread) + "       " + str(self.pays)
    

class WagerMade(Transaction):
    line=models.ForeignKey(AvailableLine)
    def __unicode__(self):
        return self.account.name + self.line.team.name + "         " +str(self.line.spread) + "         " + str(self.line.pays) + "   " + self.t_type +"       " + str(self.amount)
    
    
class WagerPaid(Transaction):
    wager=models.ForeignKey(WagerMade)
    won=models.NullBooleanField()

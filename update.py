
from datetime import datetime
import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'pineapple_gaming.settings')
import django
django.setup()
import pytz

# if i entered a home margin


def checktimes():
    newgames=Game.objects.filter(started=False)

    for game in newgames:
        if game.gametime< datetime.now():
            game.started =True
            game.save()
            lines=game.availableline_set.all()
            for line in lines:
                line.available=False
                wagers=line.wagermade_set.all()
                for wager in wagers:
                    wager.public=True
                    wager.save()
                
                line.save()
            
            

def payout(wager):
    # this should take in a specifc wager, and payout.
    
    if wager.line.result=='Won':
        pay_amount = wager.amount*wager.line.pays
    elif wager.line.result=='Pushed':
        pay_amount=wager.amount
    else:
        pay_amount=0
    
        
    previous_balance=wager.account.balance
    forward_balance=previous_balance+pay_amount
    wager.account.balance=forward_balance
    wager.account.save()
    
    new_payout = WagerPaid(wager=wager, t_type='Credit',account=wager.account,previous_balance=previous_balance,
                           forward_balance=forward_balance, amount=pay_amount, public=True)
    new_payout.save()



def update_wagers():
    #if a game is active, check to see if it has a ascore
    # if it does, that means this game is over. so lets pay out if we must
    # once we payout, we can make this public to anyone in the league
    
    
    active_games= Game.objects.filter(started=True, completed=False, home_score__isnull=False,away_score__isnull=False)
    
    #these are the games that have ended.
    for game in active_games:
        game.completed=True
        game.save()
        
        lines=game.availableline_set.all()
        for line in lines:
            
            if line.team==line.game.home_team:
                #this is a hometeam
                linemargin=line.spread+line.game.home_margin
                if linemargin >0:
                    line.result='Won'
                elif linemargin==0:
                    line.result='Pushed'
                else:
                    line.result='Lost'
                
                line.save()
                
            else:
                #this is an awayteam+
                linemargin=line.spread-line.game.home_margin
                if linemargin >0:
                    line.result='Won'
                elif linemargin==0:
                    line.result='Pushed'
                else:
                    line.result='Lost'
                line.save()
            wagers = line.wagermade_set.all()
            for wager in wagers:
                payout(wager)
                wager.line.paidout=True
                wager.line.save()

    
                
                
if  __name__ == '__main__':
    print "Starting NFL Lines population script..."
    print ""
    from accounts.models import *
    checktimes()
    update_wagers()
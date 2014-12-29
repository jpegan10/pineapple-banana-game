
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'pineapple_gaming.settings')

import django
django.setup()

def populate():
    
    teams = ["New England", 
              "NY Jets",
              "San Diego",
              "Jacksonville",
              "Houston",
              "Kansas City",
              "Cincinnati",
              "Detroit",
              "Buffalo",
              "Miami",
              "Chicago",
              "Washington",
              "Dallas",
              "Philadelphia",
              "St. Louis",
              "Carolina",
              "Tampa Bay",
              "Atlanta",
              "San Francisco",
              "Tennessee",
              "Cleveland",
              "Green Bay",
              "Baltimore",
              "Pittsburgh",
              "Denver",
              "Indianapolis",
              "Minnesota",
              "NY Giants",
              "Seattle",
              "Arizona"
             ]

    for team in teams:
        add_team(team)
        
def add_team(team):
    t=Team.objects.get_or_create(name=team)
    return t



if __name__ == '__main__':
    print "Starting Rango population script..."
    from accounts.models import *
    populate()
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'pineapple_gaming.settings')
from bs4 import BeautifulSoup as BS
import urllib2
import django
from datetime import datetime, date

from django.utils.timezone import utc

django.setup()



from accounts.models import Game, AvailableLine, Team

def populate(classname):
    #url='c:/users/jpegan10/desktop/pinnaclesports.html'
    url='http://www.pinnaclesports.com/League/Football/NFL/1/Lines.aspx'
    page=urllib2.urlopen(url)
    #page=open('c:/users/jpegan10/desktop/pinnaclesports.html')
    currentyear = str(date.today().year)
    soup=BS(page.read())
    rows=soup.find_all('tr',attrs={'class':classname})
    teamcell=''
    
    
    for row in rows:
        numcell = row.find('td', {'class':'linesRotNumBold'})
        numcellstring=numcell.text
        wagernumber=int(numcellstring)
        if wagernumber %2 ==1:
            # this is an odd:
            # it went to a awayteam
            # we get the date
            awaynumcell=numcell
            if wagernumber<5000:
                datecell= row.find('td', {'class':'linesDate'})
                awayteamcell = list(row.find('td', {'class':'linesTeam'}))
                awayspreadcell = row.find('td', {'class':'linesSpread'})
                awaymlinecell= row.find('td', {'class':'linesMLine'})
                
                
                if datecell is None:#we dont need to worry here. date is not doubled
                    pass
                else:
                    newstring=datecell.text
                    datelist=newstring.split()
                    datestring=datelist[1] + " 2014"
                    print datelist[1]
                    
                if awayteamcell is None:
                    pass
                else:
                    awayteam=awayteamcell[0].replace(u'\xa0', u' ')
                    t_away, created = Team.objects.get_or_create(name=awayteam)
                
                if awaynumcell is None:
                    pass
                else:
                    print awaynumcell.text
                if awayspreadcell is None:
                    pass
                else:
                    newstring= awayspreadcell.text
                    awayspreadlist= newstring.split()
                    print float(awayspreadlist[0])
                if awaymlinecell is None :
                    pass
                else:
                    newstring=awaymlinecell.text
                    if len(newstring)>1:
                        awaymlinelist=newstring.split()            
                    else:
                        awaymlinelist=[]
                        awaymlinelist=awaymlinelist.append(newstring)
                        
        else: # even
            homenumcell=numcell
            if wagernumber<5000:
                timecell= row.find('td', {'class':None})
                hometeamcell = list(row.find('td', {'class':'linesTeam'}))
                homespreadcell = row.find('td', {'class':'linesSpread'})
                homemlinecell= row.find('td', {'class':'linesMLine'})

                if timecell is None:#we dont need to worry here. date is not doubled
                    pass
                else:
                    
                    timestring=timecell.text
                    datetimestring= datestring + " " + timestring
                    date_object = datetime.strptime(datetimestring, '%m/%d %Y %I:%M %p')
                    date_object=date_object.replace(tzinfo=utc)
                    
                    print date_object
                if hometeamcell is None:
                    pass
                else:
                    hometeam=hometeamcell[0].replace(u'\xa0', u' ')
                    t_home, created = Team.objects.get_or_create(name=hometeam)
                  
                    g, created=Game.objects.get_or_create(away_team=t_away, home_team=t_home, gametime=date_object)
                    
                    print g
                    
                    
                if homenumcell is None:
                    pass
                else:
                    print homenumcell.text
                if homespreadcell is None:
                    pass
                else:
                    newstring= homespreadcell.text
                    homespreadlist= newstring.split()
                    print float(homespreadlist[0])
                    hsl,created=AvailableLine.objects.get_or_create(game=g,pays=1.909,team=t_home,spread=float(homespreadlist[0]))
                    asl,created=AvailableLine.objects.get_or_create(game=g,pays=1.909,team=t_away,spread=float(awayspreadlist[0]))
                    
                if homemlinecell is None :
                    pass
                else: #its not none,but is it blank
                    mline_text=homemlinecell.text
                    homemline_list=mline_text.split()
                    mline_len=len(homemline_list)
                    print ('mline len is   : %s ' %mline_len)
                    if mline_len==1:
                        print homemline_list[0]
                        hml,created=AvailableLine.objects.get_or_create(game=g,spread=0,team=t_home,pays=float(homemline_list[0]))
                        aml,created=AvailableLine.objects.get_or_create(game=g,spread=0,team=t_away,pays=float(awaymlinelist[0]))
                        
                    if mline_len==2:
                        
                        pass
                        

                    
if __name__ == '__main__':
    print "Starting NFL Lines population script..."
    print ""
    from accounts.models import *
    populate("linesAlt1")
    populate("linesAlt2")
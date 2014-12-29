from django.contrib import admin
from accounts.models import *

# Register your models here.

#class GameAdmin(admin.ModelAdmin):
    #fields = ['gametime']

class AvailableLineInline(admin.TabularInline):
    model = AvailableLine
    extra=0

class GameAdmin(admin.ModelAdmin):
    inlines=[AvailableLineInline]
    list_display=('__unicode__',  'gametime', 'started','completed', 'away_score','home_score')
    list_editable=('away_score','home_score')


class WagerMadeInline(admin.TabularInline):
    model=WagerMade
    extra=0
    


class AvailableLineAdmin(admin.ModelAdmin):
    inlines=[WagerMadeInline]
    list_display = ('team', 'game','spread','pays','available')
    
    

admin.site.register(Game,GameAdmin)
admin.site.register(AvailableLine, AvailableLineAdmin)
admin.site.register(Transaction)
admin.site.register(WagerMade)
admin.site.register(WagerPaid)
admin.site.register(Account)
admin.site.register(Team)
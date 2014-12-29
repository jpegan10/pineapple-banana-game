from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

# Register your models here.
from wagerapp.models import AvailableLine, Bettor, Game, Wager

class BettorAdmin(admin.ModelAdmin):
    fields=[  'user','balance']

admin.site.register(Bettor, BettorAdmin)

admin.site.register(Game)
admin.site.register(AvailableLine)
admin.site.register(Wager)
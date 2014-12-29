import django_tables2 as tables
from accounts.models import AvailableLine

class AvailableLineTable(tables.Table):
    class Meta:
        model = AvailableLine
        # add class="paleblue" to <table> tag
        attrs = {"class": "paleblue"}
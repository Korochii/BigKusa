import django_tables2 as tables
from home.models import Entry

class EntryTable(tables.Table):
    class Meta:
        model = Entry
        exclude = ("id", "owner")
    
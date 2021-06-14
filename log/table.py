import django_tables2 as tables
from home.models import Entry

class EntryTable(tables.Table):
    class Meta:
        model = Entry
        exclude = ("id", "user")
        template_name = "django_tables2/bootstrap4.html"
    
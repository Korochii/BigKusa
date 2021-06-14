from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from home.models import Entry
from .table import EntryTable
from django_tables2 import RequestConfig

# Create your views here.
@login_required
def index(request):
    filteredData = EntryTable(Entry.objects.filter(user=request.user).order_by('-date_added'))
    RequestConfig(request).configure(filteredData)
    # Render the HTML template index.html with the filtered data
    return render(request, 'log/index.html', {'data':filteredData})

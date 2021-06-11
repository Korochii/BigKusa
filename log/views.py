from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from home.models import Entry

# Create your views here.
@login_required
def index(request):
    filteredData = Entry.objects.filter(owner=request.user.id).order_by('date_added') # Can use -date_added for reverse order   
    # Render the HTML template index.html with the filtered data
    return render(request, 'log/index.html', {'data':filteredData})

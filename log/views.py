from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from home.models import Entry
from django.shortcuts import get_object_or_404

# Create your views here.
@login_required
def index(request):
    filteredData = Entry.objects.filter(user=request.user).order_by('-date_added')
    
    # Render the HTML template index.html with the filtered data
    return render(request, 'log/index.html', {'data':filteredData})

@login_required()
def post_remove(request, pk):
    post = get_object_or_404(Entry, pk=pk)
    post.delete()
    return HttpResponseRedirect('/log')
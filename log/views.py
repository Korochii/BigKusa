from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def index(request):
    """View function for home page of site."""
    context = {
    
    }
    # Render the HTML template index.html with the data in the context variable
    return render(request, 'log/index.html', context=context)

from django.shortcuts import render

from .models import Entry

# Create your views here.
def index(request):
    return render(request, "data/index.html", {
        "data": Entry.objects.all()
    })
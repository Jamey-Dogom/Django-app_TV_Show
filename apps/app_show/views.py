from django.shortcuts import render, HttpResponse
from apps.app_show.models import *

# Create your views here.
def index(request):
    all_shows = Show.objects.all()
    
    context = {
    "all_shows": all_shows
    }
    
    return render(request, "app_show/index.html", context)

from django.shortcuts import render, redirect
from apps.app_show.models import *
import datetime
from django.contrib import messages

# Create your views here.
def index(request):
    all_shows = Show.objects.all()

    context = {
    "all_shows": all_shows
    }
    
    return render(request, "app_show/index.html", context)

def add_show(request):
    return render(request, "app_show/addshow.html")

def create_show(request):
    # pass the post data to the method we wrote and save the response in a variable called errors
    errors = Show.objects.basic_validator(request.POST)
        # check if the errors dictionary has anything in it
    if len(errors) > 0:
        # if the errors dictionary contains anything, loop through each key-value pair and make a flash message
        for key, value in errors.items():
            messages.error(request, value)
        # redirect the user back to the form to fix the errors
        fix = '/shows/new'
        return redirect(fix)
    else:
        release = str(request.POST['release_date'])
        release = datetime.datetime.strptime(release, "%m/%d/%Y").strftime("%Y-%m-%d")

        new_show = Show.objects.create(title = request.POST['title'], network = request.POST['network'], description = request.POST['description'], release_date = release)

        show_id = new_show.id
        urlll = '/shows/{}'.format(show_id)
        print(urlll)

        return redirect(urlll)

def display_show(request, show_id):
    show = Show.objects.get(id = show_id)
    context = {
        "show": show 
        }
    return render(request, "app_show/showinfo.html", context)

def update_show(request, show_id):
    update_show = Show.objects.get(id = show_id)
    context = {
        "update_show": update_show
    }
    return render(request, "app_show/updateshow.html", context)

def update(request, show_id):
    
    errors = Show.objects.basic_validator(request.POST)
    # check if the errors dictionary has anything in it
    if len(errors) > 0:
        # if the errors dictionary contains anything, loop through each key-value pair and make a flash message
        for key, value in errors.items():
            messages.error(request, value)
        # redirect the user back to the form to fix the errors
        urlll = '/shows/{}/edit'.format(show_id)
        return redirect(urlll)
    else:
        release = str(request.POST['release_date'])
        release = datetime.datetime.strptime(release, "%m/%d/%Y").strftime("%Y-%m-%d")

        Show.objects.filter(id=show_id).update(title = request.POST['title'], network = request.POST['network'], description = request.POST['description'], release_date = release)

        urlll = '/shows/{}'.format(show_id)
        return redirect(urlll)

def delete(request, show_id):
    print("Deleting")
    Show.objects.filter(id=show_id).delete()  
    return redirect('/shows')







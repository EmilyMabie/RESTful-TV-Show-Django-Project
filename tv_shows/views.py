from django.shortcuts import render, redirect
from django.contrib import messages
from tv_shows.models import *

# Create your views here.

def index(request):
    # Number of visits to this view, as counted in the session variable.
    num_visits = request.session.get('num_visits', 0)
    request.session['num_visits'] = num_visits + 1
    context = {
        "shows": Show.objects.all(),
        'num_visits': num_visits
    }
    return render(request, "index.html", context)

def new(request):
    context = {"networks": Network.objects.all()}
    return render(request, "new.html", context)

def create(request):
    if request.method=="POST":
        errors = Show.objects.req_validator(request.POST)
        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request, value)
                return redirect('/shows/new')
        else:
            #this_show = Show.objects.get(id=show_id)
            Show.objects.create(title=request.POST["title"], network_id=request.POST["network"], release_date=request.POST["release_date"], description=request.POST["description"])
    #return redirect(f'/shows/{show_id}')
    return redirect('/shows')

def show_info(request, show_id):
    this_show = Show.objects.get(id=show_id)
    context = {"show": this_show}
    return render(request, "show_details_view.html", context)

def edit(request, show_id):
    this_show = Show.objects.get(id=show_id)
    context = {
        "show" : this_show,
        "networks": Network.objects.all(),
    }
    return render(request, "edit.html", context)

def update(request, show_id):
    if request.method=="POST":
        errors = Show.objects.req_validator(request.POST)
        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request, value)
                return redirect(f'/shows/{show_id}/edit')
        else:
            show_to_update = Show.objects.get(id=show_id)
            show_to_update.title = request.POST["title"]
            show_to_update.release_date = request.POST["release_date"]
            show_to_update.network_id = request.POST["network"]
            show_to_update.description = request.POST["description"]
            show_to_update.save()
            messages.success(request, "Show successfully updated!")
    return redirect("/shows")

def delete(request, show_id):
    show_to_delete = Show.objects.get(id=show_id)
    show_to_delete.delete()
    return redirect("/shows")
    #utilizing a form with a hidden input might make more sense in the future
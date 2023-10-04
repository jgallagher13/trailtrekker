from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Trail
from .forms import HikingForm


# Create your views here.
def home(request):
    return render(request, "home.html")


def about(request):
    return render(request, "about.html")


def trails_index(request):
    trails = Trail.objects.all()
    return render(request, "trails/index.html", {"trails": trails})


def trails_detail(request, trail_id):
    trail = Trail.objects.get(id=trail_id)
    hiking_form = HikingForm()
    return render(
        request, "trails/detail.html", {"trail": trail, "hiking_form": hiking_form}
    )


class TrailCreate(CreateView):
    model = Trail
    fields = "__all__"
    success_url = "/trails/"


class TrailUpdate(UpdateView):
    model = Trail
    fields = ["location", "distance", "est"]


class TrailDelete(DeleteView):
    model = Trail
    success_url = "/trails"


def add_hiking(request, trail_id):
    form = HikingForm(request.POST)
    if form.is_valid():
        new_hiking = form.save(commit=False)
        new_hiking.trail_id = trail_id
        new_hiking.save()
    return redirect("detail", trail_id=trail_id)

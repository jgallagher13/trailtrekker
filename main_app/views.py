import os
import uuid
import boto3
from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Trail, Photo
from .forms import HikingForm


# Create your views here.
def home(request):
    return render(request, "home.html")


def about(request):
    return render(request, "about.html")

@login_required
def trails_index(request):
    trails = Trail.objects.filter(user=request.user)
    return render(request, "trails/index.html", {"trails": trails})

@login_required
def trails_detail(request, trail_id):
    trail = Trail.objects.get(id=trail_id)
    hiking_form = HikingForm()
    return render(
        request, "trails/detail.html", {"trail": trail, "hiking_form": hiking_form}
    )


class TrailCreate(LoginRequiredMixin, CreateView):
    model = Trail
    fields = ["name", "location", "distance", "est"]
    success_url = "/trails/"

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class TrailUpdate(LoginRequiredMixin, UpdateView):
    model = Trail
    fields = ["location", "distance", "est"]


class TrailDelete(LoginRequiredMixin, DeleteView):
    model = Trail
    success_url = "/trails"

@login_required
def add_hiking(request, trail_id):
    form = HikingForm(request.POST)
    if form.is_valid():
        new_hiking = form.save(commit=False)
        new_hiking.trail_id = trail_id
        new_hiking.save()
    return redirect("detail", trail_id=trail_id)

@login_required
def add_photo(request, trail_id):
    photo_file = request.FILES.get('photo-file', None)
    if photo_file:
        s3 = boto3.client('s3')
        key = uuid.uuid4().hex[:6] + photo_file.name[photo_file.name.rfind('.'):]
        try:
            bucket = os.environ['S3_BUCKET']
            s3.upload_fileobj(photo_file, bucket, key)
            url = f"{os.environ['S3_BASE_URL']}{bucket}/{key}"
            Photo.objects.create(url=url, trail_id=trail_id)
        except Exception as e:
            print('An error occurred uploading file to S3')
            print(e)
    return redirect('detail', trail_id=trail_id)

def signup(request):
  error_message = ''
  if request.method == 'POST':
    form = UserCreationForm(request.POST)
    if form.is_valid():
      user = form.save()
      login(request, user)
      return redirect('index')
    else:
      error_message = 'Invalid sign up - try again'
  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'registration/signup.html', context)

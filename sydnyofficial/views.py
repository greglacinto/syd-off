from django.shortcuts import render
from django.http import HttpResponse

from . import models

# Create your views here.

def index(request):
  audios = models.Audio.objects.all()
  videos = models.Video.objects.all()
  images = models.Image.objects.all()
  context = {
    'audios': audios,
    'videos': videos,
    'images': images
  }
  return render(request, 'sydnyofficial/body.html', context)

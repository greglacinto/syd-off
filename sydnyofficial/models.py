from django.db import models

# Create your models here.

class Audio(models.Model):
  title = models.CharField(max_length=20)
  url = models.CharField(max_length=200)
  source = models.CharField(max_length=20)
  fanlink = models.CharField(max_length=200)

  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)

  def __str__(self):
    return self.title


class Video(models.Model):
  title = models.CharField(max_length=20)
  url = models.CharField(max_length=200)
  source = models.CharField(max_length=20)

  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)

  def __str__(self):
    return self.title

class Image(models.Model):
  title = models.CharField(max_length=20)
  alt = models.CharField(max_length=20)
  url = models.CharField(max_length=200)
  source = models.CharField(max_length=20)

  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)

  def __str__(self):
    return self.title
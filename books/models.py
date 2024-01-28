from django.db import models

# Create your models here.
from django.utils.crypto import get_random_string
from django.db import models
import os

# Create your models here.

def get_filename_ext(filepath):
    base_name = os.path.basename(filepath)
    name, ext = os.path.splitext(base_name)
    return name, ext

def upload_image_path(instance, filename):
    name, ext = get_filename_ext(filename)
    unique_id = get_random_string(length=15)
    final_name = f"image-{unique_id}{ext}"
    return f"courses/{final_name}"

def upload_video_path(instance, filename):
    name, ext = get_filename_ext(filename)
    unique_id = get_random_string(length=15)
    final_name = f"video-{unique_id}{ext}"
    return f"courses/{final_name}"


class Writer(models.Model):
    title =  models.CharField(max_length=100)
    description = models.TextField()

class Category(models.Model):
    title =  models.CharField(max_length=100)
    # description = models.TextField()

class Book(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    categories = models.ManyToManyField(Category, blank=True)
    writer = models.ForeignKey(Writer, on_delete=models.SET_NULL, null=True)
    image = models.ImageField(upload_to=upload_image_path)

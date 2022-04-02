from turtle import title
from unicodedata import category
from django.db import models
# from datetime import datetime

class Frame(models.Model):
    title = models.CharField(max_length=255)
    summary = models.CharField(max_length=255)
    category = models.CharField(max_length=255)
    pubdate = models.DateTimeField()
    full_text = models.TextField()
    # slug = ... #TODO
    # is_published = models.BooleanField() #TODO

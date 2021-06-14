from django.conf import settings
from django.db import models
from django.utils import timezone
from django.contrib.auth import get_user_model

# Create your models here.
class Entry(models.Model):
    owner = models.TextField('Owner')
    date_added = models.DateTimeField('Date Added', auto_now_add=True)
    input_text = models.TextField('Text')
    output_text = models.TextField('Translation')
    language = models.CharField('Language', max_length=120)
    remarks = models.TextField('Remarks', blank=True)
from django.conf import settings
from django.db import models
from django.utils import timezone
from django.contrib.auth import get_user_model

class Entry(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    date_added = models.DateTimeField('Date Added', auto_now=True)
    input_text = models.TextField('Text')
    output_text = models.TextField('Translation')
    language = models.CharField('Language', max_length=120)
    frequency = models.IntegerField('Frequency')
    remarks = models.TextField('Remarks', blank=True)
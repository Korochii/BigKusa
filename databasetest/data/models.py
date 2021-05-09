from django.db import models

# Create your models here.

class Entry(models.Model):
    dateAdded = models.DateTimeField()
    text = models.TextField()
    translation = models.TextField()
    remarks = models.TextField()

    def __str__(self):
        return f"{self.id}: At {self.dateAdded}, from {self.text} to {self.translation + self.remarks}"


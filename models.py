from django.db import models
from django.utils import timezone

# Create your models here.


class Task(models.Model):

    def __unicode__(self):
        return self.name

    name = models.CharField(max_length=200)
    date = models.DateField(default=timezone.now().date())
    completed = models.BooleanField(default=False)

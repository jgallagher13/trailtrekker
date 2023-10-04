from django.db import models
from django.urls import reverse

# Create your models here.
class Trail(models.Model):
    name = models.CharField(max_length=150)
    location = models.CharField(max_length=150)
    distance = models.IntegerField()
    est = models.IntegerField()

    def __str__(self):
      return self.name
    
    def get_absolute_url(self):
      return reverse('detail', kwargs={'trail_id': self.id})
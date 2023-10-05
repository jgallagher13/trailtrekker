from django.db import models
from django.urls import reverse
from datetime import date
from django.contrib.auth.models import User


BREAKS = (
    ("W", "Water"),
    ("L", "Lunch"),
    ("S", "Snack"),
    ("P", "Picture"),
)


# Create your models here.
class Trail(models.Model):
    name = models.CharField(max_length=150)
    location = models.CharField(max_length=150)
    distance = models.IntegerField()
    est = models.IntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("detail", kwargs={"trail_id": self.id})


class Hiking(models.Model):
    date = models.DateField("hiking date")
    break_type = models.CharField(max_length=1, choices=BREAKS, default=BREAKS[0][0])
    created = models.TimeField(auto_now_add=True)

    trail = models.ForeignKey(Trail, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.get_break_type_display()} on {self.date}"

    class Meta:
        ordering = ['-date', '-created']


class Photo(models.Model):
    url = models.CharField(max_length=200)
    trail = models.ForeignKey(Trail, on_delete=models.CASCADE)

    def __str__(self):
        return f"Photo for trail_id: {self.trail_id} @{self.url}"

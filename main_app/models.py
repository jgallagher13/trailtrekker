from django.db import models
from django.urls import reverse


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

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("detail", kwargs={"trail_id": self.id})


class Hiking(models.Model):
    date = models.DateField("hiking date")
    break_type = models.CharField(max_length=1, choices=BREAKS, default=BREAKS[0][0])

    trail = models.ForeignKey(Trail, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.get_break_type_display()} on {self.date}"

    class Meta:
        ordering = ["-date"]

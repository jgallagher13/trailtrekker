from django.forms import ModelForm
from .models import Hiking


class HikingForm(ModelForm):
    class Meta:
        model = Hiking
        fields = ["date", "break_type"]

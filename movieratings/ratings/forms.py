from django import forms
from django.forms import HiddenInput
from ratings.models import Rating


# dead code
class RatingForm(forms.ModelForm):
    rater = forms.CharField(widget=HiddenInput)

    class Meta:
        fields = ("rater", "movie", "rating", "time_stamp")
        model = Rating
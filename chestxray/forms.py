from .models import Testing
from django import forms

CHOICES_side=[['front','front view'],['back','back view']]
CHOICES_gender=[['male','male'],['female','female']]


class TestingForm(forms.ModelForm):
    # exclude = ['id','image','side','submitted_on','description','user']
    class Meta:
        model = Testing
        exclude = ['id', 'image', 'submitted_on', 'description', 'user']
        widgets = {
            'side': forms.Select(attrs={'class': 'form-control'}, choices=CHOICES_side),
            'gender': forms.Select(attrs={'class': 'form-control'}, choices=CHOICES_gender),
        }
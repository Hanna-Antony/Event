from django import forms
from .models import Eventappl

class Eventapplform(forms.ModelForm):
    class Meta:
        model = Eventappl
        fields = ['full_name','email','number' ]
# forms.py
from django import forms
from .models import SpliceTray, Coupler


class SpliceTrayForm(forms.ModelForm):
    class Meta:
        model = SpliceTray
        fields = '__all__'


class CouplerForm(forms.ModelForm):
    class Meta:
        model = Coupler
        fields = '__all__'
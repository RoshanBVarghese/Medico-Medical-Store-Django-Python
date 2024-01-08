from django.forms import ModelForm
from django import forms
from .models import Medicines

class MedicalForm(ModelForm):
    class Meta:
        model=Medicines
        fields='__all__'

        widgets={
            'name':forms.TextInput(attrs={'class':'form-control'}),
            'company':forms.TextInput(attrs={'class':'form-control'}),
            'price':forms.TextInput(attrs={'class':'form-control'}),
            'dosage':forms.TextInput(attrs={'class':'form-control'}),
        }
from django import forms
from . models import *

class Appointment_form(forms.ModelForm):
    class Meta:
        model=Appointment
        fields='__all__'

class Contact_form(forms.ModelForm):
    class Meta:
        model=Contact
        fields='__all__'       

from django import forms
from .models import *

class InfoForm(forms.ModelForm):
    class Meta:
        model = Info
        fields = ['first_name', 'last_name', 'department', 'phone_no', 'hostel', 'location', 'comment']

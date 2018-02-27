__author__ = 'Pavan Kotehal'

from django import forms
from .models import Student

class StudentForm(forms.ModelForm):

    class Meta:
        model = Student
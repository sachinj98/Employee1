from django import forms
from .models import Employee
from django.utils import timezone

class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ['name', 'email', 'birth_date', 'joining_date']


    def clean_birthdate(self):
        birthdate = self.cleaned_data['birthdate']
        today = timezone.now().date()
        
        if birthdate >= today:
            raise forms.ValidationError("Birthdate cannot be today or in the future.")
        
        return birthdate    
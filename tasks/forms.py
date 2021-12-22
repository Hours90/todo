from django import forms

from .models import *

class TaskForm(forms.ModelForm):

    class Meta:
        model = Task
        fields = '__all__'
        widgets = {
            'text': forms.TextInput(attrs={'placeholder': 'Create New Task', 'class':'form-control'}),
            'complete': forms.CheckboxInput(attrs={'class':'form-check-input'})
        }
from django import forms
from .models import todo


class todoAddForm(forms.ModelForm):
    class Meta:
        model = todo
        fields = ['title']
        
class todoUpdateForm(forms.ModelForm):
    class Meta:
        model = todo
        fields = ['title', 'completed']
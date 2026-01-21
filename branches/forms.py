from django import forms
from .models import Branch

class BranchForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs.setdefault('class', 'form-control')
    class Meta:
        model = Branch
        fields = [
            'name',
            'address',
            'establishment_date',
            'facilities',
            'is_active'
        ]
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
            }),
            'address': forms.TextInput(attrs={
                'class': 'form-control',
            }),
            'establishment_date': forms.DateInput(attrs={
                'class': 'form-control',
                'type': 'date'
            }),
            'facilities': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 3,

            }),
            'is_active': forms.CheckboxInput(attrs={
                'class': 'form-check-input'
            }),
        }

from django import forms
from .models import User

class UserForm(forms.ModelForm):
    password = forms.CharField(
        widget=forms.PasswordInput,
        required=False
    )

    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'branch',
            'is_active',
            'is_staff',
        ]
        widgets = {
            'username': forms.TextInput(attrs={
                'class': 'form-control',
            }),
            'email': forms.TextInput(attrs={
                'class': 'form-control',
            }),
            'establishment_date': forms.DateInput(attrs={
                'class': 'form-control',
                'type': 'date'
            }),
            'branch': forms.Select(attrs={
                'class': 'form-control',


            }),
            'is_active': forms.CheckboxInput(attrs={
                'class': 'form-check-input'
            }),
        }
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs.setdefault('class', 'form-control')

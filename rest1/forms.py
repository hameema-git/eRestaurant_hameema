from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username','password1','password2','email','first_name','last_name')
    def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.fields['username'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Username'})
            self.fields['password1'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Password'})
            self.fields['password1'].help_text ='<span style="color:yellow;font-size:15px;">(Must contain atleast 8 characters long and contain a mix of letters and numbers.)</span>'
            self.fields['password2'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Confirm Password'})
            self.fields['password2'].help_text = '<span style="color:yellow;font-size:15px;">(Re-enter the same password)</span>'
            self.fields['password2'].label='Confirm password'
            self.fields['first_name'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Enter'})
            self.fields['last_name'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Enter'})
            self.fields['username'].help_text=""



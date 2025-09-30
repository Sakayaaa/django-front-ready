from django import forms
from .models import Experience, Education, UserProfile
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User



class AddExperienceForm(forms.ModelForm):
    class Meta:
        model = Experience
        fields = ['job', 'company', 'location',
                  'start_date', 'end_date', 'current', 'description']
        widgets = {
            'job': forms.TextInput(attrs={'placeholder': '* Job Title', 'required': True}),
            'company': forms.TextInput(attrs={'placeholder': '* Company', 'required': True}),
            'location': forms.TextInput(attrs={'placeholder': 'Location'}),
            'start_date': forms.DateInput(attrs={'type': 'date'}),
            'end_date': forms.DateInput(attrs={'type': 'date'}),
            'description': forms.Textarea(attrs={'placeholder': 'Job Description', 'rows': 5, 'cols': 30}),
        }

    def clean(self):
        cleaned_data = super().clean()
        current = cleaned_data.get("current")
        end_date = cleaned_data.get("end_date")

        # If current job is checked, ignore end_date
        if current:
            cleaned_data["end_date"] = None
        return cleaned_data


class AddEducationForm(forms.ModelForm):
    class Meta:
        model = Education
        fields = ['school', 'degree', 'field',
                  'start_date', 'end_date', 'current', 'description']
        widgets = {
            'school': forms.TextInput(attrs={'placeholder': '* School or Bootcamp', 'required': True}),
            'degree': forms.TextInput(attrs={'placeholder': '* Degree or Certificate', 'required': True}),
            'field': forms.TextInput(attrs={'placeholder': 'Field Of Study'}),
            'start_date': forms.DateInput(attrs={'type': 'date'}),
            'end_date': forms.DateInput(attrs={'type': 'date'}),
            'description': forms.Textarea(attrs={'placeholder': 'Program Description', 'rows': 5, 'cols': 30}),
        }

    def clean(self):
        cleaned_data = super().clean()
        current = cleaned_data.get("current")
        if current:
            cleaned_data["end_date"] = None
        return cleaned_data


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['professional_status', 'pfp', 'company', 'website',
                  'location', 'skills', 'github', 'bio', 'twitter',
                  'facebook', 'youtube', 'linkedin', 'instagram'
        ]
        widgets = {
            'professional_status': forms.Select(attrs={'class': 'form-control'}),
            'company': forms.TextInput(attrs={'placeholder': "Company"}),
            'website': forms.TextInput(attrs={'placeholder': "Website"}),
            'location': forms.TextInput(attrs={'placeholder': "Location"}),
            'skills': forms.TextInput(attrs={'placeholder': "*Skills"}),
            'github': forms.URLInput(attrs={'placeholder': "Github Link"}),
            'bio': forms.Textarea(attrs={'placeholder': "A short bio of yourself"}),
            'twitter': forms.URLInput(attrs={'placeholder': "Twitter URL", 'class': 'form-control'}),
            'facebook': forms.URLInput(attrs={'placeholder': "Facebook URL"}),
            'youtube': forms.URLInput(attrs={'placeholder': "Youtube URL"}),
            'linkedin': forms.URLInput(attrs={'placeholder': "Linkedin URL"}),
            'instagram': forms.URLInput(attrs={'placeholder': "Instagram URL"}),
            'pfp': forms.ClearableFileInput(attrs={'class':'form-control'}),
        }
    
    # To set the default-showing value for 'professional_status' field
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['professional_status'].empty_label = "* Select Professional Status"
        
        
class RegisterForm(UserCreationForm):
    username = forms.CharField(
        widget=forms.TextInput(attrs={
            'placeholder': 'Username',
            'class': 'form-control',
            'required': True,
            'autocomplete': 'off',
        })
    )
    email = forms.EmailField(
        required=True,
        widget=forms.EmailInput(attrs={
            'placeholder': 'Email Address',
            'class': 'form-control',
            'required': True,
            'autocomplete': 'off',
        })
    )
    password1 = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'placeholder': 'Password',
            'class': 'form-control',
            'minlength': 8,
            'autocomplete': 'new-password',
        })
    )
    password2 = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'placeholder': 'Confirm Password',
            'class': 'form-control',
            'minlength': 8,
            'autocomplete': 'new-password',
        })
    )

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
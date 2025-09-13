from django import forms
from .models import Experience, Education


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

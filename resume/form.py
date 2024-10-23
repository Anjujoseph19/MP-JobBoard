from django import forms
from .models import *
from datetime import datetime

def possible_years(first_year_in_scroll, last_year_in_scroll):
    p_year = []
    for i in range(first_year_in_scroll, last_year_in_scroll, -1):
        p_year_tuple = str(i), i
        p_year.append(p_year_tuple)
    return p_year

class AddResumeForm(forms.ModelForm):
    class Meta:
        model = Resume
        exclude = ('user', )

class UpdateResumeForm(forms.ModelForm):
    class Meta:
        model = Resume
        exclude = ('user', )

class AddEducationForm(forms.ModelForm):
    start_date = forms.ChoiceField(choices=possible_years(((datetime.now()).year), 1990))
    end_date = forms.ChoiceField(choices=possible_years(((datetime.now()).year), 1990))
    class Meta:
        model = Education
        exclude = ('resume', )

class UpdateEducationForm(forms.ModelForm):
    start_date = forms.ChoiceField(choices=possible_years(((datetime.now()).year), 1990))
    end_date = forms.ChoiceField(choices=possible_years(((datetime.now()).year), 1990))
    class Meta:
        model = Education
        exclude = ('resume', )

class AddWorkForm(forms.ModelForm):
    start_year = forms.ChoiceField(choices=possible_years(((datetime.now()).year), 1990))
    end_year = forms.ChoiceField(choices=possible_years(((datetime.now()).year), 1990))
    class Meta:
        model = Work
        exclude = ('resume', )

class UpdateWorkForm(forms.ModelForm):
    start_year = forms.ChoiceField(choices=possible_years(((datetime.now()).year), 1990))
    end_year = forms.ChoiceField(choices=possible_years(((datetime.now()).year), 1990))
    class Meta:
        model = Work
        exclude = ('resume', )

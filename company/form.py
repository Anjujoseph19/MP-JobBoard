from django import forms
from .models import Company
from datetime import datetime

def possible_years(first_year_in_scroll, last_year_in_scroll):
    p_year = []
    for i in range(first_year_in_scroll, last_year_in_scroll, -1):
        p_year_tuple = str(i), i
        p_year.append(p_year_tuple)
    return p_year

#adding company form
class AddCompanyForm(forms.ModelForm):
    founded_in = forms.ChoiceField(choices=possible_years(((datetime.now()).year), 1900))
    class Meta:
        model = Company
        exclude =('user', )

#update company form
class UpdateCompanyForm(forms.ModelForm):
    founded_in = forms.ChoiceField(choices=possible_years(((datetime.now()).year), 1900))
    class Meta:
        model = Company
        exclude =('user', )
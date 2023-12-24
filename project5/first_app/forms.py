from django import forms
from django.forms.widgets import NumberInput
import datetime

BIRTH_YEAR_CHOICES = ['1980', '1981', '1982'],
FAVORITE_COLORS_CHOICES = [
    ('blue', 'Blue'),
    ('green', 'Green'),
    ('black', 'Black'),
]

class contactForm(forms.Form):
    name = forms.CharField(label='username',max_length=20)
    email = forms.EmailField(required = False)
    comment = forms.CharField(widget=forms.Textarea(attrs={'rows':3}))
    agree = forms.BooleanField()
    birth_date = forms.DateField(widget=NumberInput(attrs={'type': 'date'}))
    birth_year = forms.DateField(widget=forms.SelectDateWidget(years=BIRTH_YEAR_CHOICES))
    value = forms.DecimalField(initial='0')
    day = forms.DateField(initial=datetime.date.today)
    favorite_color = forms.ChoiceField(widget=forms.RadioSelect, choices=FAVORITE_COLORS_CHOICES)
    favorite_colors = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple,choices=FAVORITE_COLORS_CHOICES)
    # geeksforgeeks starts from here
    roll_number = forms.IntegerField( help_text = "Enter 6 digit roll number")  
    password = forms.CharField(widget = forms.PasswordInput()) 

